#!/usr/bin/python3

import os
import mysql.connector
import csv
import uuid

DB_NAME = "ALX_prodev"


def connect_db():
    try:
        connection = mysql.connector.connect(
            user=os.getenv("MYSQL_USER", "root"),
            password=os.getenv("MYSQL_PASSWORD"),
            host=os.getenv("MYSQL_HOST", "localhost"),
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def create_database(connection):
    cursor = connection.cursor()
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME};")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
    cursor.close()


def connect_to_prodev():
    try:
        connection = mysql.connector.connect(
            user=("MYSQL_USER", "root"), password=("MYSQL_PASSWORD"), host=("MYSQL_HOST", "localhost"), database=DB_NAME
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def create_table(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS user_data (
        user_id VARCHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age DECIMAL NOT NULL
    );
    """
    cursor = connection.cursor()
    try:
        cursor.execute(create_table_query)
        print("Table user_data created successfully")
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")
    cursor.close()


def insert_data(connection, filename):
    cursor = connection.cursor()
    try:
        with open(filename, mode="r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                user_id = str(uuid.uuid4())
                name = row["name"]
                email = row["email"]
                age = row["age"]

                cursor.execute(
                    """
                    SELECT * FROM user_data WHERE email = %s;
                """,
                    (email,),
                )
                existing = cursor.fetchone()
                if not existing:
                    cursor.execute(
                        """
                        INSERT INTO user_data (user_id, name, email, age)
                        VALUES (%s, %s, %s, %s);
                    """,
                        (user_id, name, email, age),
                    )
        connection.commit()
    except Exception as e:
        print(f"Error inserting data: {e}")
        connection.rollback()
    finally:
        cursor.close()
