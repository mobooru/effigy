from flask import Flask, request
app = Flask(__name__, static_url_path='', static_folder='./')

from insert import queue
from search import search
from auth import authenticate
from image import getImage

from classes import WebError

@app.route("/insert")
def insertHandle():
  try:
    imgurl = request.args.get('url')
    thumb = request.args.get('thumb')
    query = request.args.get('query')
    token = request.args.get('token')

    if not token:
      return WebError("Malformed Request. Missing params: token").json()

    if not authenticate(token):
      return WebError("You are not authenticated to perform this action.").json()

    if imgurl and query and thumb:
      return queue(imgurl, query, thumb)
    else:
      return WebError("Malformed Request. Required params: url, query, thumb").json()
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

@app.route("/images/<image>")
def imageHandler(image):
  try:
    return getImage('images',image)
  except Exception as e:
    return '',404

@app.route("/thumbnails/<image>")
def thumbnailHandler(image):
  try:
    return getImage('thumbnails',image)
  except Exception as e:
    return '',404

@app.route("/")
def root():
  return app.send_static_file('index.html')

app.run(port=80)