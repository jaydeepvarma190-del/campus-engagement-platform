import streamlit as st
import sqlite3
from datetime import datetime


conn = sqlite3.connect(
"data/campus.db",
check_same_thread=False
)

cur = conn.cursor()


cur.execute("""

CREATE TABLE IF NOT EXISTS club_announcements(

id INTEGER PRIMARY KEY AUTOINCREMENT,

club TEXT,

title TEXT,

message TEXT,

created_at TEXT

)

""")

conn.commit()


st.title(
"🏛️ Club Member Portal"
)


club = st.selectbox(

"Select Club",

[
"Finance Club",
"E-Cell",
"AIESEC",
"Kalakriti",
"Football Club",
"Qubit Club"
]

)


title = st.text_input(
"Announcement Title"
)

message = st.text_area(
"Write Announcement"
)


if st.button(
"🚀 Publish"
):

    cur.execute("""

    INSERT INTO
    club_announcements

    (
    club,
    title,
    message,
    created_at
    )

    VALUES
    (?, ?, ?, ?)

    """,

    (

    club,

    title,

    message,

    datetime.now().strftime(
        "%d %b %Y %I:%M %p"
    )

    ))

    conn.commit()

    st.success(
    "Published"
    )


st.divider()

st.subheader(
"Club Feed"
)


cur.execute("""

SELECT *
FROM club_announcements
ORDER BY id DESC

""")

rows = cur.fetchall()


for row in rows:

    st.success(
f"""
🏛️ {row[1]}

{row[2]}

{row[3]}

🕒 {row[4]}
"""
)