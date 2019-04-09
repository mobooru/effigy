import match

from classes import Image, WebSuccess

queueItems = []

def queue(imgurl, query):
  queueItems.append(Image(imgurl, query))

  if(len(queueItems) == 1):
    handleQueue()

  return WebSuccess('Image added to process queue.').json()

def handleQueue():
  image = queueItems.pop(0)

  try:
    match.add(image.url, image.query)
    print("Added " + image.query + "to the index.")
  except:
    print("An error occured when processing " + image.url)

  if len(queueItems) > 0:
    handleQueue()