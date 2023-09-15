import sqlite3

# Function to create the initial database and table
def create_database():
    try:
        conn = sqlite3.connect('ebookstore.db')
        c = conn.cursor()

        # Create the books table if it doesn't exist
        c.execute('''CREATE TABLE IF NOT EXISTS books
                    (id INTEGER PRIMARY KEY,
                     Title TEXT,
                     Author TEXT,
                     Qty INTEGER)''')

        # Insert initial data into the table
        books_data = [
            (3001, "A Tale of Two Cities", "Charles Dickens", 30),
            (3002, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 40),
            (3003, "The Lion, the Witch and the Wardrobe", "C. S. Lewis", 25),
            (3004, "The Lord of the Rings", "J.R.R Tolkien", 37),
            (3005, "Alice in Wonderland", "Lewis Carroll", 12)
        ]
        for book in books_data:
            c.execute("INSERT OR IGNORE INTO books (id, Title, Author, Qty) VALUES (?, ?, ?, ?)", book)

        conn.commit()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print("Error creating database:", str(e))
    finally:
        conn.close()

# Function to add a new book to the database
def add_book():
    try:
        conn = sqlite3.connect('ebookstore.db')
        c = conn.cursor()

        title = input("Enter the book title: ")
        author = input("Enter the author name: ")
        quantity = int(input("Enter the quantity: "))

        c.execute("INSERT INTO books (Title, Author, Qty) VALUES (?, ?, ?)", (title, author, quantity))

        conn.commit()
        print("Book added successfully.")
    except sqlite3.Error as e:
        print("Error adding book:", str(e))
    finally:
        conn.close()

# Function to update book information
def update_book():
    try:
        conn = sqlite3.connect('ebookstore.db')
        c = conn.cursor()

        book_id = int(input("Enter the book ID to update: "))
        new_quantity = int(input("Enter the new quantity: "))

        c.execute("UPDATE books SET Qty = ? WHERE id = ?", (new_quantity, book_id))

        if c.rowcount > 0:
            print("Book information updated successfully.")
        else:
            print("Book not found.")

        conn.commit()
    except sqlite3.Error as e:
        print("Error updating book:", str(e))
    finally:
        conn.close()

# Function to delete a book from the database
def delete_book():
    try:
        conn = sqlite3.connect('ebookstore.db')
        c = conn.cursor()

        book_id = int(input("Enter the book ID to delete: "))

        c.execute("DELETE FROM books WHERE id = ?", (book_id,))

        if c.rowcount > 0:
            print("Book deleted successfully.")
        else:
            print("Book not found.")

        conn.commit()
    except sqlite3.Error as e:
        print("Error deleting book:", str(e))
    finally:
        conn.close()

# Function to search for a book in the database
def search_books():
    try:
        conn = sqlite3.connect('ebookstore.db')
        c = conn.cursor()

        search_term = input("Enter the book title or author: ")

        c.execute("SELECT * FROM books WHERE Title LIKE ? OR Author LIKE ?", ('%' + search_term + '%', '%' + search_term + '%'))
        books = c.fetchall()

        if len(books) > 0:
            print("Search results:")
            for book in books:
                print("ID:", book[0])
                print("Title:", book[1])
                print("Author:", book[2])
                print("Quantity:", book[3])
                print()
        else:
            print("No books found.")
    except sqlite3.Error as e:
        print("Error searching for books:", str(e))
    finally:
        conn.close()

# Main program loop
def main():
    create_database()

    while True:
        print("Menu:")
        print("1. Enter a book")
        print("2. Update a book")
        print("3. Delete a book")
        print("4. Search for a books")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            update_book()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            search_books()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

        print()

if __name__ == '__main__':
    main()

# I added try, except and finally clauses to catch any possible errors.