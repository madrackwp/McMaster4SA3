import requests
import sys
sys.path.append('C:/Users/madra/OneDrive - Nanyang Technological University/McMasters/Software Arch/McMaster4SA3/controller')
import Book as Book
import QueryFactory as QueryFactory

'''
Base URL = http://openlibrary.org/search.json

Types of queries:
1. General query (q=the+lord+of+the+rings)
2. Search Title (title=the+lord+of+the+rings)
3. Search Author (author=tolkien)
'''


class OpenLibAPI():
    def __init__(self):
        self.BASE_URL = "http://openlibrary.org/search.json"

    def sendQuery(self, query):
        response = requests.get(query)
        return response

    def parseResponse(self, response):
        reponseCode = response.status_code
        apiResponse = response.json()
        bookLibrary = []
        
        books = apiResponse["docs"]
        print("SHOWING TOP 5 RESPONSES:")

        for i in range(min(5,len(books))):
            book = books[i]
            result = Book.Book(book["title"], book["author_name"][0], book["first_publish_year"])
            bookLibrary.append(result)
        return bookLibrary
        
