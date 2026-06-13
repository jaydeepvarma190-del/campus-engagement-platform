import streamlit as st

st.title("📅 Events")

events = [

{
"name":"Startup Talk",
"venue":"Auditorium",
"time":"4 PM"
},

{
"name":"Hackathon",
"venue":"Lab 1",
"time":"2 PM"
}

]

for e in events:

    st.subheader(
        e["name"]
    )

    st.write(
        e["venue"]
    )

    st.write(
        e["time"]
    )

    if st.button(
        f"RSVP {e['name']}"
    ):
        st.success(
            "Registered"
        )