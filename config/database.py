import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return mysql.connector.connect(
        user="root",
        password=os.getenv("DB_PASSWORD"),
        host="localhost",
        database="book_store"
    )