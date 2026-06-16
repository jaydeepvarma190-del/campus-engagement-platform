import streamlit as st


# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="Buzzing Now",
    layout="wide"
)


# ==========================
# CUSTOM CSS
# ==========================

st.markdown("""
<style>

.stApp{
background:
linear-gradient(
180deg,
#050816,
#070b1a
);
color:white;
}


/* FIRE */

.fire-title{
display:flex;
align-items:center;
gap:20px;
margin-bottom:10px;
}

.fire{

font-size:78px;

animation:
flame 1.4s infinite,
float 2s ease-in-out infinite;

filter:
drop-shadow(0 0 15px orange)
drop-shadow(0 0 25px red);

}


@keyframes flame{

0%{
transform:
scale(1)
rotate(-2deg);
}

25%{
transform:
scale(1.1)
rotate(3deg);
}

50%{
transform:
scale(1.22)
rotate(-3deg);
}

75%{
transform:
scale(1.08)
rotate(2deg);
}

100%{
transform:
scale(1)
rotate(-2deg);
}

}

@keyframes float{

0%{
transform:
translateY(0px);
}

50%{
transform:
translateY(-8px);
}

100%{
transform:
translateY(0px);
}

}


.title{

font-size:72px;

font-weight:800;

background:
linear-gradient(
90deg,
white,
#ffba49
);

-webkit-background-clip:text;

-webkit-text-fill-color:transparent;

}



.subtitle{

color:#9ca3af;

font-size:22px;

margin-bottom:25px;

}


.card{

background:
linear-gradient(
90deg,
#0d3d24,
#115d37
);

padding:30px;

border-radius:18px;

margin-bottom:35px;

}


.section{

margin-top:45px;

font-size:40px;

font-weight:700;

}


.event{

background:#111827;

padding:20px;

border-radius:16px;

margin-top:18px;

}


.club{

background:#101827;

padding:15px;

border-radius:12px;

}

</style>
""", unsafe_allow_html=True)


# ==========================
# HEADER
# ==========================

st.markdown("""

<div class="fire-title">

<div class="fire">
🔥
</div>

<div class="title">
Buzzing Now
</div>

</div>

<div class="subtitle">

Discover opportunities built around your interests

</div>

""",

unsafe_allow_html=True)


# ==========================
# STATS
# ==========================

st.markdown("""

<div class="card">

<h2>
✨ Your campus is active today
</h2>

<h3>
24 Clubs
</h3>

<h3>
18 Events
</h3>

<h3>
300+ Students Participating
</h3>

</div>

""",

unsafe_allow_html=True)


# ==========================
# FOLLOW CLUBS
# ==========================

st.markdown(
'<div class="section">🏛️ Follow Clubs</div>',
unsafe_allow_html=True
)

clubs = [

"Finance Club",

"Entrepreneurship Cell",

"AIESEC",

"MU Qubit Club",

"Art Felt Club",

"Kalakriti Cultural Club",

"Ambrosia Biology Club",

"AeiForia Sustainability Club",

"Outreach Club",

"Rotaract Club",

"Aether Committee",

"AIRO Committee",

"Football Club",

"Cricket Club",

"Badminton Club",

"Basketball Club"

]

selected = st.multiselect(

"Choose clubs",

clubs

)

if st.button(
"Save Preferences"
):

    st.success(
        "Clubs saved"
    )


# ==========================
# TRENDING
# ==========================

st.markdown(
'<div class="section">🔥 Trending Across Campus</div>',
unsafe_allow_html=True
)

events = [

"🎤 Startup Talk",

"🏆 Sports Tournament",

"🎵 Cultural Fest",

"💼 Placement Drive",

"🎓 Guest Lecture"

]

for e in events:

    st.markdown(

f"""

<div class="event">

{e}

</div>

""",

unsafe_allow_html=True

)


# ==========================
# RECOMMENDED
# ==========================

st.markdown(
'<div class="section">⭐ Recommended For You</div>',
unsafe_allow_html=True
)

st.info(
"""
Marketing Workshop

Finance Competition

Startup Meetup
"""
)


# ==========================
# SCHOOL SECTION
# ==========================

st.markdown(
'<div class="section">📚 From Your School</div>',
unsafe_allow_html=True
)

col1,col2,col3=st.columns(3)

with col1:
    st.metric(
        "Workshops",
        "8"
    )

with col2:
    st.metric(
        "Competitions",
        "5"
    )

with col3:
    st.metric(
        "Open Registrations",
        "12"
    )


# ==========================
# FOOTER
# ==========================

st.divider()

st.caption(
"Campus Engagement Platform • Mahindra University"
)