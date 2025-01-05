import mysql.connector
from dotenv import load_dotenv
import os


# Load the environment variables
load_dotenv()

password = os.getenv("DB_PASSWORD")

# Establish a connection 
conn  = mysql.connector.connect(user="root", password=password, host="localhost", database="book_store")

# Create a cursor 
cursor = conn.cursor()


# Execute a query
cursor.execute("SHOW TABLES;")

tables = cursor.fetchall()
print("Tables in the database:")
for table in tables:
    print(table[0])



# # Fetch all the rows
# all_rows = cursor.fetchall()
# print("all_rows: ", all_rows)

# #Fetch three rows
# three_rows = cursor.fetchmany(3)
# print("three_rows: ", three_rows)

# #Fetch one row at a time using fetchone()
# row = cursor.fetchone()
# while row:
#     print("row: ", row)
#     row = cursor.fetchone() 

# for row in cursor:
#     print("row in cursor: ", row)


# Close the cursor
cursor.close()
conn.close()


