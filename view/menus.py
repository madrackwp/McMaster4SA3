import os

BOOK_STATUS = {
    1: "toRead",
    2: "reading",
    3: "read"
}

def printReadList():
    os.system('cls')
    print("================")
    print("READ BOOKS")
    print("================")

def printToReadList():
    os.system('cls')
    print("================")
    print("TO READ BOOKS")
    print("================")

def printCurrentlyReadingList():
    os.system('cls')
    print("================")
    print("CURRENTLY READING BOOKS")
    print("================")

def printLoginMenu():
    os.system('cls')
    print("=============================")
    print("WELCOME TO READIEBOOKS")
    print("WHAT IS YOUR LOGIN ID")
    print("=============================")

def printCreateIDMenu():
    print("Login does not exist, please create a new account:")
    print("Please input a new userID: ")
    newUserID = input()
    return newUserID

def printMainMenu():
    os.system('cls')
    print("===============================================")
    print("1. SEARCH FOR BOOKS")
    print("2. LOOK AT MY 'TO READ' LIST")
    print("3. LOOK AT MY 'CURRENTLY READING' LIST")
    print("4. LOOK AT MY 'READ' LIST")
    print("5. QUIT")
    print("===============================================")

def bookListMenu():
    # os.system('cls')
    print("1. MOVE BOOKS")
    print("2. DELETE BOOK")
    print("3. BACK TO MAIN MENU")
    userInput = input("WHAT WOULD YOU LIKE TO DO NOW?")
    
    while userInput != "1" and userInput != "2" and userInput != "3":
        print("INVALID INPUT!")
        userInput = input("WHAT WOULD YOU LIKE TO DO NOW?")
    return userInput


def bookListMovementMenu(currentList):
    print("WHICH LIST WOULD YOU LIKE TO MOVE IT TO?")
    for key, value in BOOK_STATUS.items():
        print(f"{key}: {value}")
    choice = input()
    return int(choice)

def bookDeleteMenu():
    choice = input("WHICH BOOK WOULD YOU LIKE TO DELETE?")
    return int(choice)

def queryMenu():
    print("SEARCH BY: \n1. QUERY\n2. TITLE\n3. AUTHOR")
    rawQueryType = input("WHAT WOULD YOU LIKE TO SEARCH BY?(ENTER 1-3): ")
    while rawQueryType != "1" and rawQueryType != "2" and rawQueryType != "3":
        print("INVALID INPUT")
        rawQueryType = input("WHAT WOULD YOU LIKE TO SEARCH BY?(ENTER 1-3): ")
    query = input("ENTER YOUR SEARCH: ")
    if rawQueryType == "1":
        queryType = "query"
    elif rawQueryType == "2":
        queryType = "title"
    else:
        queryType = "author"
    return queryType, query
    