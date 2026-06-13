import sqlite3

conn = sqlite3.connect(
    "data/campus.db",
    check_same_thread=False
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY,
college_id TEXT UNIQUE,
name TEXT,
school TEXT,
program TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS events(
id INTEGER PRIMARY KEY,
title TEXT,
club TEXT,
venue TEXT,
date TEXT,
attending INTEGER
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS clubs(
id INTEGER PRIMARY KEY,
name TEXT,
description TEXT
)
""")

conn.commit()