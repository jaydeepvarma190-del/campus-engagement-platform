import streamlit as st
from auth import register, login
from database import create_tables


create_tables()


# -----------------------------
# PAGE
# -----------------------------


st.set_page_config(
    page_title="Campus Engagement Platform",
    page_icon="🎓",
    layout="wide"
)


# -----------------------------
# HEADER
# -----------------------------


st.title("🎓 Campus Engagement Platform")


st.caption(
"Discover • Connect • Participate"
)


# -----------------------------
# SIDEBAR
# -----------------------------


option = st.sidebar.radio(


"Select",


[


"Student Login",


"Club Member Login",


"Teacher Login",


"Sign Up"


]


)


# =================================
# STUDENT LOGIN
# =================================


if option == "Student Login":


    st.subheader(
        "👨‍🎓 Student Login"
    )


    email = st.text_input(
        "College Email"
    )


    password = st.text_input(
        "Password",
        type="password"
    )


    if st.button(
        "Student Login"
    ):


        user = login(
            email,
            password
        )


        if user:


            st.success(
                "Welcome Student 🎉"
            )


            st.switch_page(
                "pages/dashboard.py"
            )


        else:


            st.error(
                "Invalid credentials"
            )


# =================================
# CLUB MEMBER LOGIN
# =================================


elif option == "Club Member Login":


    st.subheader(
        "🏛 Club Member Login"
    )


    email = st.text_input(
        "Club Email"
    )


    password = st.text_input(
        "Password",
        type="password"
    )


    if st.button(
        "Club Login"
    ):


        user = login(
            email,
            password
        )


        if user:


            st.success(
                "Club Member Logged In 🎉"
            )


            st.switch_page(
                "pages/dashboard.py"
            )


        else:


            st.error(
                "Invalid credentials"
            )


# =================================
# TEACHER LOGIN
# =================================


elif option == "Teacher Login":


    st.subheader(
        "👩‍🏫 Teacher Login"
    )


    teacher = st.text_input(
        "University Email"
    )


    password = st.text_input(
        "Password",
        type="password"
    )


    if st.button(
        "Teacher Login"
    ):


        if teacher.endswith(
            "@mahindrauniversity.edu.in"
        ):


            st.success(
                "Teacher Login Successful"
            )


        else:


            st.error(
                "Use University Email"
            )


# =================================
# SIGN UP
# =================================


else:


    st.subheader(
        "✨ Sign Up"
    )


    role = st.selectbox(


        "Register As",


        [


        "Student",


        "Club Member",


        "Professor"


        ]


    )


    name = st.text_input(
        "Full Name"
    )


    email = st.text_input(
        "Email"
    )


    school = st.selectbox(


        "School",


        [


        "Engineering",


        "Management",


        "Law",


        "Media",


        "Sciences"


        ]


    )


    program = ""


    if role != "Professor":


        program = st.selectbox(


            "Program",


            [


            "Undergraduate",


            "Post Graduate",


            "PhD"


            ]


        )


    password = st.text_input(


        "Create Password",


        type="password"


    )


    if st.button(
        "Create Account"
    ):


        try:


            register(
                name,
                email,
                password
            )


            st.success(
                f"{role} Account Created 🎉"
            )


            st.balloons()


        except:


            st.error(
                "Account already exists"
            )


# -----------------------------
# FOOTER
# -----------------------------


st.markdown("---")


st.caption(
"Mahindra University • Campus Engagement Platform"
)

