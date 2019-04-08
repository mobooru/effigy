from flask import Flask, request
app = Flask(__name__, static_url_path='', static_folder='./')

from insert import queue
from search import search
from auth import authenticate

from classes import WebError

@app.route("/insert")
def insertHandle():
  try:
    imgurl = request.args.get('url')
    query = request.args.get('query')
    token = request.args.get('token')

    if not token:
      return WebError("Malformed Request. Missing params: token").json()

    if not authenticate(token):
      return WebError("You are not authenticated to perform this action.").json()

    if imgurl and query:
      return queue(imgurl, query)
    else:
      if not (imgurl and query):
        return WebError("Malformed Request. Missing params: url, query").json()
      if not imgurl:
        return WebError("Malformed Request. Missing params: url").json()
      if not query:
        return WebError("Malformed Request. Missing params: query").json()
  except:
    return WebError("An error occured. Try again.").json()

@app.route("/search")
def searchHandle():
  try:
    imgurl = request.args.get('url')
    if imgurl:
      return search(imgurl)
    else:
      return WebError("Malformed Request. Missing params: url").json()
  except:
    return WebError("An error occured. Try again.").json()

@app.route("/")
def root():
  return app.send_static_file('index.html')