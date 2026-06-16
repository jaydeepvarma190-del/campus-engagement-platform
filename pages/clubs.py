import streamlit as st
import random

st.set_page_config(
    page_title="Campus Clubs",
    page_icon="🏛️",
    layout="wide"
)

# --------------------------------
# TITLE
# --------------------------------

st.title("🏛️ Campus Communities")

st.caption(
"Discover • Join • Build • Connect"
)

# --------------------------------
# SESSION
# --------------------------------

if "joined_clubs" not in st.session_state:
    st.session_state.joined_clubs = []

# --------------------------------
# CLUB DATA
# --------------------------------

clubs = {

"Finance Club":[
"💰 Finance",
"Investment • Markets • Business",
"Learn finance and networking",
523
],

"Entrepreneurship Cell (E-Cell)":[
"🚀 Startup",
"Innovation • Startups",
"Build and launch ideas",
741
],

"AIESEC":[
"🌍 Global",
"Leadership • Exchange",
"International opportunities",
412
],

"MU Qubit Club":[
"⚛ Tech",
"Quantum • AI",
"Advanced technologies",
280
],

"Art Felt Club":[
"🎨 Creative",
"Art • Design",
"Express creativity",
220
],

"Kalakriti Cultural Club":[
"🎭 Cultural",
"Performances",
"Stage and events",
480
],

"Dance Club":[
"💃 Performance",
"Choreography",
"Perform and compete",
360
],

"Football Club":[
"⚽ Sports",
"Training",
"Fitness and teamwork",
610
],

"Debate Club":[
"🎤 Public Speaking",
"Debates",
"Communication skills",
180
],

"Astronomy Club":[
"🌌 Science",
"Space",
"Explore the universe",
140
]

}

# --------------------------------
# SEARCH
# --------------------------------

search = st.text_input(
    "🔍 Search Club"
)

# --------------------------------
# STATS
# --------------------------------

a,b,c=st.columns(3)

with a:
    st.metric(
        "🏛 Clubs",
        "24"
    )

with b:
    st.metric(
        "👥 Joined",
        len(
            st.session_state.joined_clubs
        )
    )

with c:
    st.metric(
        "🔥 Trending",
        "6"
    )

st.markdown("---")

# --------------------------------
# FEATURED
# --------------------------------

st.subheader("🔥 Trending This Week")

featured = [
"Finance Club",
"E-Cell",
"Football Club"
]

for item in featured:

    st.success(
        item
    )

st.markdown("---")

# --------------------------------
# CLUBS
# --------------------------------

for club,data in clubs.items():

    if search.lower() in club.lower():

        with st.container():

            st.markdown(
f"### {club}"
            )

            c1,c2 = st.columns(
                [4,1]
            )

            with c1:

                st.write(
                    data[0]
                )

                st.write(
                    data[1]
                )

                st.caption(
                    data[2]
                )

                st.progress(
                    random.randint(
                        55,
                        95
                    )
                )

                st.write(
f"👥 {data[3]} Members"
                )

            with c2:

                if club not in st.session_state.joined_clubs:

                    if st.button(
                        "Join",
                        key=club
                    ):

                        st.session_state.joined_clubs.append(
                            club
                        )

                        st.rerun()

                else:

                    st.success(
                        "Joined"
                    )

            if club in st.session_state.joined_clubs:

                st.info(
f"""
🎉 Welcome to {club}

Inside this app you now receive:

📢 Announcements

📅 Event alerts

👥 Club chats

🏆 Competitions

🎯 Opportunities
"""
                )

                updates = [

"Workshop Registration Open",

"New Event Added",

"Community Meet This Week"

]

                for u in updates:

                    st.success(
                        u
                    )

            st.markdown("---")

# --------------------------------
# FOOTER
# --------------------------------

st.markdown("---")

st.caption(
"Mahindra University • Campus Engagement Platform"
)