import streamlit as st
import os
from song_data import songs
import streamlit.components.v1 as components
from datetime import datetime


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="NITU'S JUKEBOX",
    page_icon="🎧",
    layout="wide"
)


# ---------------- CSS ----------------

st.markdown("""
<style>

.stApp {

background:
linear-gradient(
135deg,
#ffd6e7,
#ffffff,
#f8bfd6
);

color:#111111;

font-family:Segoe UI;

}


.main-title {

font-size:50px;
font-weight:900;
color:#111111;
text-align:center;

}


.profile-card {

background:white;
padding:25px;
border-radius:25px;
border:1px solid #ff9fc1;
box-shadow:0 10px 25px rgba(0,0,0,.15);

animation:fade 1s;

}


.song-card {

background:white;
padding:18px;
border-radius:25px;
border:1px solid #ffc1d8;
box-shadow:0 10px 25px rgba(0,0,0,.15);
margin-bottom:20px;

transition:.3s;

}


.song-card:hover {

transform:translateY(-10px);

}


.song-card img {

border-radius:20px;

}


.category {

background:white;
padding:10px 18px;
border-radius:30px;
border:1px solid #ff8fb8;
color:#111;
font-weight:bold;

}


.stButton button {

background:white!important;
color:#111!important;
border:1px solid #ff8fb8!important;
border-radius:15px!important;

}


.stButton button:hover {

background:#ff8fb8!important;

}


.player {

background:white;
padding:30px;
border-radius:30px;
border:2px solid #ff8fb8;
box-shadow:0 10px 30px rgba(0,0,0,.2);

}


@keyframes fade {

from{

opacity:0;

transform:translateY(20px);

}

to{

opacity:1;

}

}


</style>
""",
unsafe_allow_html=True)



# ---------------- SONG DATA ----------------

songs = [
    {
          "title": "oda laage",
                      "artist": "sudhansu thapa",
                      "cover": "assets/song9.jpeg",
                      "file": "music/song9.mpeg",
                      "category": "EDM"  
        },
    {
            "title": "Raaz Aaankhe",
                    "artist": "Sudhansu",
                    "cover": "assets/song10.jpeg",
                    "file": "music/song10.mpeg",
                    "category": "EDM"
            },
    {
                "title": "Tenu itna me pyar kara",
                        "artist": "Sudhansu",
                        "cover": "assets/song11.jpeg",
                        "file": "music/song11.mpeg",
                        "category": "EDM"
                },
    {
        "title": "bairan",
        "artist": "sumit and anuj",
        "cover": "assets/song2.jpeg",
        "file": "music/song2.mpeg",
        "category": "Romantic"
    },
    {
        "title": "babli badmash",
        "artist": "sunidhi chauhan",
        "cover": "assets/song3.jpeg",
        "file": "music/song3.mpeg",
        "category": "Rock"
    },
    {
        "title": "mere rang me rangne waali",
        "artist": "udit",
        "cover": "assets/song4.jpeg",
        "file": "music/song4.mpeg",
        "category": "Trending"
    },
    {
        "title": "Arz ky hai",
        "artist": "Anuv jain",
        "cover": "assets/arz kiya hai.jpeg",
        "file": "music/song5.mpeg",
        "category": "Chill"
    },
    {
        "title": " Je tu meri jaan v maang le",
        "artist": "Akhil sachdeva",
        "cover": "assets/jaan v maang le.jpeg",
        "file": "music/song6.mpeg",
        "category": "EDM"
    },
    {
    "title": "udariyaan",
            "artist": "arjit singh",
            "cover": "assets/udariaan.jpeg",
            "file": "music/song7.mpeg",
            "category": "EDM"
    },
    {
    "title": "Tenu khabar nhi",
            "artist": "Arjit singh",
            "cover": "assets/munjeya.jpeg",
            "file": "music/song8.mpeg",
            "category": "EDM"
    },
    
    
    
    {
            "title": "haareya",
            "artist": "Arjit singh",
            "cover": "assets/song1.jpeg",
            "file": "music/song1.mpeg",
            "category": "Pop"
        }
]










# ---------------- SESSION ----------------

if "favorites" not in st.session_state:

    st.session_state.favorites=[]


if "current_song" not in st.session_state:

    st.session_state.current_song=None

if "recent" not in st.session_state:
    st.session_state.recent=[]

# ---------------- HEADER ----------------

st.markdown(
"""
<h1 class="main-title">
🎧 NITUFY
</h1>
""",
unsafe_allow_html=True
)


st.markdown(
"""
<div class="profile-card">

<img src="https://static.vecteezy.com/system/resources/thumbnails/070/262/054/small/young-girl-enjoys-vibrant-party-atmosphere-while-listening-to-music-in-stylish-hoodie-and-glasses-photo.jpg"
style="
width:100%;
height:210px;
object-fit:cover;
border-radius:10px;
margin-bottom:10px;
">

<h2>👤 NITU'S JUKEBOX</h2>

<p>
🎵 Music Lover • Playlist Creator • Premium Listener
</p>

</div>
""",
unsafe_allow_html=True
)




components.html(
"""
<style>

/* Hero Slider */
*{
margin:0;
padding:0;
box-sizing:border-box;
}

body{
background:transparent;
font-family:'Segoe UI',sans-serif;
}

.hero{
width:100%;
height:420px;
border-radius:30px;
overflow:hidden;
position:relative;
background:linear-gradient(135deg,#ffd6e7,#ffffff,#f8bfd6);
box-shadow:0 20px 45px rgba(0,0,0,.18);
}

.slide{
position:absolute;
width:100%;
height:100%;
display:flex;
justify-content:space-between;
align-items:center;
padding:50px;
opacity:0;
transition:1s;
}

.slide.active{
opacity:1;
}

.left{
width:55%;
}

.left h1{
font-size:48px;
color:#111;
margin-bottom:15px;
}

.left p{
font-size:18px;
color:#444;
margin-bottom:25px;
line-height:1.6;
}

.btn{
padding:14px 28px;
border:none;
border-radius:15px;
background:#ff5ca8;
color:white;
font-size:17px;
cursor:pointer;
margin-right:12px;
transition:.3s;
}

.btn:hover{
transform:translateY(-4px);
}

.right{
width:38%;
display:flex;
justify-content:center;
}

.album{
width:280px;
height:280px;
border-radius:30px;
overflow:hidden;
background:rgba(255,255,255,.35);
backdrop-filter:blur(15px);
box-shadow:0 10px 30px rgba(0,0,0,.2);
animation:float 3s ease-in-out infinite;
}

.album img{
width:100%;
height:100%;
object-fit:cover;
}

@keyframes float {
    0% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0); }
}



.arrow{
position:absolute;
top:50%;
transform:translateY(-50%);
width:48px;
height:48px;
border-radius:50%;
background:white;
display:flex;
align-items:center;
justify-content:center;
font-size:22px;
cursor:pointer;
user-select:none;
box-shadow:0 5px 15px rgba(0,0,0,.2);
}

#prev{left:20px;}
#next{right:20px;}

.dots{
position:absolute;
bottom:18px;
left:50%;
transform:translateX(-50%);
display:flex;
gap:10px;
}

.dot{
width:12px;
height:12px;
border-radius:50%;
background:#bbb;
}

.dot.active{
background:#ff5ca8;
}

@media(max-width:768px){

.hero{
height:600px;
}

.slide{
flex-direction:column;
padding:25px;
text-align:center;
}

.left{
width:100%;
}

.right{
width:100%;
margin-top:20px;
}

.album{
width:220px;
height:220px;
}

.left h1{
font-size:34px;
}

}

</style>


<div class="hero">

    <!-- Slide 1 -->
    <div class="slide active">
        <div class="left">
            <h1>Trending Songs</h1>
            <p>Listen to top trending hits anytime, anywhere.</p>
            <button class="btn">Play Now</button>
        </div>
        <div class="right">
            <div class="album">
                <img src="https://images.unsplash.com/photo-1470225620780-dba8ba36b745?w=500" alt="Music">
            </div>
        </div>
    </div>

    <!-- Slide 2 -->
    <div class="slide">
        <div class="left">
            <h1>Romantic Vibes</h1>
            <p>Feel the rhythm with soothing melodies.</p>
            <button class="btn">Explore</button>
        </div>
        <div class="right">
            <div class="album">
                <img src="https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?w=500" alt="Music">
            </div>
        </div>
    </div>

    <!-- Arrows -->
    <div id="prev" class="arrow">&#10094;</div>
    <div id="next" class="arrow">&#10095;</div>

    <!-- Dots -->
    <div class="dots">
        <div class="dot active"></div>
        <div class="dot"></div>
    </div>

</div>

<script>

const slides = document.querySelectorAll(".slide");
const dots = document.querySelectorAll(".dot");

let index = 0;

function showSlide(i){

    slides.forEach((slide)=>{
        slide.classList.remove("active");
    });

    dots.forEach((dot)=>{
        dot.classList.remove("active");
    });

    slides[i].classList.add("active");
    dots[i].classList.add("active");
}

document.getElementById("next").onclick = function(){

    index++;

    if(index >= slides.length){
        index = 0;
    }

    showSlide(index);

};

document.getElementById("prev").onclick = function(){

    index--;

    if(index < 0){
        index = slides.length - 1;
    }

    showSlide(index);

};

setInterval(function(){

    index++;

    if(index >= slides.length){
        index = 0;
    }

    showSlide(index);

}, 4000);

</script>



""",
height=430,
)
st.markdown("""
<div style="
background:rgba(255,255,255,0.6);
padding:15px;
border-radius:20px;
margin-bottom:20px;
box-shadow:0 8px 20px rgba(0,0,0,0.1);
text-align:center;
font-size:20px;
font-weight:700;
">
🏠 Home &nbsp;&nbsp; 🎵 Trending &nbsp;&nbsp; ❤️ Favorites &nbsp;&nbsp; 📂 Playlist
</div>
""",unsafe_allow_html=True)
# ---------------- SEARCH ----------------

search=st.text_input(
"🔍 Search Songs"
)



# ---------------- SONG LIST ----------------

st.header("🔥 Popular Songs")


filtered=[]


for song in songs:

    if search.lower() in song["title"].lower() or search=="":
        filtered.append(song)



cols=st.columns(3)



for i,song in enumerate(filtered):

    with cols[i%3]:


        st.markdown(
        '<div class="song-card">',
        unsafe_allow_html=True
        )


        st.image(song["cover"])


        st.subheader(song["title"])

        st.write(
        song["artist"]
        )


        c1,c2=st.columns(2)


        with c1:
         if st.button("▶ Play", key=f"play_{i}"):
            st.session_state.current_song = song
            if song not in st.session_state.recent:
                st.session_state.recent.insert(0, song)
            st.session_state.recent = st.session_state.recent[:5]

    with c2:
        if st.button("❤️", key=f"fav_{i}"):
            if "favorites" not in st.session_state:
                st.session_state.favorites = []
            if song not in st.session_state.favorites:
                st.session_state.favorites.append(song)

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

# ---------------- RECENTLY PLAYED ----------------

if st.session_state.recent:

    st.header("🕘 Recently Played")

    rcols=st.columns(5)

    for idx,item in enumerate(st.session_state.recent):

        with rcols[idx]:

            st.image(item["cover"])

            st.caption(item["title"])
        
        




# ---------------- FAVORITES ----------------

st.header("❤️ Favorites")


for fav in st.session_state.favorites:

    st.write(
    fav["title"],
    "-",
    fav["artist"]
    )




# ---------------- MUSIC PLAYER ----------------


if st.session_state.current_song:


    song=st.session_state.current_song


    st.header("🎧 Now Playing")


    st.write(
    song["title"],
    "-",
    song["artist"]
    )


    if os.path.exists(song["file"]):

        with open(song["file"],"rb") as f:

            audio=f.read()


        st.audio(
            audio,
            format="audio/mpeg"
        )


    else:

        st.error(
        "Music file not found: "+song["file"]
        )




# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.title("Profile")

    st.write(
    """
    👤 NITU'S JUKEBOX

    ⭐ Premium User

    🎵 120 Playlists

    ❤️ 85 Favorites
    """
    )