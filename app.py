import streamlit as st
import sqlite3

# -------------------
# Database Connection
# -------------------

conn = sqlite3.connect(
    "data/campus.db",
    check_same_thread=False
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
college_id TEXT UNIQUE,
password TEXT,
school TEXT,
program TEXT
)
""")

conn.commit()


# -------------------
# Helper Functions
# -------------------

def signup(name, college_id,
           password,
           school,
           program):

    try:

        cur.execute("""
        INSERT INTO students
        (
        name,
        college_id,
        password,
        school,
        program
        )

        VALUES
        (?, ?, ?, ?, ?)

        """,

        (
        name,
        college_id,
        password,
        school,
        program
        ))

        conn.commit()

        return True

    except:
        return False


def login(
college_id,
password
):

    cur.execute("""
    SELECT *
    FROM students
    WHERE college_id=?
    AND password=?
    """,

    (
    college_id,
    password
    ))

    return cur.fetchone()


# -------------------
# Streamlit UI
# -------------------

st.set_page_config(
page_title="Campus Engagement",
layout="wide"
)

st.title(
"🎓 Campus Engagement Platform"
)

option = st.sidebar.selectbox(

"Choose",

[
"Login",
"Sign Up"
]

)


# ===================
# LOGIN
# ===================

if option == "Login":

    st.header(
    "Existing Student Login"
    )

    college_id = st.text_input(
    "College ID"
    )

    password = st.text_input(
    "Password",
    type="password"
    )

    if st.button(
    "Login"
    ):

        user = login(
        college_id,
        password
        )

        if user:

            st.success(
            f"Welcome {user[1]}"
            )

            st.session_state.logged = True
            st.session_state.user = user[1]

        else:

            st.error(
            "Invalid Login"
            )


# ===================
# SIGNUP
# ===================

else:

    st.header(
    "New Student Registration"
    )

    name = st.text_input(
    "Full Name"
    )

    college_id = st.text_input(
    "College ID"
    )

    school = st.selectbox(

    "School",

    [
    "Management",
    "Engineering",
    "Law",
    "Design"
    ]

    )

    program = st.text_input(
    "Program"
    )

    password = st.text_input(
    "Create Password",
    type="password"
    )

    if st.button(
    "Create Account"
    ):

        valid = (
        college_id.startswith(
        (
        "SM",
        "SL",
        "SE"
        )
        )
        )

        if not valid:

            st.error(
            "Use valid college ID"
            )

        else:

            success = signup(

            name,
            college_id,
            password,
            school,
            program

            )

            if success:

                st.success(
                "Account Created"
                )

                st.info(
                "Go to Login"
                )

            else:

                st.error(
                "Student already exists"
                )