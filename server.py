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


with open("book_info.json", "r") as f:
	file_contents = json.load(f)
ref.set(file_contents)