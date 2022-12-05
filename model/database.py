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
        return self.ref

    def login(self, username):
        userRef = self.ref.child(username)
        data = userRef.get()
        if data is not None:
            return data
        else: 
            return False
        

    def createAccount(self, newUsername, newPassword):
        data = self.ref.get()
        newAccount = {
            "books":{},
            "password": newPassword
        }
        data[newUsername] = newAccount
        self.ref.set(data)
        return self.ref.child(newUsername)
        

dbConnection = DatabaseConnection()
ref = dbConnection.connect()
print(ref.get())
dbConnection.createAccount("Wei Pin", "password123")
        
        






# print(type(ref))