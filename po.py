# library.py - Library Management System (with Book Issue feature)

books = [
    {"name": "Python Crash Course", "author": "Eric Matthes", "price": 450, "issued": False},
    {"name": "Clean Code", "author": "Robert C. Martin", "price": 520, "issued": False},
    {"name": "The Pragmatic Programmer", "author": "Andrew Hunt", "price": 600, "issued": False},
    {"name": "Introduction to Algorithms", "author": "Thomas H. Cormen", "price": 850, "issued": False},
]


def display_books():
    print("=" * 70)
    print(f"{'No.':<5}{'Book Name':<30}{'Author':<20}{'Price':<8}{'Status'}")
    print("=" * 70)
    for i, book in enumerate(books, start=1):
        status = "Issued" if book["issued"] else "Available"
        print(f"{i:<5}{book['name']:<30}{book['author']:<20}{'Rs.' + str(book['price']):<8}{status}")
    print("=" * 70)


def issue_book():
    display_books()
    try:
        choice = int(input("Enter book number to issue: "))
        book = books[choice - 1]
    except (ValueError, IndexError):
        print("Invalid book number.")
        return

    if book["issued"]:
        print(f"Sorry, '{book['name']}' is already issued.")
    else:
        book["issued"] = True
        print(f"'{book['name']}' has been issued successfully.")


def main():
    while True:
        print("\n--- Library Management System ---")
        print("1. Display Books")
        print("2. Issue Book")
        print("3. Exit")
        option = input("Choose an option: ")

        if option == "1":
            display_books()
        elif option == "2":
            issue_book()
        elif option == "3":
            print("Thank you for using the library!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
