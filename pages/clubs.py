import streamlit as st

st.title("🏆 Clubs")

clubs = [
"Marketing Club",
"Finance Club",
"Sports Club"
]

for c in clubs:

    st.write(c)

    if st.button(
        f"Follow {c}"
    ):

        st.success(
            "Following"
        )