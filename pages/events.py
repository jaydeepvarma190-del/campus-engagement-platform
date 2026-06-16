import streamlit as st

# --------------------------------
# PAGE CONFIG
# --------------------------------

st.set_page_config(
    page_title="Events",
    page_icon="🎉",
    layout="wide"
)

# --------------------------------
# TITLE
# --------------------------------

st.title("🎉 Campus Events")

st.caption(
"Discover • RSVP • Participate • Connect"
)

# --------------------------------
# SESSION
# --------------------------------

if "rsvp" not in st.session_state:
    st.session_state.rsvp = []

# --------------------------------
# SEARCH
# --------------------------------

search = st.text_input(
    "🔍 Search Event"
)

# --------------------------------
# STATS
# --------------------------------

a,b,c = st.columns(3)

with a:
    st.metric(
        "📅 Events",
        "25"
    )

with b:
    st.metric(
        "👥 Going",
        len(
            st.session_state.rsvp
        )
    )

with c:
    st.metric(
        "🔥 Trending",
        "7"
    )

st.markdown("---")

# --------------------------------
# FEATURED
# --------------------------------

st.subheader("🔥 Trending This Week")

st.success(
"""
🚀 Startup Summit

Founder Talks • Networking • Workshops

Today • Auditorium
"""
)

st.markdown("---")

# --------------------------------
# EVENT DATA
# --------------------------------

events = [

{
"title":"Startup Talk",
"emoji":"🚀",
"place":"Auditorium",
"time":"4:00 PM",
"type":"Career",
"description":"Meet founders and learn startup building."
},

{
"title":"Hackathon",
"emoji":"💻",
"place":"Lab 1",
"time":"2:00 PM",
"type":"Technology",
"description":"Build products with your team."
},

{
"title":"Open Mic Night",
"emoji":"🎤",
"place":"Amphitheatre",
"time":"6:30 PM",
"type":"Culture",
"description":"Music, poetry and performances."
},

{
"title":"Football Trials",
"emoji":"⚽",
"place":"Sports Ground",
"time":"5:00 PM",
"type":"Sports",
"description":"Selection for university team."
},

{
"title":"Finance Workshop",
"emoji":"📈",
"place":"Block C",
"time":"11:00 AM",
"type":"Professional",
"description":"Learn investing and markets."
}

]

# --------------------------------
# EVENTS
# --------------------------------

for event in events:

    if search.lower() in event["title"].lower():

        with st.container():

            st.markdown(
f"""
## {event["emoji"]} {event["title"]}
"""
            )

            col1,col2 = st.columns([3,1])

            with col1:

                st.write(
f"📍 {event['place']}"
                )

                st.write(
f"🕒 {event['time']}"
                )

                st.write(
f"🏷 {event['type']}"
                )

                st.info(
                    event["description"]
                )

            with col2:

                if event["title"] not in st.session_state.rsvp:

                    if st.button(
                        "🎟 RSVP",
                        key=event["title"]
                    ):

                        st.session_state.rsvp.append(
                            event["title"]
                        )

                        st.rerun()

                else:

                    st.success(
                        "Going ✅"
                    )

            if event["title"] in st.session_state.rsvp:

                st.success(
f"""
You are registered for
{event["title"]}
"""
                )

                st.write(
"""
You will receive:

📢 Event reminders

📍 Location updates

👥 Attendee updates

🏆 Participation opportunities
"""
                )

                st.progress(80)

            st.markdown("---")

# --------------------------------
# UPCOMING
# --------------------------------

st.subheader("📆 Upcoming Calendar")

st.info(
"""
Monday → Startup Summit

Wednesday → Open Mic

Friday → Football Trials

Saturday → Hackathon
"""
)

# --------------------------------
# FOOTER
# --------------------------------

st.markdown("---")

st.caption(
"Mahindra University • Campus Engagement Platform"
)