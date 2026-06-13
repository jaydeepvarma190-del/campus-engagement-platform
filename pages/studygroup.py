import streamlit as st

st.title("📚 Study Groups")

group = st.text_input(
"Group Name"
)

if st.button(
"Create"
):

    st.success(
        "Created"
    )