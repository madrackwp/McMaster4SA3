import sys
import os
sys.path.append('C:/Users/madra/OneDrive - Nanyang Technological University/McMasters/Software Arch/McMaster4SA3/model')
sys.path.append('C:/Users/madra/OneDrive - Nanyang Technological University/McMasters/Software Arch/McMaster4SA3/controller')
sys.path.append('C:/Users/madra/OneDrive - Nanyang Technological University/McMasters/Software Arch/McMaster4SA3/view')

import DatabaseConnection as db
import OpenLibraryAPI as openLib
import Book as Book
import Library as Library
import Menus as menus
import QueryFactory as QueryFactory


connection = db.DatabaseConnection()
ref = connection.connect()
data = ref.get()
lib = Library.Library()

BOOK_STATUS = {
    1: "toRead",
    2: "reading",
    3: "read"
}

while True:
    menus.printLoginMenu()
    userName = input()
    userRef = connection.login(userName)
    if userRef is None:
        newUserID = menus.printCreateIDMenu()
        result = connection.createAccount(newUserID)
        while result is None:
            #Creation failed, repeat the loop
            os.system('cls')
            print("===============================================")
            print("USERID ALREADY EXISTS, PLEASE INPUT ANOTHER ONE")
            print("===============================================")
            newUserID = input()
            result = connection.createAccount(newUserID)
        userName = newUserID
        userRef = result
    userData = userRef.get()

    print("===============================================")
    print(f"WELCOME {userName}")
    bookLibrary = lib.rawDataToLibrary(userData)
    while True:
        menus.printMainMenu()   
        choice = input("WHAT WOULD YOU LIKE TO DO? (INPUT 1-5)")
        if choice == "1":
            api = openLib.OpenLibAPI()
            type, query = menus.queryMenu()

            if type == "query":
                generalQueryFactory = QueryFactory.generalQueryFactory()
                generalQueryFactory.generateQuery(query)
                queryString = generalQueryFactory.getQuery()
            elif type == "title":
                titleQueryFactory = QueryFactory.titleQueryFactory()
                titleQueryFactory.generateQuery(query)
                queryString = titleQueryFactory.getQuery()
            else:
                authorQueryFactory = QueryFactory.authorQueryFactory()
                authorQueryFactory.generateQuery(query)
                queryString = authorQueryFactory.getQuery()

            # print(queryString)
            # queryString = api.queryBuilder(type, query)
            response = api.sendQuery(queryString)
            os.system("cls")
            booksFromAPI = api.parseResponse(response)
            for index,book in enumerate(booksFromAPI):
                print(f"VIEWING BOOK #{index + 1}")
                print(book)
            
            while True:
                print("1. ADD BOOK TO LISTS")
                print("2. EXIT")
                nextInput = input("WHAT WOULD YOU LIKE TO DO NEXT?:")
                if nextInput == "1":
                    input3 = input("SELECT WHICH BOOK TO ADD: (1-5)")
                    print("1. TO READ\n2. READING\n3. READ")
                    input4 = int(input("WHICH LIST WOULD YOU LIKE TO MOVE IT TO?:"))
                    bookToAdd = booksFromAPI[int(input3)-1]
                    # print(BOOK_STATUS[input4])
                    bookToAdd.changeBookStatus(BOOK_STATUS[input4])
                    bookLibrary[BOOK_STATUS[input4]].append(bookToAdd)
                    # print(bookLibrary)
                    userData = lib.prepBookLibraryToDictionary()
                    connection.updateData(userRef, userData)

                else:
                    break




        elif choice == "2":
            menus.printToReadList()
            for book in bookLibrary['toRead']:
                print(book)
            choice = menus.bookListMenu()
            # print(choice)
            if choice == "1":
                #Moving books
                moveTo = menus.bookListMovementMenu(BOOK_STATUS[1])
                for book in lib.getBooksFromList(BOOK_STATUS[1]):
                    print(book)
                bookToMove = int(input("WHICH BOOK WOULD YOU LIKE TO MOVE?: "))
                lib.moveBookToDiffList(moveFrom = BOOK_STATUS[1], moveTo=BOOK_STATUS[moveTo], bookIndex = bookToMove - 1)
                userData = lib.prepBookLibraryToDictionary()
                connection.updateData(userRef, userData)
            elif choice == "2":
                #Deleting books
                for book in bookLibrary['toRead']:
                    print(book)
                bookToDel = menus.bookDeleteMenu()
                lib.deleteBookFromList(list = BOOK_STATUS[1], bookIndex = bookToDel - 1)
                userData = lib.prepBookLibraryToDictionary()
                connection.updateData(userRef, userData)


        elif choice == "3":
            
            menus.printCurrentlyReadingList()
            for book in bookLibrary['reading']:
                print(book)
            choice = menus.bookListMenu()
            # print(choice)
            if choice == "1":
                #Moving books
                moveTo = menus.bookListMovementMenu(BOOK_STATUS[2])
                for book in lib.getBooksFromList(BOOK_STATUS[2]):
                    print(book)
                bookToMove = int(input("WHICH BOOK WOULD YOU LIKE TO MOVE?: "))
                lib.moveBookToDiffList(moveFrom = BOOK_STATUS[2], moveTo=BOOK_STATUS[moveTo], bookIndex = bookToMove - 1)
                userData = lib.prepBookLibraryToDictionary()
                connection.updateData(userRef, userData)
            elif choice == "2":
                #Deleting books
                for book in bookLibrary['reading']:
                    print(book)
                bookToDel = menus.bookDeleteMenu()
                lib.deleteBookFromList(list = BOOK_STATUS[2], bookIndex = bookToDel - 1)
                userData = lib.prepBookLibraryToDictionary()
                connection.updateData(userRef, userData)
            
        elif choice == "4":
            menus.printReadList()
            for book in bookLibrary['read']:
                print(book)
            choice = menus.bookListMenu()
            if choice == "1":
                moveTo = menus.bookListMovementMenu(BOOK_STATUS[3])
                for book in lib.getBooksFromList(BOOK_STATUS[3]):
                    print(book)
                bookToMove = int(input("WHICH BOOK WOULD YOU LIKE TO MOVE?: "))
                lib.moveBookToDiffList(moveFrom = BOOK_STATUS[3], moveTo=BOOK_STATUS[moveTo], bookIndex = bookToMove - 1)
                userData = lib.prepBookLibraryToDictionary()
                connection.updateData(userRef, userData)
            elif choice == "2":
                #Deleting books
                for book in bookLibrary['read']:
                    print(book)
                bookToDel = menus.bookDeleteMenu()
                lib.deleteBookFromList(list = BOOK_STATUS[3], bookIndex = bookToDel - 1)
                userData = lib.prepBookLibraryToDictionary()
                connection.updateData(userRef, userData)
        elif choice == "5":
            print("THANK YOU! GOODBYE")
            connection.updateData(userRef, userData)
            break
        else:
            print("INVALID INPUT!")


    break
