# FastAPI
from fastapi import FastAPI
import uvicorn
import json
import logging
import logging.config

# Load the logging configuration
logging.config.fileConfig("src/log.ini")
logger = logging.getLogger("api")

# Create the app
app = FastAPI()

# Create a route
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/books")
def list_books():
    with open("data/books.json", "r") as f:
        books = json.load(f)
    logger.info(f'Returning {len(books)} books')
    return books

@app.get("/books/{book_id}")
def get_book(book_id: int):
    with open("data/books.json", "r") as f:
        books = json.load(f)
    book = [book for book in books if book["id"] == book_id]
    if book:
        logger.info(f'Returning book with id {book_id}')
        return book[0]
    else:
        logger.error(f'Book with id {book_id} not found')
        return {"Error": f"Book with id {book_id} not found"}

# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8888, log_config="src/log.ini")