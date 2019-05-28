import match
import os
from os import path
import requests

from classes import Image, WebSuccess

queueItems = []

def queue(imgurl, query, thumb):
  queueItems.append(Image(imgurl, query, thumb))

  if(len(queueItems) == 1):
    handleQueue()

  return WebSuccess('Image added to process queue.').json()

def handleQueue():
  image = queueItems.pop(0)

  try:
    filetype = image.url.split('.')[-1]
    filename = image.query + '.' + filetype

    img_data = requests.get(image.url).content
    with open(path.join(os.environ['EFFIGY_PATH'], 'images', filename), 'wb') as handler:
      handler.write(img_data)

    thumb_data = requests.get(image.thumb).content
    with open(path.join(os.environ['EFFIGY_PATH'], 'thumbnails', filename), 'wb') as handler:
      handler.write(thumb_data)
  except:
    print("An error occured when downloading " + image.url)
    
  try:
    match.add('http://localhost/images/' + filename, image.query)
    match.add('http://localhost/thumbnails/' + filename, image.query)
    print("Added " + image.query + "to the index.")
  except:
    print("An error occured when processing " + filename)

  if len(queueItems) > 0:
    handleQueue()