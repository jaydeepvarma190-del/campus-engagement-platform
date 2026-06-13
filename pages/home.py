import streamlit as st

st.title("🔥 Buzzing Now")

clubs = st.multiselect(
"Follow Clubs",
[
"Marketing",
"Finance",
"Sports",
"Photography"
]
)

interests = st.multiselect(
"Choose Interests",
[
"Coding",
"Design",
"Finance"
]
)

if st.button("Save"):

    st.success(
        "Preferences Saved"
    )