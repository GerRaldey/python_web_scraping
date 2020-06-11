from app import books

USER_CHOICE = '''Please choose one option provided below...
   press b - to look for top rating books
   press c - to look for cheapest books
   press n - for the next book available in the catalogue
   press q - exit the program
    >>>'''

books_list = (x for x in books)

def sort_rating():
    best_books = sorted(books, key=lambda x: x.rating, reverse=True)[:10]
    for book in best_books:
        print(book)

def cheapest_book():
    cheap_books = sorted(books, key=lambda x: x.price)[:10]
    for book in cheap_books:
        print(book)

def next_book():
    print(next(books_list))

user_choices = {
    'b': sort_rating,
    'c': cheapest_book,
    'n': next_book
}

def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ('b', 'c', 'n'):
            user_choices[user_input]() #calling a function from the dictionary
        else:
            print('Your option is not valid')

        user_input = input(USER_CHOICE)

menu()