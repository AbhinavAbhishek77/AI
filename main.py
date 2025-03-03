
import os
import json
import requests
from dotenv import load_dotenv
import streamlit as st
from PIL import Image

# ----------------------------------------------------------------------------
#               LOAD ENVIRONMENT VARIABLES & CONFIGURE STREAMLIT
# ----------------------------------------------------------------------------
load_dotenv()
edenai_api_key = os.getenv("EDENAI_API_KEY")

if edenai_api_key is None:
    raise ValueError("EdenAI API key not found. Please set the EDENAI_API_KEY environment variable.")

st.set_page_config(
    page_title="GenAI Demo | Trigent AXLR8 Labs",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------------------------------
#                                CUSTOM STYLES
# ----------------------------------------------------------------------------
st.markdown("""
<style>
/* ---------- GLOBAL APP STYLES ---------- */
.stApp {
    background: #0A0A0A; /* Dark background */
    font-family: 'Helvetica Neue', sans-serif;
    margin: 0;
    padding: 0;
}

.block-container {
    max-width: 1200px !important;
    margin: 0 auto;
    padding: 0 1rem 3rem 1rem;
}

/* ---------- HEADER / NAV BAR ---------- */
.top-nav-bar {
    background: #000000;
    width: 100%;
    padding: 0.5rem 2rem; /* Reduced nav bar padding */
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

/* Spacing below the nav bar so content won't be hidden */
.body-space {
    margin-top: 60px;
}

/* ---------- HERO SECTION ---------- */
.hero-section {
    background: radial-gradient(circle at top left, #3b0066 0%, #0A0A0A 80%);
    padding: 2rem 2rem 3rem 2rem; /* decreased from 4rem/6rem to shorten */
    border-radius: 8px;
    text-align: center;
    margin-bottom: 3rem;
}
.hero-title {
    font-size: 2.2rem; /* decreased from 2.8rem */
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 1rem;
    line-height: 1.2;
}
.hero-subtitle {
    font-size: 1.1rem; /* decreased from 1.2rem */
    color: #d1d5db;
    margin-bottom: 2rem; /* decreased from 2.5rem */
}

/* ---------- INPUT SECTIONS ---------- */
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
.stTextArea label, .stTextInput label, .stSlider label {
    color: #ffffff !important; /* Force labels to be white in dark mode */
}
.stTextArea textarea, .stTextInput input {
    background: #ffffff;
    border-radius: 50px;
    border: 2px solid #555;
    padding: 15px 20px;
    width: 100% !important;
    box-shadow: none !important;
    transition: all 0.3s ease;
    outline: none !important;
}
.stTextArea textarea:focus, .stTextInput input:focus {
    border-color: #9F7AEA !important;
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

/* ---------- PROMPT BOX ---------- */
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
        font-size: 1.8rem;
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


# ----------------------------------------------------------------------------
#                              HERO SECTION
# ----------------------------------------------------------------------------
st.markdown("""
<div class="body-space"></div>
<div class="hero-section">
    <h1 class="hero-title">Your Story, Your Style—AI-Driven Comic Creation Made Simple.</h1>
    <p class="hero-subtitle">
        Visualize, communicate, and iterate on designs in minutes. 
        Just describe your scene, add a style, and let AI do the rest!
    </p>
</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------------------------------
#                          USER INPUTS + PANELS SLIDER
# ----------------------------------------------------------------------------
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

    # Number of panels to generate (the user can adjust as needed)
    num_panels = st.slider("Number of Strips", min_value=1, max_value=2, value=1)

# ----------------------------------------------------------------------------
#                         IMAGE GENERATION LOGIC
# ----------------------------------------------------------------------------
def generate_comic_images(prompt, n_images=1):
    """
    Generate 'n_images' from EdenAI using 'stabilityai'.
    Returns a list of image URLs.
    """
    url = "https://api.edenai.run/v2/image/generation"
    headers = {"Authorization": f"Bearer {edenai_api_key}"}
    payload = {
        "providers": "stabilityai",
        "text": prompt,
        "resolution": "1024x1024",
        "num_images": n_images
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        response_data = response.json()
        # stabilityai -> items -> each item has image_resource_url
        if "stabilityai" in response_data and "items" in response_data["stabilityai"]:
            items = response_data["stabilityai"]["items"]
            return [item["image_resource_url"] for item in items]
        return []
    except Exception as e:
        st.error(f"Error generating image: {str(e)}")
        return []

# ----------------------------------------------------------------------------
#                             GENERATE BUTTON
# ----------------------------------------------------------------------------
generate_button = st.button("Generate")

# ----------------------------------------------------------------------------
#                             MAIN APP LOGIC
# ----------------------------------------------------------------------------
if generate_button:
    if not SCENARIO.strip() or not STYLE.strip():
        st.warning("Please fill in both the scene description and style fields!")
    else:
        # Combine user scenario + style into a single prompt
        full_prompt = f"{SCENARIO}, {STYLE}"
        
        with st.spinner("Creating your masterpiece..."):
            # Generate multiple images at once
            image_urls = generate_comic_images(full_prompt, n_images=num_panels)

            # Display the prompt card
            st.markdown(f"""
            <div class="prompt-box">
                <h4>Prompt used for generation:</h4>
                <p>{full_prompt}</p>
            </div>
            """, unsafe_allow_html=True)

            if len(image_urls) == 0:
                st.error("Failed to generate image. Please try again with a different prompt.")
            else:
                # Display images side by side in a "comic strip"
                columns = st.columns(num_panels, gap="small")
                for i, img_url in enumerate(image_urls):
                    with columns[i]:
                        st.image(img_url, 
                                 caption=f"Panel {i+1}", 
                                 use_column_width=True)

# ----------------------------------------------------------------------------
#                                  FOOTER
# ----------------------------------------------------------------------------
st.markdown("""
<div class="footer">
    Created By Abhinav Abhishek
</div>
""", unsafe_allow_html=True)
