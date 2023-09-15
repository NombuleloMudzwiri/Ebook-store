
# eBookstore Database Management System

This GitHub repository contains a Python eBookstore Database Management System. The system allows users to create, manage, and search for books in an SQLite database. 
This README will guide you through the usage of the program and provide insights into its features.

## Getting Started

To use the eBookstore Database Management System, follow these steps:

1. **Clone the Repository**: Start by cloning this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/ebookstore-database.git
   ```

   Replace `your-username` with your actual GitHub username.

2. **Navigate to the Project Directory**: Change your working directory to the project folder:

   ```bash
   cd ebookstore-database
   ```

3. **Run the Program**: Execute the `ebookstore.py` file to start the eBookstore Database Management System:

   ```bash
   python ebookstore.py
   ```

   The program will launch and present a menu for you to interact with.

## Features and How the System Works

The eBookstore Database Management System offers the following features:

### 1. Create Initial Database

- The program creates an SQLite database called `ebookstore.db` if it doesn't exist.
- It also creates a `books` table with columns for book ID, title, author, and quantity.
- Initial book data is inserted into the table.

### 2. Enter a Book

- Users can add a new book to the database by providing the book title, author name, and quantity.
- The new book is added to the database, and the user is notified of the successful addition.

### 3. Update a Book

- Users can update the quantity of a book in the database by specifying the book's ID and the new quantity.
- The program updates the book's quantity, and the user receives a confirmation message.

### 4. Delete a Book

- Users can delete a book from the database by specifying the book's ID.
- The program removes the book from the database, and the user receives a confirmation message.

### 5. Search for Books

- Users can search for books in the database by entering a search term (book title or author).
- The program performs a search and displays matching books along with their details.

### 6. Exit

- Selecting this option exits the program.


Thank you for using the eBookstore Database Management System! If you have any questions or encounter any issues, please don't hesitate to open an issue in the GitHub repository.
```

You can replace `your-username` and `feature-name` with your actual GitHub username and the name of your feature branch when contributing. This README template provides an overview of the project's functionality and instructions on how to use and contribute to it.
