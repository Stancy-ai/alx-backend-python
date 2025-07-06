# 4-stream_ages.py — Compute average age using a generator (memory-efficient)

import seed


def stream_user_ages():
    """
    Generator that yields user ages one by one from the user_data table.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data")
    for row in cursor:
        yield row["age"]
    cursor.close()
    connection.close()


def calculate_average_age():
    """
    Uses the stream_user_ages generator to compute average age
    without loading the entire dataset into memory.
    """
    total_age = 0
    count = 0
    for age in stream_user_ages():  # FIRST LOOP
        total_age += age
        count += 1
    if count == 0:
        print("No users found.")
    else:
        average_age = total_age / count
        print(f"Average age of users: {average_age:.2f}")


if __name__ == "__main__":
    calculate_average_age()
