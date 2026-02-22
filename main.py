# Library Book Management System
# Laboratory Activity - OOP Practice

class Book:
    def __init__(self):
        # All attributes will be set using input() later
        self.title = ""
        self.author = ""
        self.year = 0
        self.available = True  # True = available, False = borrowed

    def set_book_info(self):
        # Set book details from user input
        print("\n--- Enter Book Details ---")
        self.title = input("Enter book title: ").strip()
        
        self.author = input("Enter author name: ").strip()
        
        while True:
            try:
                year_input = input("Enter publication year: ").strip()
                self.year = int(year_input)
                if self.year < 1000 or self.year > 2100:
                    print("Please enter a reasonable year (1000-2100).")
                    continue
                break
            except ValueError:
                print("Invalid year! Please enter a number.")

        print("\nBook information saved successfully!")

    def borrow_book(self):
        # Mark the book as borrowed if available
        if self.available:
            self.available = False
            print(f"\nSuccess! You have borrowed '{self.title}' by {self.author}.")
        else:
            print(f"\nSorry, '{self.title}' is currently NOT available (already borrowed).")

    def return_book(self):
        # Mark the book as available again if it was borrowed
        if not self.available:
            self.available = True
            print(f"\nThank you! '{self.title}' has been returned.")
        else:
            print(f"\n'{self.title}' was not borrowed. Nothing to return.")

    def display_info(self):
        # Display all book information and status
        print("\n--- Book Information ---")
        print(f"Title     : {self.title}")
        print(f"Author    : {self.author}")
        print(f"Year      : {self.year}")
        status = "Available" if self.available else "Borrowed"
        print(f"Status    : {status}")
        print("-" * 30)

    def is_available(self):
        # Return True if book is available, False if borrowed
        return self.available


def main():
    print("=====================================")
    print("   Library Book Management System    ")
    print("=====================================\n")

    book = Book()

    book.set_book_info()

    while True:
        print("\nWhat would you like to do?")
        print("1. Display book information")
        print("2. Borrow the book")
        print("3. Return the book")
        print("4. Exit program")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            book.display_info()

        elif choice == "2":
            book.borrow_book()

        elif choice == "3":
            book.return_book()

        elif choice == "4":
            print("\nThank you for using the Library Book Management System!")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice! Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram closed. Goodbye!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Program will now exit.")