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
        "author":"Ping Pong",
        "publishedDate":"20221010",
        "status":"reading"
      },
      "Tales Of Chang":{
        "author":"Ching Chong",
        "publishedDate":"20221111",
        "status":"read"
      },
      "The Story of Kale":{
        "author":"King Kong",
        "publishedDate":"19991023",
        "status":"toRead"
      }
    }
  }
}
data = ref.set(testData)
print(data)
print(type(data))