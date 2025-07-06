#!/usr/bin/python3

# lazy_paginate.py — Generator that lazily paginates user_data table
seed = __import__("seed")


def paginate_users(page_size, offset):
    """
    Fetch a page of users from the user_data table using LIMIT and OFFSET.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows


def lazy_pagination(page_size):
    """
    Generator that lazily paginates through user_data using paginate_users,
    yielding each page only when needed.
    Uses only one loop.
    """
    offset = 0
    while True:  # SINGLE LOOP
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size
