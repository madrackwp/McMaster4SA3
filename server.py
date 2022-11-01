import firebase_admin
from firebase_admin import db
import json

cred_obj = firebase_admin.credentials.Certificate('C:/Users/madra/OneDrive - Nanyang Technological University\McMasters/Software Arch/McMaster4SA3/mcmastersa-cb17c-firebase-adminsdk-xl82d-0427c135f3.json')
databaseURL = "https://mcmastersa-cb17c-default-rtdb.firebaseio.com/"

default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':databaseURL
	})

ref = db.reference("/")


with open("book_info.json", "r") as f:
	file_contents = json.load(f)
ref.set(file_contents)