class Book:
    def __init__(self, bookNumber, title, author, price = 0, numberOfCopies = 0):  # initialise book
        self.bookNumber = bookNumber
        self.title = title
        self.author = author
        self.price = price
        self.numberOfCopies = numberOfCopies


    def setPrice(self, price):
        self.price = price


    def setNumberOfCopies(self, numberOfCopies):
        self.numberOfCopies = numberOfCopies


class Library:
    def __init__(self): # initialise library
        self.bookNumbers = []
        self.mapOfBooks = []


    def findBook(self, title):
        result = []
        for book in self.mapOfBooks:
            if book.title == title:
                result.append({'title': book.title, 'book number': book.bookNumber})
        return result


    def insertNewBook(self, book):  # insert a new book entry into the library
        if book.bookNumber in self.bookNumbers:
            raise Exception('Duplicate book numbers!')
        else:
            self.mapOfBooks.append(book)
            self.bookNumbers.append(book.bookNumber)
        

    def retrieveBook(self, bookNumber):     # remove one copy of a book from the library
        if bookNumber in self.bookNumbers:
            position = self.bookNumbers.index(bookNumber)
            book = self.mapOfBooks[position]
            if book.numberOfCopies > 0:
                self.mapOfBooks[position].numberOfCopies -= 1
                return book
            else:
                 raise ValueError('All copies of {} have been lent out.'.format(book.title))
        else:
            raise IndexError('Book does not exist!')


    def insertBook(self, bookNumber):
        if bookNumber in self.bookNumbers:
            position = self.bookNumbers.index(bookNumber)
            self.mapOfBooks[position].numberOfCopies += 1
        else:
            raise IndexError('Book does not exist!')


    def removeBook(self, bookNumber):
        if bookNumber in self.bookNumbers:
            position = self.bookNumbers.index(bookNumber)
            del self.mapOfBooks[position]
            del self.bookNumbers[position]
        else:
            raise IndexError('Book does not exist!')

    def listBooks(self):
        listOfBooks = []
        for book in self.mapOfBooks:
            listOfBooks.append({'Book number': book.bookNumber, 'title': book.title})
        return listOfBooks


##################################################################################################
#library = Library()
#book1 = Book(1, 'The Wizard of Oz', 'Pink Panther', 20, 10)
#library.insertNewBook(book1)
#print(library.listBooks())
#print(library.findBook('The Wizard of Oz'))
#for i in range(10):
#    library.retrieveBook(1)
#book2 = library.retrieveBook(1)
#print(book2.numberOfCopies)
#library.returnBook(1)
#print(book2.numberOfCopies)
#library.removeBook(1)
#print(library.listBooks())