import requests

'''
Base URL = http://openlibrary.org/search.json

Types of queries:
1. General query (q=the+lord+of+the+rings)
2. Search Title (title=the+lord+of+the+rings)
3. Search Author (author=tolkien)
'''

BASE_URL = "http://openlibrary.org/search.json"

def queryBuilder(type, queryString):
    if type == "query":
        queryType = "?q="
    elif type == "title":
        queryType ="?title="
    else: #type == "author"
        queryType ="?author="
    
    keywordsList = queryString.split(" ")
    query = "+".join(keywordsList)
    
    return BASE_URL + queryType + query

sampleQueries = [
    ["query", "three body problem liu ci xin"],
    ["title", "house of leaves"],
    ["author", "dan brown"]
]

for query in sampleQueries:
    query = queryBuilder(query[0], query[1])
    print(query)
    response = requests.get(query)
    print(response.status_code)



response = requests.get("http://openlibrary.org/search.json?q=the+lord+of+the+rings")

# print(response)
# print(response.status_code)
# print(response.json())