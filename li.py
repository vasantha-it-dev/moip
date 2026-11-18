# library.py - Library Management System

books = [
    {"name": "Python Crash Course", "author": "Eric Matthes", "price": 450},
    {"name": "Clean Code", "author": "Robert C. Martin", "price": 520},
    {"name": "The Pragmatic Programmer", "author": "Andrew Hunt", "price": 600},
    {"name": "Introduction to Algorithms", "author": "Thomas H. Cormen", "price": 850},
]


def display_books():
    print("=" * 60)
    print(f"{'Book Name':<30}{'Author':<20}{'Price':>8}")
    print("=" * 60)
    for book in books:
        print(f"{book['name']:<30}{book['author']:<20}{'Rs.' + str(book['price']):>8}")
    print("=" * 60)


if __name__ == "__main__":
    print("\nWelcome to the Library Management System\n")
    display_books()
    
