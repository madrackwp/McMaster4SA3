import sys
sys.path.append('C:/Users/madra/OneDrive - Nanyang Technological University/McMasters/Software Arch/McMaster4SA3/model')
sys.path.append('C:/Users/madra/OneDrive - Nanyang Technological University/McMasters/Software Arch/McMaster4SA3/controller')
import database as db
import openLibraryAPI as openLib
import Book as Book
# for p in sys.path:
#     print(p)
# print("Establishing connection to Firebase")
connection = db.DatabaseConnection()
ref = connection.connect()
# print("Connection established!")
data = ref.get()
# print(data)

BOOK_STATUS = {
    1: "toRead",
    2: "reading",
    3: "read"
}

def prepBookLibraryToDictionary(bookLibrary):
    print(bookLibrary)
    data = {'books':{},"password": 'password'}
    for bookStatus in bookLibrary:
        for book in bookLibrary[bookStatus]:
            print(book.getBookTitle())
            print(book.getBookAuthor())
            print(book.getPublishedDate())
            print(book.getBookStatus())
            data['books'][book.getBookTitle()] = {
                "author":book.getBookAuthor(),
                "publishedDate": book.getPublishedDate(),
                "status": book.getBookStatus()
                }
    print(data)
    return data
    

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
        newBook = Book.Book(bookTitle, author, publishedDate, status)
        if status == "read":
            bookLibrary['read'].append(newBook)
        elif status == "toRead":
            bookLibrary['toRead'].append(newBook)
        else:
            bookLibrary['reading'].append(newBook)

        # print("=============================")
        # print(book)
        # print(bookData[book]["author"])
        # print(bookData[book]["publishedDate"])
        # print(bookData[book]["status"])
        # print("=============================")
    # print(bookLibrary)
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
    print(userData)
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
            api = openLib.OpenLibAPI()
            type = input("Enter your query type: ")
            query = input("Enter your search query:")

            queryString = api.queryBuilder(type, query)
            response = api.sendQuery(queryString)
            booksFromAPI = api.parseResponse(response)
            for book in booksFromAPI:
                print(book)
            
            while True:
                print("1. Add book to lists")
                print("2. Exit")
                nextInput = input("What would you like to do next?:")
                if nextInput == "1":
                    
                    input3 = input("Select which book to add: (1-5)")
                    print("1. To Read\n2. Reading\n3. Read")
                    input4 = int(input("Which list would you like to move it to?:"))
                    bookToAdd = booksFromAPI[int(input3)-1]
                    # print(BOOK_STATUS[input4])
                    bookToAdd.changeBookStatus(BOOK_STATUS[input4])
                    bookLibrary[BOOK_STATUS[input4]].append(bookToAdd)
                    # print(bookLibrary)
                    userData = prepBookLibraryToDictionary(bookLibrary)
                    connection.updateData(userRef, userData)

                else:
                    break




        elif choice == "2":
            print("================")
            print("To Read Books")
            print("================")
            for book in bookLibrary['toRead']:
                print(book)
        elif choice == "3":
            print("================")
            print("Currently Reading Books")
            print("================")
            for book in bookLibrary['reading']:
                print(book)
        elif choice == "4":
            print("================")
            print("Read Books")
            print("================")
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