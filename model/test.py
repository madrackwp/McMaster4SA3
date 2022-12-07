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
      "Legend of Po":{
        "author":"Tom",
        "publishedDate":"2010",
        "status":"reading"
      },
      "Tales Of Chang":{
        "author":"Dick",
        "publishedDate":"2013",
        "status":"read"
      },
      "The Story of Kale":{
        "author":"Harry",
        "publishedDate":"1990",
        "status":"toRead"
      }
    }
  }
}
data = ref.set(testData)
print(data)
print(type(data))