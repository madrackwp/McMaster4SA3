class Book():
    def __init__(self, title, author, publishedDate, status=None):
        self._title = title
        self._author = author
        self._publishedDate = publishedDate
        self._status = status

    def __str__(self):
        toReturn = f"Book Title: {self._title}\nAuthor: {self._author}\nWritten in: {self._publishedDate}\n=========================="
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

    def changeBookStatus(self, newStatus):
        self._status = newStatus