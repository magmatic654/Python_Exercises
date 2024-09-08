import pkg
import pkg.utils

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.books = []

    def borrow_book(self, library, book):
        for item in library.books:
            if item['title'] == book.title and item['available'] == True:
                self.books.append(pkg.utils.user_book(item))
                item['available'] = False
                return 'Solicitud de prestamo aprobada'
        return f'{self.name}, el libro no está disponible'
    
    def return_book(self, library, book):
        for item in self.books:
            if item['title'] == book.title:
                self.books.remove(item)
                for i in library.books:
                    if i['title'] == item['title']:
                        i['available'] = True
                return 'Libro devuelto exitosamente!'
        return 'No se ha encontrado el libro'
    
class Library:
    def __init__(self):
        self._books = []

    @property
    def books(self):
        return self._books

    @books.setter
    def books(self, new_books):
        self._books = new_books

    def add_book(self, book):
        self._books.append(pkg.utils.library_book(book))

    def lend_book(self, user, book):
        for item in self.books:
            if item['title'] == book.title and item['available'] == True:
                user.books.append(pkg.utils.user_book(item))
                item['available'] = False
                return 'Solicitud de prestamo aprobada'
        return f'No fue posible prestar el libro a {user._name}'
    
    def show_books(self):
        return self._books
    
if __name__ == '__main__':
    book1 = Book("El Quijote", "Cervantes")
    book2 = Book("Cien años de soledad", "Gabriel García Márquez")
    book3 = Book("Moby Dick", "Herman Melville")
    book4 = Book("Orgullo y prejuicio", "Jane Austen")
    book5 = Book("1984", "George Orwell")
    book6 = Book("Don Juan Tenorio", "José Zorrilla")
    book7 = Book("La Odisea", "Homero")
    book8 = Book("El Gran Gatsby", "F. Scott Fitzgerald")
    book9 = Book("Crimen y castigo", "Fiódor Dostoyevski")
    book10 = Book("La metamorfosis", "Franz Kafka")

    user1 = User("Juan", '001')
    user2 = User("Pedro", '002')
    library = Library()

    library.add_book(book1)
    library.add_book(book2)
    # library.add_book(book3)
    # library.add_book(book4)
    # library.add_book(book5)
    # library.add_book(book6)
    # library.add_book(book7)
    # library.add_book(book8)
    # library.add_book(book9)
    # library.add_book(book10)

    # print(user1.borrow_book(library, book1))
    # print(user2.borrow_book(library, book2))

    # print(f'{user1.name} =>',user1.books)
    # print(f'{user2.name} =>',user2.books)

    print(library.lend_book(user1, book1))
    print(library.lend_book(user2, book2))

    print(f'{user1.name} =>',user1.books)
    print(f'{user2.name} =>',user2.books)

    print('Library =>',library.show_books())

    print(user1.return_book(library, book1))
    print(user2.return_book(library, book2))
    print('Library =>',library.show_books())
    # print(library.books)