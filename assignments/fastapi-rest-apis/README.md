# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API with FastAPI that validates data and performs create, read, update, and delete (CRUD) operations for a collection of books.

## 📝 Tasks

### 🛠️	Create the API and Book Model

#### Description
Set up a FastAPI application and define the data models used to represent books and book updates.

#### Requirements
Completed program should:

- Create a `FastAPI` application with a descriptive title
- Define a `Book` model with integer `id`, string `title`, string `author`, and integer `year` fields
- Define a `BookUpdate` model whose `title`, `author`, and `year` fields are optional
- Provide a `GET /` endpoint that returns a welcome message


### 🛠️	Add Create and Read Endpoints

#### Description
Use an in-memory list to store books, then add endpoints that create books and retrieve the collection.

#### Requirements
Completed program should:

- Provide a `POST /books` endpoint that accepts and stores a valid `Book`
- Return HTTP status `201 Created` after successfully creating a book
- Reject a duplicate book ID with HTTP status `409 Conflict`
- Provide a `GET /books` endpoint that returns all books
- Provide a `GET /books/{book_id}` endpoint that returns one matching book or HTTP status `404 Not Found`


### 🛠️	Complete the CRUD API

#### Description
Add endpoints that update and delete an existing book while returning useful errors for unknown IDs.

#### Requirements
Completed program should:

- Provide a `PUT /books/{book_id}` endpoint that changes only the fields supplied in a `BookUpdate`
- Keep the existing book ID unchanged during an update
- Provide a `DELETE /books/{book_id}` endpoint that removes a book and returns HTTP status `204 No Content`
- Return HTTP status `404 Not Found` when updating or deleting an unknown book ID
- Make all endpoints testable from the interactive documentation at `/docs`