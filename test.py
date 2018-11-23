import unittest
from books import Book, Library

class BookTest(unittest.TestCase):
    def setUp(self):
        self.book = Book(1, 'Title One', 'Author One', 50, 10)


    def test_isInstance_Book(self):
        self.assertIsInstance(self.book, Book, msg = 'Object should be an instance of the class Book')


    def test_object_type(self):
        self.assertTrue((type(self.book) is Book), msg= 'Object should be of type Book')

    
    def test_default_price(self):
        bookX = Book(10, 'Title X', 'Author X')
        self.assertEqual(0, bookX.price, msg = 'Default price should be 0')


    def test_default_number_of_copies(self):
        bookX = Book(10, 'Title X', 'Author X')
        self.assertEqual(0, bookX.numberOfCopies, msg = 'Default number of copies should be 0')


class LibraryTest(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book(1, 'Title One', 'Author One', 50, 10)
        self.book2 = Book(2, 'Title Two', 'Author Two', 500, 5)
        self.book3 = Book(3, 'Title Three', 'Author Three', 5000, 1)
        
        self.library.insertNewBook(self.book1)
        self.library.insertNewBook(self.book2)
        self.library.insertNewBook(self.book3)
        
    
    def test_library_instance(self):
        self.assertIsInstance(self.library, Library, msg='library should be an instance of Library')

    
    def test_insert_new_book(self):
        self.assertListEqual([self.book1, self.book2, self.book3], self.library.mapOfBooks,
                                msg = 'All the books should be in mapOfBooks in the correct order')

    
    def test_duplicate_entry(self):
        self.assertRaises(Exception, self.library.insertNewBook, self.book1)


    def test_retrieve_book(self):
        self.library.retrieveBook(1)
        self.assertEqual(9, self.book1.numberOfCopies, msg = 'Number of copies should reduce by one')


    def test_retrieve_spent_book(self):
        self.library.retrieveBook(3)
        self.assertRaises(ValueError, self.library.retrieveBook, 3)


    def test_retrieve_nonexistent_book(self):
        self.assertRaises(IndexError, self.library.retrieveBook, 5)


    def test_insert_book(self):
        self.library.insertBook(1)
        self.assertEqual(11, self.book1.numberOfCopies, msg='Number of copies should increase by one')


    def test_insert_nonexistent_book(self):
        self.assertRaises(IndexError, self.library.insertBook, 5)

    
    def test_remove_book(self):
        self.library.removeBook(1)
        self.assertListEqual([self.book2, self.book3], self.library.mapOfBooks,
                                msg='Book one should be removed from the library')


    def test_remove_nonexistent_book(self):
        self.assertRaises(IndexError, self.library.removeBook, 5)

    
    def test_find_book(self):
        self.assertListEqual([{'title': 'Title Two', 'book number': 2}], self.library.findBook('Title Two'))
    


if __name__ == '__main__':
    unittest.main(exit = False)