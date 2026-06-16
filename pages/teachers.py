import streamlit as st

st.set_page_config(
    page_title="Teacher Portal",
    page_icon="👩‍🏫",
    layout="wide"
)

# -------------------------
# SESSION
# -------------------------

if "teacher_announcements" not in st.session_state:
    st.session_state.teacher_announcements = []

# -------------------------
# HEADER
# -------------------------

st.title("👩‍🏫 Teacher Portal")

st.caption(
    "Monitor • Guide • Engage"
)

# -------------------------
# NOTICE
# -------------------------

st.subheader("📢 Faculty Notice Board")

notice = st.text_area(
    "Write Announcement"
)

if st.button(
    "Publish Announcement"
):

    if notice:

        st.session_state.teacher_announcements.append(
            notice
        )

        st.success(
            "Announcement Published"
        )

st.markdown("---")

# -------------------------
# DASHBOARD
# -------------------------

st.subheader(
    "📌 Published Announcements"
)

if len(
    st.session_state.teacher_announcements
) == 0:

    st.info(
        "No announcements yet"
    )

for i, announcement in enumerate(
    st.session_state.teacher_announcements
):

    box, delete = st.columns(
        [5,1]
    )

    with box:

        st.info(
            announcement
        )

    with delete:

        if st.button(
            "🗑 Delete",
            key=f"teacher_{i}"
        ):

            st.session_state.teacher_announcements.pop(
                i
            )

            st.rerun()

st.markdown("---")

st.caption(
    "Mahindra University • Teacher Portal"
)