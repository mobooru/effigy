from flask import jsonify

class WebError:
  def __init__(self, message):
    self.message = message
  def json(self):
    return jsonify(
      message=self.message,
      success=False
    )

class WebSuccess:
  def __init__(self, message):
    self.message = message
  def json(self):
    return jsonify(
      message=self.message,
      success=True
    )

class Image:
  def __init__(self, url, query, thumb):
    self.url = url
    self.query = query
    self.thumb = thumb