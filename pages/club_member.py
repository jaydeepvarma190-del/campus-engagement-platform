import streamlit as st

st.set_page_config(
page_title="Club Member",
page_icon="🏛",
layout="wide"
)

# ---------------------
# SESSION
# ---------------------

if "club_posts" not in st.session_state:
    st.session_state.club_posts=[]

# ---------------------
# HEADER
# ---------------------

st.title(
"🏛 Club Member Dashboard"
)

st.caption(
"Publish • Update • Manage"
)

# ---------------------
# CREATE
# ---------------------

st.subheader(
"📢 Publish Club Update"
)

title=st.text_input(
"Title"
)

message=st.text_area(
"Update"
)

if st.button(
"Publish"
):

    if title and message:

        st.session_state.club_posts.append({

        "title":title,

        "message":message

        })

        st.success(
        "Published"
        )

        st.rerun()

# ---------------------
# POSTS
# ---------------------

st.markdown("---")

st.subheader(
"📌 Published Updates"
)

if len(
st.session_state.club_posts
)==0:

    st.info(
    "No announcements"
    )

for i,post in enumerate(
st.session_state.club_posts
):

    a,b=st.columns(
    [6,1]
    )

    with a:

        st.info(
f"""
🏛 {post["title"]}

{post["message"]}
"""
        )

    with b:

        if st.button(

        "🗑",

        key=f"club{i}"

        ):

            st.session_state.club_posts.pop(
            i
            )

            st.rerun()

st.markdown("---")

st.caption(
"Mahindra University"
)