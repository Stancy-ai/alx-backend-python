#!/usr/bin/python3
import os
import mysql.connector


def stream_users():
    """
    Generator function to stream rows one by one from user_data table.
    Yields each row as a dictionary.
    """
    # Connect to your ALX_prodev database
    connection = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        port=int(os.getenv("MYSQL_PORT", 3308)),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", ""),
        database="ALX_prodev",
    )
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM user_data")
        for row in cursor:
            yield row
    finally:
        cursor.close()
        connection.close()
