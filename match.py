from elasticsearch import Elasticsearch
from image_match.elasticsearch_driver import SignatureES

es = Elasticsearch()
ses = SignatureES(es)

from flask import jsonify

def add(url, meta):
  ses.add_image(url, metadata=meta)

def find(url):
  return jsonify(ses.search_image(url))