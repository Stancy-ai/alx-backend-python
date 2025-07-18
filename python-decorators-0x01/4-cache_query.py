import sqlite3
import functools

query_cache = {}


def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("users.db")
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()

    return wrapper


def cache_query(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        # Extract the query from positional or keyword arguments
        query = kwargs.get("query")
        if query is None and len(args) > 0:
            query = args[0]
        if query is None:
            raise ValueError("No SQL query provided for caching.")

        if query in query_cache:
            print("Returning cached result for query.")
            return query_cache[query]
        else:
            print("Executing and caching result for query.")
            result = func(conn, *args, **kwargs)
            query_cache[query] = result
            return result

    return wrapper


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


# First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")
print(users)

# Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
print(users_again)
