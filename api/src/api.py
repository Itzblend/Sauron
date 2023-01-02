# FastAPI
from fastapi import FastAPI
import uvicorn
import json
import logging
import logging.config
from datetime import datetime

from logging.handlers import TimedRotatingFileHandler
import time


def create_timed_rotating_log(path):
    """"""
    logging.config.fileConfig("src/log.ini")
    logger = logging.getLogger("api")
    logger.setLevel(logging.INFO)
    
    handler = TimedRotatingFileHandler(path,
                                       when="s",
                                       interval=30,
                                       backupCount=5)
    logger.addHandler(handler)
    return logger


# Load the logging configuration
logger = create_timed_rotating_log("src/api.log")

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

@app.get("/purchase/{book_id}")
def purchase_book(book_id: int):
    with open("data/books.json", "r") as f:
        books = json.load(f)
    book = [book for book in books if book["id"] == book_id]
    if book:
        purchase_status = process_purchase(book[0])

    if purchase_status:
        logger.info(f'Purchasing book with id {book_id}')
        return {"Success": f"Book with id {book_id} purchased"}
    else:
        logger.error("Purchase failed")
        return {"Error": "Purchase failed"}

def process_purchase(book):
    purchase_log = {
        "id": book["id"],
        "name": book["name"],
        "price(usd)": book["price(usd)"],
        "timestamp": datetime.now().isoformat()
    }
    with open("data/purchases.json", "a") as f:
        f.write(json.dumps(purchase_log))
        f.write("\n")

    purchase_status = validate_purchase(purchase_log)
    return purchase_status

def validate_purchase(purchase_log):
    with open('data/purchases.json', 'r') as f:
        last_purchase = json.loads(f.readlines()[-1])
    if purchase_log == last_purchase:
        return True
    else:
        return False




# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8888, log_config="src/log.ini")