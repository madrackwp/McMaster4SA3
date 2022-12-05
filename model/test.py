import firebase_admin
from firebase_admin import db
import env as env
import json

cred_obj = firebase_admin.credentials.Certificate(env.cert_url)
databaseURL = env.dbURL
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL':databaseURL
    })
ref = db.reference("/")

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
data = ref.set(testData)
print(data)
print(type(data))