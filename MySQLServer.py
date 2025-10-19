#!/usr/bin/python3
"""
A Python script that connects to a MySQL server
and creates a database named 'alx_book_store'.
"""

import mysql.connector

try:
    # Connect to MySQL Server
    connection = mysql.connector.connect(
        host='localhost',        # or '127.0.0.1'
        user='root',             # replace with your MySQL username
        password='your_password' # replace with your MySQL password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        # Create database if not exists
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # Close the connection properly
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
