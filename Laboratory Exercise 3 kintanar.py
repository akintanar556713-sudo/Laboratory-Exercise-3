class Book:
    def borrow_book(self):
        self.available = False
        print("Success: Book is now borrowed.")
    def return_book(self):
        self.available = True
        print("Success: Book is now available.")
    def display_info(self):
        status = "Available" if self.available else "Unavailable"
        print(f"\n{self.title} by {self.author} ({self.year})")
        print(f"Current Status: {status}")

    def __init__(self):
        self.title = input("Enter Title: ")
        self.author = input("Enter Author: ")
        self.year = input("Enter Year: ")
        self.available = True
b = Book()
while True:
    print("\n1: Borrow | 2: Return | 3: Info | 4: Exit")
    choice = input("Select action: ")
    if choice == '1': b.borrow_book()
    elif choice == '2': b.return_book()
    elif choice == '3': b.display_info()
    elif choice == '4': break
    else: print("Invalid choice.")