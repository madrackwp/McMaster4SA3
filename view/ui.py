import sys
sys.path.append('C:/Users/madra/OneDrive - Nanyang Technological University/McMasters/Software Arch/McMaster4SA3/model')
import database as db

# for p in sys.path:
#     print(p)
print("Establishing connection to Firebase")
connection = db.DatabaseConnection()
ref = connection.connect()
print("Connection established!")
data = ref.get()
# print(data)



class Book():
    def __init__(self, title, author, publishedDate, status):
        self._title = title
        self._author = author
        self._publishedDate = publishedDate
        self._status = status

    def __str__(self):
        toReturn = f"==========================\nBook Title: {self._title}\nAuthor: {self._author}\nWritten in: {self._publishedDate}\n=========================="
        # print("==========================")
        # print(f"Book Title: {self._title}\n")
        # print(f"Author: {self._author}\n")
        # print(f"Written in: {self._publishedDate}")
        # print("==========================")
        return toReturn

    def getBookTitle(self):
        return self._title

    def getBookAuthor(self):
        return self._author
    
    def getPublishedDate(self):
        return self._publishedDate

    def getBookStatus(self):
        return self._status



def parseInfomation(userData):
    bookLibrary = {}
    bookLibrary['reading'] = []
    bookLibrary['read'] = []
    bookLibrary['toRead'] = []
    bookData = userData["books"]
    for book in bookData:
        status = bookData[book]["status"]
        bookTitle = book
        author = bookData[book]["author"]
        status = bookData[book]["status"]
        publishedDate = bookData[book]["publishedDate"]
        newBook = Book(bookTitle, author, publishedDate, status)
        if status == "read":
            bookLibrary['read'].append(newBook)
        elif status == "toRead":
            bookLibrary['toRead'].append(newBook)
        else:
            bookLibrary['reading'].append(newBook)

        print("=============================")
        print(book)
        print(bookData[book]["author"])
        print(bookData[book]["publishedDate"])
        print(bookData[book]["status"])
        print("=============================")
    print(bookLibrary)
    print("DEBUG: SUCCESSFULLY PARSED INFO")
    return bookLibrary

    

while True:
    print("=============================")
    print("What is your Login ID")
    print("=============================")
    userName = input()
    # userData = data.get(userName)
    userRef = connection.login(userName)
    # print(userRef)
    if userRef is None:
        print("Login does not exist, please create a new account:")
        print("Please input a new userID: ")
        newUserID = input()
        result = connection.createAccount(newUserID)
        while result is None:
            #Creation failed, repeat the loop
            print("===============================================")
            print("UserID already exists, please input another one")
            print("===============================================")
            newUserID = input()
            result = connection.createAccount(newUserID)
        userName = newUserID
        userRef = result


    userData = userRef.get()
    print("===============================================")
    print(f"WELCOME {userName}")
    # print(userRef)
    print("===============================================")
    # print()
    print("1. Search for books")
    print("2. Look at my 'To Read' list")
    print("3. Look at my 'Currently Reading' List")
    print("4. Look at my 'Read' list")
    print("5. Quit")
    print("===============================================")
    bookLibrary = parseInfomation(userData)
    # print(data)
    while True:
        choice = input("What would you like to do? (Input 1-5)")

        if choice == "1":
            
            pass
        elif choice == "2":
            for book in bookLibrary['toRead']:
                print(book)
        elif choice == "3":
            for book in bookLibrary['reading']:
                print(book)
        elif choice == "4":
            for book in bookLibrary['read']:
                print(book)
        elif choice == "5":
            print("Thank you. Bye!")
            connection.updateData(userRef, userData)
            break
        else:
            print("Invalid input!")


    break


    # print("Password")

    # result = 