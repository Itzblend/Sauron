"""
Sole purpose of this bot is to in random intervals call different endpoints of the API
to simulate real user activity.
"""

import time
import random
import requests
import os
import logging
import logging.config

# Load the logging configuration
logging.config.fileConfig("src/log.ini")
logger = logging.getLogger("bot")


HOSTNAME = os.environ.get('HOSTNAME')

HOST = 'api:8888' if HOSTNAME == 'bot' else 'localhost:8888'

def get_books():
    logger.info(f'Getting books from {HOST}')
    r = requests.get(f'http://{HOST}/books')
    return r.json()

def purchase_book(book_id):
    logger.info(f'Purchasing book with id {book_id} from {HOST}')
    r = requests.get(f'http://{HOST}/purchase/{book_id}')

if __name__ == '__main__':
    while True:
        books = get_books()
        random_book_id = random.choice(books)["id"]
        print(purchase_book(random_book_id))
        time.sleep(random.uniform(0.2, 3))

