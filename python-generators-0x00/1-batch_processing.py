#!/usr/bin/python3

import os
import mysql.connector


def stream_users_in_batches(batch_size):
    """
    Generator that yields batches of users from the user_data table
    with the specified batch size.
    """
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
        batch = []
        for row in cursor:  # LOOP 1
            batch.append(row)
            if len(batch) == batch_size:
                yield batch
                batch = []
        if batch:
            yield batch
    finally:
        cursor.close()
        connection.close()


def batch_processing(batch_size):
    """
    Processes each batch to filter users over the age of 25
    and prints them.
    """
    for batch in stream_users_in_batches(batch_size):  # LOOP 2
        for user in batch:  # LOOP 3
            if user["age"] > 25:
                print(user)
