import os
import json
import requests
from dotenv import load_dotenv
import streamlit as st
from PIL import Image

# Load environment variables
load_dotenv()
edenai_api_key = os.getenv("EDENAI_API_KEY")

if edenai_api_key is None:
    raise ValueError("EdenAI API key not found. Please set the EDENAI_API_KEY environment variable.")

# Favicon
# favicon = Image.open("favicon.png")

# Streamlit Page Config
st.set_page_config(
    page_title="GenAI Demo | Trigent AXLR8 Labs",
    # page_icon=favicon,
    layout="wide",
    initial_sidebar_state="expanded"
)

########################################
#            CUSTOM STYLES             #
########################################
st.markdown("""
<style>
/* ---------- GLOBAL APP STYLES ---------- */
.stApp {
    background: #0A0A0A; /* Dark background */
    font-family: 'Helvetica Neue', sans-serif;
    margin: 0;
    padding: 0;
}

/* Center and widen the main container */
.block-container {
    max-width: 1200px !important;
    margin: 0 auto;
    padding: 0 1rem 3rem 1rem;
}

/* ---------- HEADER / NAV BAR ---------- */
.top-nav-bar {
    background: #000000;
    width: 100%;
    /* Reduced padding for shorter nav bar */
    padding: 0.5rem 2rem;
    position: fixed;
    top: 0;
    left: 0;
    z-index: 9999;
    border-bottom: 1px solid rgba(255,255,255,0.1);
}

.nav-content {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.nav-logo {
    font-size: 1.2rem;
    font-weight: 700;
    color: #ffffff;
}

.nav-links a {
    margin-left: 1.5rem;
    color: #ffffff;
    text-decoration: none;
    font-weight: 500;
    transition: color 0.3s ease;
}

.nav-links a:hover {
    color: #c084fc;
}

/* Reduced margin for the body space below the nav bar */
.body-space {
    margin-top: 60px;
}

/* ---------- HERO SECTION ---------- */
/* Smaller padding to reduce overall height */
.hero-section {
    background: radial-gradient(circle at top left, #3b0066 0%, #0A0A0A 80%);
    padding: 2rem 2rem 3rem 2rem; /* decreased from 4rem/6rem */
    border-radius: 8px;
    text-align: center;
    margin-bottom: 3rem;
}

/* Slightly smaller hero title */
.hero-title {
    font-size: 2.2rem; /* decreased from 2.8rem */
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 1rem;
    line-height: 1.2;
}

/* Slightly smaller hero subtitle */
.hero-subtitle {
    font-size: 1.1rem; /* decreased from 1.2rem */
    color: #d1d5db;
    margin-bottom: 2rem; /* decreased from 2.5rem */
}

/* We replicate a "search bar" style around the inputs */
.input-container {
    display: inline-flex;
    align-items: center;
    gap: 1rem;
    flex-wrap: wrap;
    justify-content: center;
    margin-top: 2rem;
    width: 100%;
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
}

/* Force the labels on text_area and text_input to be white */
.stTextArea label, .stTextInput label {
    color: #ffffff !important;
}

/* The text-area/input fields themselves */
.stTextArea textarea, .stTextInput input {
    background: #ffffff;
    border-radius: 50px;
    border: 2px solid #555;
    padding: 15px 20px;
    width: 100% !important;
    max-width: 100% !important;
    box-shadow: none !important;
    transition: all 0.3s ease;
    outline: none !important;
}

.stTextArea textarea:focus, .stTextInput input:focus {
    border-color: #9F7AEA !important; /* Purple accent */
    box-shadow: 0 0 0 3px rgba(159,122,234,0.2) !important;
}

/* ---------- BUTTON STYLES ---------- */
.stButton>button {
    background: linear-gradient(135deg, #9F7AEA 0%, #6B46C1 100%) !important;
    color: white !important;
    border-radius: 50px !important;
    border: none !important;
    padding: 0.8rem 1.5rem !important;
    font-weight: 600 !important;
    cursor: pointer;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    margin-top: 0 !important;
    white-space: nowrap;
}
.stButton>button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(159,122,234,0.4);
}

/* ---------- GENERATED PROMPT DISPLAY ---------- */
.prompt-box {
    background: #181818;
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 2rem;
}
.prompt-box h4 {
    color: #ffffff;
    margin-bottom: 0.5rem;
}
.prompt-box p {
    color: #bbbbbb;
    margin: 0;
}

/* ---------- IMAGE DISPLAY ---------- */
.stImage>img {
    border-radius: 12px;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
    border: 2px solid #222;
    margin-bottom: 2rem;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.stImage>img:hover {
    transform: scale(1.01);
    box-shadow: 0 12px 24px rgba(0,0,0,0.3);
}

/* ---------- FOOTER ---------- */
.footer {
    background: #000000;
    padding: 1rem;
    color: #ffffff;
    text-align: center;
    border-top: 1px solid rgba(255,255,255,0.1);
}
.footer a {
    color: #A78BFA;
    text-decoration: none;
    font-weight: 500;
    margin: 0 0.5rem;
}
.footer a:hover {
    color: #D6BCFA;
}

/* ---------- SPINNER OVERRIDES ---------- */
[data-testid="stSpinner"] {
    color: #ffffff !important;
}
[data-testid="stSpinner"] svg {
    stroke: #9F7AEA !important;
}

/* ---------- RESPONSIVE MEDIA QUERIES ---------- */
@media (max-width: 768px) {
    .hero-title {
        font-size: 1.8rem; /* smaller on mobile */
    }
    .hero-subtitle {
        font-size: 0.95rem;
    }
    .nav-links a {
        margin-left: 1rem;
        font-size: 0.9rem;
    }
}
</style>
""", unsafe_allow_html=True)

########################################
#             TOP NAV BAR              #
########################################
st.markdown("""
<div class="top-nav-bar">
    <div class="nav-content">
        <div class="nav-logo">
            Trigent AXLR8 Labs
        </div>
        <div class="nav-links">
            <a href="#">Home</a>
            <a href="#">Features</a>
            <a href="#">Pricing</a>
            <a href="#">Blog</a>
            <a href="#">Contact</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

########################################
#             HERO SECTION             #
########################################
st.markdown("""
<div class="body-space"></div>
<div class="hero-section">
    <h1 class="hero-title">Your Story, Your Style—AI-Driven Comic Creation Made Simple.</h1>
    <p class="hero-subtitle">Visualize, communicate, and iterate on designs in minutes. Just describe your scene, add a style, and let AI do the rest!</p>
</div>
""", unsafe_allow_html=True)

########################################
#             USER INPUTS              #
########################################
with st.container():
    st.markdown("<div class='input-container'>", unsafe_allow_html=True)
    col1, col2 = st.columns(2, gap="medium")

    with col1:
        SCENARIO = st.text_area(
            "What is your scene? (e.g., A futuristic city with flying cars...)",
            height=120
        )
    with col2:
        STYLE = st.text_input(
            "Which style? (e.g., Realistic, Anime, Comic...)"
        )

    st.markdown("</div>", unsafe_allow_html=True)

########################################
#          IMAGE GENERATION LOGIC      #
########################################
def generate_comic_image(prompt):
    url = "https://api.edenai.run/v2/image/generation"
    headers = {"Authorization": f"Bearer {edenai_api_key}"}
    payload = {
        "providers": "stabilityai",
        "text": prompt,
        "resolution": "1024x1024",
        "num_images": 1
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        response_data = response.json()
        if "stabilityai" in response_data and "items" in response_data["stabilityai"]:
            return response_data["stabilityai"]["items"][0]["image_resource_url"]
        return None
    except Exception as e:
        st.error(f"Error generating image: {str(e)}")
        return None

########################################
#            GENERATE BUTTON           #
########################################
generate_button = st.button("Generate")

########################################
#            MAIN APP LOGIC            #
########################################
if generate_button:
    if not SCENARIO.strip() or not STYLE.strip():
        st.warning("Please fill in both the scene description and style fields!")
    else:
        with st.spinner("Creating your masterpiece..."):
            full_prompt = f"{SCENARIO}, {STYLE}"
            
            # Display the prompt card
            st.markdown(f"""
            <div class="prompt-box">
                <h4>Prompt used for generation:</h4>
                <p>{full_prompt}</p>
            </div>
            """, unsafe_allow_html=True)

            # Generate and display the image
            image_url = generate_comic_image(full_prompt)
            if image_url:
                st.image(image_url, caption="Your Custom Creation", use_column_width=True)
            else:
                st.error("Failed to generate image. Please try again with a different prompt.")

########################################
#                FOOTER                #
########################################
st.markdown("""
<div class="footer">
    Created By Abhinav Abhishek
</div>
""", unsafe_allow_html=True)
