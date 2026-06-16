import streamlit as st
import sqlite3
from datetime import datetime


# =====================
# DATABASE
# =====================

conn = sqlite3.connect(
    "data/campus.db",
    check_same_thread=False
)

cur = conn.cursor()


cur.execute("""

CREATE TABLE IF NOT EXISTS teacher_announcements(

id INTEGER PRIMARY KEY AUTOINCREMENT,

teacher TEXT,

title TEXT,

message TEXT,

created_at TEXT

)

""")

conn.commit()


# =====================
# PAGE
# =====================

st.title("👩‍🏫 Teacher Announcements")

st.write(
"Publish announcements for students"
)


teacher = st.text_input(
"Teacher Name"
)

title = st.text_input(
"Announcement Title"
)

message = st.text_area(
"Write Announcement"
)


if st.button(
"📢 Publish Announcement"
):

    if teacher and title and message:

        cur.execute("""

        INSERT INTO teacher_announcements
        (
        teacher,
        title,
        message,
        created_at
        )

        VALUES
        (?, ?, ?, ?)

        """,

        (

        teacher,

        title,

        message,

        datetime.now().strftime(
            "%d %b %Y %I:%M %p"
        )

        ))

        conn.commit()

        st.success(
            "Announcement Published"
        )


st.divider()

st.subheader(
"Published"
)


cur.execute("""

SELECT *
FROM teacher_announcements
ORDER BY id DESC

""")

rows = cur.fetchall()

for row in rows:

    with st.container():

        st.info(
f"""
📢 {row[2]}

{row[3]}

— {row[1]}

🕒 {row[4]}
"""
)