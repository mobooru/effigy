import os
from os import path
from flask import send_file
from pathvalidate import sanitize_filename

def getImage(directory, image):
  filename = sanitize_filename(image)
  filepath = path.join(os.environ['EFFIGY_PATH'], directory, filename)
  return send_file(filepath, attachment_filename=filename)