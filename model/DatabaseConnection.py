import firebase_admin
from firebase_admin import db
import env as env
import json



# ref.set(testData)

# result = ref.get()
# user = ref.child("-NIZHIu1bSPKv4kg03wW")
# print(user.get())

class DatabaseConnection():
    def __init__(self):
        self.ref = None
    
    def connect(self):
        cred_obj = firebase_admin.credentials.Certificate(env.cert_url)
        databaseURL = env.dbURL
        default_app = firebase_admin.initialize_app(cred_obj, {
            'databaseURL':databaseURL
            })
        self.ref = db.reference("/")
        # cred = credentials.Certificate('/path/to/serviceAccountKey.json')
        # firebase_admin.initialize_app(cred)

        return self.ref

    def login(self, username):
        # print("DEBUG: ATTEMPING LOGIN")
        userRef = self.ref.child(username)
        data = userRef.get()
        if data is not None:
            # print("DEBUG: LOGIN SUCCESS")
            return userRef
        else: 
            # print("DEBUG: LOGIN FAILED")
            return None
            
        

    def createAccount(self, newUsername, newPassword = "password"):
        # print("DEBUG: ATTEMPTING TO CREATE ACCOUNT")
        data = self.ref.get()
        newAccount = {
            "books":{},
            "password": newPassword
        }
        if self.login(newUsername) is None:
            data[newUsername] = newAccount
            self.ref.set(data)
            # print("DEBUG: ACCOUNT CREATED!")
            return self.ref.child(newUsername)
        else:
            # print("DEBUG: ACCOUNT CREATION FAILED!")
            return None

    

    def updateData(self, userRef, data):
        # print("DEBUG: UPDATING DATA!")
        # print(data)
        userRef.set(data)

        return True

    

        
        






# print(type(ref))