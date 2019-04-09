import os
import pymongo

conn = pymongo.MongoClient("mongodb://"+os.environ['EFFIGY_USER']+':'+os.environ['EFFIGY_PASS']+'@'+os.environ['EFFIGY_DB']+":27017/")
db = conn['mobooru']
tokens = db['tokens']
users = db['users']

def authenticate(reqtoken):
  token = tokens.find_one({ "token": reqtoken })
  if not token:
    return False

  user = users.find_one({ "name": token['name'] })
  if not user:
    return False

  if not (user['tier'] == 'admin' or user['tier'] == 'moderator'):
    return False
  
  return True