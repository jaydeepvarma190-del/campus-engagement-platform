import streamlit as st

st.set_page_config(
    page_title="Club Member",
    page_icon="🏛",
    layout="wide"
)

# -------------------------
# SESSION
# -------------------------

if "club_announcements" not in st.session_state:
    st.session_state.club_announcements = []

# -------------------------
# HEADER
# -------------------------

st.title(
    "🏛 Club Member Dashboard"
)

st.caption(
    "Manage • Publish • Connect"
)

# -------------------------
# ANNOUNCEMENT
# -------------------------

st.subheader(
    "📢 Club Announcement"
)

announcement = st.text_area(
    "Write Update"
)

if st.button(
    "Publish"
):

    if announcement:

        st.session_state.club_announcements.append(
            announcement
        )

        st.success(
            "Announcement Published"
        )

st.markdown("---")

# -------------------------
# DASHBOARD
# -------------------------

st.subheader(
    "📌 Club Updates"
)

if len(
    st.session_state.club_announcements
) == 0:

    st.info(
        "No announcements"
    )

for i, post in enumerate(
    st.session_state.club_announcements
):

    c1, c2 = st.columns(
        [5,1]
    )

    with c1:

        st.success(
            post
        )

    with c2:

        if st.button(
            "🗑 Delete",
            key=f"club_{i}"
        ):

            st.session_state.club_announcements.pop(
                i
            )

            st.rerun()

st.markdown("---")

st.caption(
    "Mahindra University • Club Member Portal"
)