""" Program to create and manage a list of books that the user wishes to read, and books that the user has read. """

from bookstore import Book, BookStore
from menu import Menu
import ui

store = BookStore()

def main():

    menu = create_menu()

    while True:
        choice = ui.display_menu_get_choice(menu)
        action = menu.get_action(choice)
        action()
        if choice == 'Q':
            break


def create_menu():
    menu = Menu()
    menu.add_option('1', 'Add Book', add_book)
    menu.add_option('2', 'Search For Book', search_book)
    menu.add_option('3', 'Show Unread Books', show_unread_books)
    menu.add_option('4', 'Show Read Books', show_read_books)
    menu.add_option('5', 'Show All Books', show_all_books)
    menu.add_option('6', 'Change Book Read Status', change_read)
    ##added deleting the book here
    menu.add_option('7', 'Delete a book', delete_book)
    menu.add_option('Q', 'Quit', quit_program)

    return menu


def add_book():

     new_book = ui.get_book_info()
     all_books = store.get_all_books()
     if new_book in all_books:
        ui.message('The book already exist')
     else:
      store.add_book(new_book)
      new_book = ui.get_book_info()
      new_book.save()
    

def show_read_books():
    read_books = store.get_books_by_read_value(True)
    ui.show_books(read_books)


def show_unread_books():
    unread_books = store.get_books_by_read_value(False)
    ui.show_books(unread_books)


def show_all_books():
    books = store.get_all_books()
    ui.show_books(books)


def search_book():
    search_term = ui.ask_question('Enter search term, will match partial authors or titles.')
    matches = store.book_search(search_term)
    ui.show_books(matches)


##added try catch block if error occurs when trying to change read status of book


##Added Delete book function here
def delete_book():
    book_id = ui.get_book_id()
    book = store.get_book_by_id(book_id)
    store.delete_book(book)
    ui.message('Book Deleted')


def change_read():
     try:
        book_id = ui.get_book_id()
        book = store.get_book_by_id(book_id)  
        new_read = ui.get_read_value()     
        book.read = new_read 
        book.save()
        print('It has been changed !')
     except:
        ui.message('Book not found')

    

def quit_program():
    quit_program = input("enter q or Q to quit")
    if quit_program == 'q' or 'Q':
         break
    ui.message('Thanks and bye!')


if __name__ == '__main__':
    main()
