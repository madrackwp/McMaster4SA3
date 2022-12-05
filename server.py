import firebase_admin
from firebase_admin import db
import json
import env as env

cred_obj = firebase_admin.credentials.Certificate(env.cert_url)
databaseURL = env.dbURL

default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':databaseURL
	})

ref = db.reference("/")

'''
Methods:
UPDATE
SET
GET

'''
# with open("model/book_info.json", "r") as f:
# 	file_contents = json.load(f)
# print(type(file_contents))
# ref.set(file_contents)
testData = {
  "Account1":
  {
    "password": "abc123",
    "books":{
      "Book1":{
        "title": "",
        "author":"",
        "publishedDate":"",
        "status":"Reading"
      },
      "Book2":{
        "title": "",
        "author":"",
        "publishedDate":"",
        "status":"Read"
      },
      "Book3":{
        "title": "",
        "author":"",
        "publishedDate":"",
        "status":"To Read"
      }
    }
  }
}




ref.set(testData)
print(ref)