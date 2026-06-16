import streamlit as st
import sqlite3


# ==========================
# DATABASE
# ==========================

conn = sqlite3.connect(
    "data/campus.db",
    check_same_thread=False
)

cur = conn.cursor()


# ==========================
# PAGE
# ==========================

st.set_page_config(
page_title="Dashboard",
layout="wide"
)


st.title(
"📊 Dashboard"
)

st.caption(
"Campus Engagement Hub"
)


# ==========================
# QUICK ACCESS
# ==========================

st.subheader(
"⚡ Quick Access"
)

col1,col2,col3,col4=st.columns(4)


with col1:

    if st.button(
    "🏠 Home",
    use_container_width=True
    ):

        st.switch_page(
        "pages/home.py"
        )


with col2:

    if st.button(
    "📅 Events",
    use_container_width=True
    ):

        st.switch_page(
        "pages/events.py"
        )


with col3:

    if st.button(
    "📚 Study Groups",
    use_container_width=True
    ):

        st.switch_page(
        "pages/studygroup.py"
        )


with col4:

    if st.button(
    "🏛️ Clubs",
    use_container_width=True
    ):

        st.switch_page(
        "pages/clubs.py"
        )


st.divider()


# ==========================
# TEACHER ANNOUNCEMENTS
# ==========================

st.header(
"👩‍🏫 Teacher Announcements"
)


try:

    cur.execute("""

    SELECT

    title,

    message,

    teacher,

    created_at

    FROM teacher_announcements

    ORDER BY id DESC

    """)

    teachers = cur.fetchall()


    if teachers:

        for row in teachers:

            with st.container():

                st.warning(

f"""
📢 {row[0]}

{row[1]}

By:
{row[2]}

🕒 {row[3]}
"""

)

    else:

        st.info(
        "No teacher announcements"
        )

except:

    st.info(
    "No teacher announcements"
    )


st.divider()


# ==========================
# CLUB ANNOUNCEMENTS
# ==========================

st.header(
"🏛️ Club Announcements"
)


try:

    cur.execute("""

    SELECT

    club,

    title,

    message,

    created_at

    FROM club_announcements

    ORDER BY id DESC

    """)

    clubs = cur.fetchall()


    if clubs:

        for row in clubs:

            with st.container():

                st.success(

f"""
🏛️ {row[0]}

{row[1]}

{row[2]}

🕒 {row[3]}
"""

)

    else:

        st.info(
        "No club announcements"
        )

except:

    st.info(
    "No club announcements"
    )


# ==========================
# CAMPUS SNAPSHOT
# ==========================

st.divider()

st.subheader(
"📈 Campus Snapshot"
)

c1,c2,c3,c4=st.columns(4)


with c1:
    st.metric(
        "Events",
        "18"
    )

with c2:
    st.metric(
        "Clubs",
        "24"
    )

with c3:
    st.metric(
        "Study Groups",
        "12"
    )

with c4:
    st.metric(
        "Students",
        "300+"
    )


# ==========================
# FOOTER
# ==========================

st.divider()

st.caption(
"Campus Engagement Platform • Mahindra University"
)