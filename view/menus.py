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
    print("What is your Login ID")
    print("=============================")

def printCreateIDMenu():
    print("Login does not exist, please create a new account:")
    print("Please input a new userID: ")
    newUserID = input()
    return newUserID

def printMainMenu():
    os.system('cls')
    print("===============================================")
    print("1. Search for books")
    print("2. Look at my 'To Read' list")
    print("3. Look at my 'Currently Reading' List")
    print("4. Look at my 'Read' list")
    print("5. Quit")
    print("===============================================")

def bookListMenu():
    # os.system('cls')
    print("1. Move books")
    print("2. Delete book")
    print("3. Back to Main Menu")
    userInput = input("What would you like to do now?")
    
    while userInput != "1" and userInput != "2" and userInput != "3":
        print("Invalid input!")
        userInput = input("What would you like to do now?")
    return userInput


def bookListMovementMenu(currentList):
    print("Which List would you like to move it to?")
    for key, value in BOOK_STATUS.items():
        print(f"{key}: {value}")
    choice = input()
    return int(choice)

def bookDeleteMenu():
    choice = input("Which book would you like to delete?")
    return int(choice)
    