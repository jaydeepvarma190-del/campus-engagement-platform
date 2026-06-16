import streamlit as st

# --------------------------------
# PAGE
# --------------------------------

st.set_page_config(
    page_title="Study Buddy",
    page_icon="📚",
    layout="wide"
)

# --------------------------------
# SESSION
# --------------------------------

if "posts" not in st.session_state:
    st.session_state.posts = []

# --------------------------------
# TITLE
# --------------------------------

st.title("📚 Study Buddy")

st.caption(
"Post requests • Find study partners • Connect"
)

# --------------------------------
# MENU
# --------------------------------

tab = st.radio(

"Select",

[
"➕ Post",

"🙋 Request"

]

)

st.markdown("---")

# ==================================
# POST
# ==================================

if tab == "➕ Post":

    st.subheader(
        "Create Study Request"
    )

    name = st.text_input(
        "Your Name"
    )

    student_id = st.text_input(
        "Student ID"
    )

    subject = st.selectbox(

        "Subject",

        [

        "Programming",

        "Finance",

        "Math",

        "Physics",

        "AI",

        "Management"

        ]

    )

    location = st.selectbox(

        "Location",

        [

        "Library",

        "Block A",

        "Block B",

        "Study Hall",

        "Cafeteria",

        "Online"

        ]

    )

    date = st.date_input(
        "Date"
    )

    time = st.time_input(
        "Time"
    )

    message = st.text_area(
        "Request Message"
    )

    if st.button(
        "🚀 Post Request"
    ):

        st.session_state.posts.append({

        "name":name,

        "id":student_id,

        "subject":subject,

        "location":location,

        "date":date,

        "time":time,

        "message":message

        })

        st.success(
            "Request Posted"
        )

        st.balloons()

# ==================================
# REQUEST
# ==================================

else:

    st.subheader(
        "Available Requests"
    )

    if len(
        st.session_state.posts
    ) == 0:

        st.info(
            "No requests available"
        )

    for i,post in enumerate(
        st.session_state.posts
    ):

        with st.container():

            st.markdown(
f"## 👤 {post['name']}"
            )

            st.write(
f"🆔 {post['id']}"
            )

            st.write(
f"📚 {post['subject']}"
            )

            st.write(
f"📍 {post['location']}"
            )

            st.write(
f"📅 {post['date']}"
            )

            st.write(
f"🕒 {post['time']}"
            )

            st.info(
                post["message"]
            )

            if st.button(

                "🤝 Apply to Join",

                key=i

            ):

                st.success(
f"""
Application Sent

Meet at:
{post['location']}

Time:
{post['time']}
"""
                )

            st.markdown("---")

# --------------------------------
# FOOTER
# --------------------------------

st.caption(
"Mahindra University • Study Buddy"
)