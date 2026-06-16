import sqlite3

# Connect database
conn = sqlite3.connect(
    "campus.db",
    check_same_thread=False
)

# Create cursor
cursor = conn.cursor()


def create_tables():

    # Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            email TEXT UNIQUE NOT NULL,

            password TEXT NOT NULL

        )
    """)

    conn.commit()