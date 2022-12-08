from abc import ABC, abstractmethod

BASE_URL = "http://openlibrary.org/search.json"

class QueryFactory(ABC):
    def __init__(self):
        self.query = None

    @abstractmethod
    def getQuery(self):
        pass

    @abstractmethod
    def generateQuery(self, type, queryString):
        pass

class generalQueryFactory(QueryFactory):
    def __init__(self):
        self.query = None

    def getQuery(self):
        return self.query

    def generateQuery(self, queryString):
        keywordsList = queryString.split(" ")
        query = "+".join(keywordsList)
        self.query = BASE_URL + "?q=" + query

class authorQueryFactory(QueryFactory):
    def __init__(self):
        self.query = None

    def getQuery(self):
        return self.query

    def generateQuery(self, queryString):
        keywordsList = queryString.split(" ")
        query = "+".join(keywordsList)
        self.query = BASE_URL + "?author=" + query

class titleQueryFactory(QueryFactory):
    def __init__(self):
        self.query = None

    def getQuery(self):
        return self.query

    def generateQuery(self, queryString):
        keywordsList = queryString.split(" ")
        query = "+".join(keywordsList)
        self.query = BASE_URL + "?title=" + query

# queryFactory = titleQueryFactory()
# queryFactory.generateQuery("lord of the rings")
# print(queryFactory.getQuery())
    