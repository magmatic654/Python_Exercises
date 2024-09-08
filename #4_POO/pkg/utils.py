def library_book(book):
    return{
        'title': book.title,
        'author': book.author,
        'available': book.available
        }

def user_book(dict_book):
    return {
        'title': dict_book['title'],
        'author': dict_book['author'],
        }
    