books = ["The Great Gatsby", "To Kill a Mockingbird", "1984", "Pride and Prejudice", "The Catcher in the Rye", "The Lord of the Rings"]
print(len(books))
print(books[0])
print(books[-1])
books.append("diary of a wimpy kid")
books.remove("1984")
books.sort()
books.reverse()
librarian = {
    "name": "John Doe",
    "section": "Fiction",
    "experience": 10
}
print(librarian["name"])
librarian["experience"] = 6
librarian["email"] = "john.doe@example.com"
librarian.pop("section")
book_ids = [101, 102, 103, 104, 105]
book_names = ["The Great Gatsby", "To Kill a Mockingbird", "1984", "Pride and Prejudice", "The Catcher in the Rye"]
book_dict = dict(zip(book_ids, book_names))
print("Available books:",books)
print("librarian details:", librarian)
print("Book ID dictionary:", book_dict)