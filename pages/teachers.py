import streamlit as st

st.set_page_config(
    page_title="Teacher Portal",
    page_icon="👩‍🏫",
    layout="wide"
)

# ---------------------
# SESSION
# ---------------------

if "teacher_posts" not in st.session_state:
    st.session_state.teacher_posts = []

# ---------------------
# HEADER
# ---------------------

st.title("👩‍🏫 Teacher Portal")

st.caption(
"Create • Publish • Manage"
)

# ---------------------
# CREATE
# ---------------------

st.subheader(
"📢 Publish Announcement"
)

title = st.text_input(
"Announcement Title"
)

message = st.text_area(
"Announcement"
)

if st.button(
"Publish"
):

    if title and message:

        st.session_state.teacher_posts.append({

        "title":title,

        "message":message

        })

        st.success(
        "Announcement Published"
        )

        st.rerun()

# ---------------------
# DASHBOARD
# ---------------------

st.markdown("---")

st.subheader(
"📌 Published Announcements"
)

if len(
st.session_state.teacher_posts
)==0:

    st.info(
    "No announcements"
    )

for i,post in enumerate(
st.session_state.teacher_posts
):

    c1,c2=st.columns(
    [6,1]
    )

    with c1:

        st.success(
f"""
📢 {post["title"]}

{post["message"]}
"""
        )

    with c2:

        if st.button(

        "🗑",

        key=f"teacher{i}"

        ):

            st.session_state.teacher_posts.pop(
            i
            )

            st.rerun()

st.markdown("---")

st.caption(
"Mahindra University"
)