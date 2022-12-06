import requests
import sys
sys.path.append('C:/Users/madra/OneDrive - Nanyang Technological University/McMasters/Software Arch/McMaster4SA3/controller')
import Book as Book

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
        print("DEBUG: CREATING OPENLIBAPI")

    def queryBuilder(self, type, queryString):
        if type == "query":
            queryType = "?q="
        elif type == "title":
            queryType ="?title="
        else: #type == "author"
            queryType ="?author="
        
        keywordsList = queryString.split(" ")
        query = "+".join(keywordsList)
        
        return self.BASE_URL + queryType + query

    def sendQuery(self, query):
        response = requests.get(query)
        return response

    def parseResponse(self, response):
        # print(type(response.text))
        reponseCode = response.status_code
        # print(type(response.json()))
        apiResponse = response.json()
        # print(apiResponse["status_code"])
        # print(apiResponse)
        bookLibrary = []
        books = apiResponse["docs"]
        print("Showing Top 5 Responses:")
        for i in range(5):
            
            # print("====================")
            # print(f"RESULT {i+1}:")
            book = books[i]
            result = Book.Book(book["title"], book["author_name"][0], book["first_publish_year"])
            # print(result)
            # print("====================")
            bookLibrary.append(result)
        return bookLibrary
        
        # responseCode = response.status_code
        # responseBody
#     sampleQueries = [
#         ["query", "three body problem liu ci xin"],
#         ["title", "house of leaves"],
#         ["author", "dan brown"]
#     ]

# for query in sampleQueries:
#     query = queryBuilder(query[0], query[1])
#     print(query)
    
    # print(response.status_code)


# api = OpenLibAPI()
# response = api.sendQuery("http://openlibrary.org/search.json?q=the+lord+of+the+rings")
# api.parseResponse(response)
# # response = requests.get()

# print(response)
# print(response.status_code)
# print(response.json())