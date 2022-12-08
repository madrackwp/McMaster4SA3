import Book as Book

class Library():
    def __init__(self):
        self.bookLibrary = {
            'toRead':[],
            'reading':[],
            'read':[]
        }

    def getBooksFromList(self, bookStatus):
        return self.bookLibrary[bookStatus]
    
    def prepBookLibraryToDictionary(self):
        # print(bookLibrary)

        data = {'books':{},"password": 'password'}
        for bookStatus in self.bookLibrary:
            for book in self.bookLibrary[bookStatus]:
                # print(book.getBookTitle())
                # print(book.getBookAuthor())
                # print(book.getPublishedDate())
                # print(book.getBookStatus())
                data['books'][book.getBookTitle()] = {
                    "author":book.getBookAuthor(),
                    "publishedDate": book.getPublishedDate(),
                    "status": book.getBookStatus()
                    }
        return data
        

    def rawDataToLibrary(self, userData):
        bookData = userData.get("books")
        if bookData is not None:

        # bookData = userData["books"]
            for book in bookData:
                status = bookData[book]["status"]
                bookTitle = book
                author = bookData[book]["author"]
                status = bookData[book]["status"]
                publishedDate = bookData[book]["publishedDate"]
                newBook = Book.Book(bookTitle, author, publishedDate, status)
                if status == "read":
                    self.bookLibrary['read'].append(newBook)
                elif status == "toRead":
                    self.bookLibrary['toRead'].append(newBook)
                else:
                    self.bookLibrary['reading'].append(newBook)
        return self.bookLibrary
    
    def moveBookToDiffList(self, moveFrom, moveTo, bookIndex):
        bookToMove = self.bookLibrary[moveFrom][bookIndex]
        self.bookLibrary[moveFrom].remove(bookToMove)
        bookToMove.changeBookStatus(moveTo)
        self.bookLibrary[moveTo].append(bookToMove)

    def deleteBookFromList(self, list, bookIndex):
        bookToDel = self.bookLibrary[list][bookIndex]
        self.bookLibrary[list].remove(bookToDel)
        
