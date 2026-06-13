import streamlit as st

st.set_page_config(
page_title="Campus Engagement",
layout="wide"
)

st.title("🎓 Campus Engagement Platform")

college_id = st.text_input(
"Enter College ID"
)

if st.button("Login"):

    if college_id.startswith(
        ("SM","SL","SE")
    ):

        st.success(
            "Verified Login"
        )

        st.session_state.logged=True

    else:
        st.error(
            "Invalid ID"
        )