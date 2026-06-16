import streamlit as st

# --------------------------------
# PAGE
# --------------------------------

st.set_page_config(
    page_title="Dashboard",
    page_icon="🎓",
    layout="wide"
)

# --------------------------------
# SESSION
# --------------------------------

if "teacher_posts" not in st.session_state:
    st.session_state.teacher_posts = []

if "club_posts" not in st.session_state:
    st.session_state.club_posts = []

# --------------------------------
# STYLE
# --------------------------------

st.markdown("""
<style>

.stApp{
background:
linear-gradient(
to right,
#071426,
#10213d
);

color:white;
}

.card{
padding:20px;
border-radius:18px;
background:#132848;
}

</style>
""",
unsafe_allow_html=True)

# --------------------------------
# HEADER
# --------------------------------

st.title(
    "🎓 Campus Dashboard"
)

st.caption(
    "Discover • Connect • Participate"
)

st.markdown("---")

# --------------------------------
# METRICS
# --------------------------------

c1,c2,c3,c4=st.columns(4)

with c1:
    st.metric(
        "🎉 Events",
        "25"
    )

with c2:
    st.metric(
        "🏛 Clubs",
        "24"
    )

with c3:
    st.metric(
        "📚 Study Groups",
        "15"
    )

with c4:
    st.metric(
        "🚀 Opportunities",
        "18"
    )

st.markdown("---")

# --------------------------------
# QUICK ACCESS
# --------------------------------

st.subheader(
    "⚡ Quick Access"
)

a,b,c=st.columns(3)

with a:

    if st.button(
        "🏛 Clubs",
        use_container_width=True
    ):

        st.switch_page(
            "pages/clubs.py"
        )

with b:

    if st.button(
        "🎉 Events",
        use_container_width=True
    ):

        st.switch_page(
            "pages/events.py"
        )

with c:

    if st.button(
        "📚 Study Groups",
        use_container_width=True
    ):

        st.switch_page(
            "pages/studygroup.py"
        )

st.markdown("---")

# ==================================
# TEACHER ANNOUNCEMENTS
# ==================================

st.subheader(
    "👩‍🏫 Teacher Announcements"
)

if len(
    st.session_state.teacher_posts
) == 0:

    st.info(
        "No teacher announcements"
    )

else:

    for i,post in enumerate(
        st.session_state.teacher_posts
    ):

        left,right=st.columns(
            [8,1]
        )

        with left:

            st.warning(
                f"📢 {post}"
            )

        with right:

            if st.button(
                "🗑",
                key=f"teacher_{i}"
            ):

                st.session_state.teacher_posts.pop(
                    i
                )

                st.rerun()

st.markdown("---")

# ==================================
# CLUB ANNOUNCEMENTS
# ==================================

st.subheader(
    "🏛 Club Announcements"
)

if len(
    st.session_state.club_posts
) == 0:

    st.info(
        "No club announcements"
    )

else:

    for i,post in enumerate(
        st.session_state.club_posts
    ):

        left,right=st.columns(
            [8,1]
        )

        with left:

            st.success(
                f"📣 {post}"
            )

        with right:

            if st.button(
                "🗑",
                key=f"club_{i}"
            ):

                st.session_state.club_posts.pop(
                    i
                )

                st.rerun()

st.markdown("---")

# --------------------------------
# TRENDING
# --------------------------------

st.subheader(
    "🔥 Trending"
)

st.success(
"""
Finance Club Recruitment Open
"""
)

st.success(
"""
Hackathon Registration Live
"""
)

st.success(
"""
Study Buddy Requests Increasing
"""
)

st.markdown("---")

# --------------------------------
# FOOTER
# --------------------------------

st.caption(
    "Mahindra University • Campus Engagement Platform"
)