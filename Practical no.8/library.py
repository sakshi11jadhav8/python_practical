

# Python program to make functions for library to issue a book, check if book is present or not & return book

def issue_book(title):
    if title in lib:
        lib[title] -= 1
        print(title, 'issued.')

        if lib[title] == 0:
            del lib[title]

        if title in issued_books:
            issued_books[title] += 1
        else:
            issued_books[title] = 1

    else:
        print(title, "is not available.")


def checkif(title):
    if title in lib:
        print(lib[title], 'copies of', title, 'available')
    else:
        print(title, "is not available.")


def return_book(title):
    if title in lib:
        lib[title] += 1
        print(title, 'returned.')
    else:
        lib[title] = 1
        print("Now available:", title)

    if title in issued_books:
        issued_books[title] -= 1
        if issued_books[title] == 0:
            del issued_books[title]


lib = {
    'Little women': 3,
    'The Alchemist': 2,
    'The Secret': 1,
    'The Lord of the Rings': 3,
    'The Hunger Games': 3,
    'The Book Theif': 4,
    'The Kite Runner': 2,
    'Gone with the Wind': 5,
    '1984': 3
}

issued_books = {}

issue_book('Little women')
checkif('The Alchemist')
issue_book('The Secret')
checkif('The Secret')
return_book('The Secret')
return_book('Little women')
