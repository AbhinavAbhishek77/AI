# import os
# import json
# from comic_generation.generate_panels import generate_panels
# from comic_generation.stability_ai import text_to_image
# from comic_generation.add_text import add_text_to_panel
# from comic_generation.create_strip import create_strip
# import streamlit as st
# from PIL import Image

# api_key = os.getenv("OPENAI_API_KEY")
# stability_api_key=os.getenv("STABILITY_KEY")

# if api_key is None:
#     raise ValueError(
#         "OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")

# favicon = Image.open("favicon.png")


# st.set_page_config(
#     page_title="GenAI Demo | Trigent AXLR8 Labs",
#     page_icon=favicon,
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# logo_html = """
# <style>
#     [data-testid="stSidebarNav"] {
#         background-image: url(https://trigent.com/wp-content/uploads/Trigent_Axlr8_Labs.png);
#         background-repeat: no-repeat;
#         background-position: 20px 20px;
#         background-size: 80%;
#     }
# </style>
# """
# st.sidebar.markdown(logo_html, unsafe_allow_html=True)
# st.title("Provide your story and wait for your comic. 😀")

# if api_key:
#     success_message_html = """
#     <span style='color:green; font-weight:bold;'>✅ Powering the Chatbot using Open AI's 
#     <a href='https://platform.openai.com/docs/models/gpt-3-5' target='_blank'>gpt-3.5-turbo-0613 model</a>!</span>
#     """

#     # Display the success message with the link
#     st.markdown(success_message_html, unsafe_allow_html=True)
#     openai_api_key = api_key
# else:
#     openai_api_key = st.text_input(
#         'Enter your OPENAI_API_KEY: ', type='password')
#     if not openai_api_key:
#         st.warning('Please, enter your OPENAI_API_KEY', icon='⚠️')
#         stop = True
#     else:
#         st.success('Get your comic ready in minutes!', icon='👉')


# SCENARIO = st.text_area(
#     "Enter your Story and the characters",
#     """Characters: A IT industry Manager named Andy and Couple of Software developers with a Laptop.
# The manager is a super guy who manages all his Developers.
# Once there was a super powerful task which the  manager  assigned to on of his new developers and the developer was able to do it and the Manager was amazed and awarded him with a USA ticket.""",
# )

# STYLE = st.text_input("Enter the style of your characters", "Indian comic, coloured")
# if st.button("Generate"):
#     with st.spinner("Making a comic for you..."):
#         print(f"Generate panels with style '{STYLE}' for this scenario: \n {SCENARIO}")

#         panels = generate_panels(SCENARIO)

#         with open("output/panels.json", "w") as outfile:
#             json.dump(panels, outfile)

#         panel_images = []

#         for panel in panels:
#             panel_prompt = panel["description"] + ", cartoon box, " + STYLE
#             textData = f"Generate panel {panel['number']} with prompt: {panel_prompt}"
#             st.markdown(textData)
#             panel_image = text_to_image(panel_prompt)
#             panel_image_with_text = add_text_to_panel(panel["text"], panel_image)
#             panel_images.append(panel_image_with_text)

#         res = create_strip(panel_images)
#         st.image(res)



# # Footer
# footer_html = """
# <div style="text-align: right; margin-right: 10%;">
#     <p>
#         Copyright © 2024, Trigent Software, Inc. All rights reserved. | 
#         <a href="https://www.facebook.com/TrigentSoftware/" target="_blank">Facebook</a> |
#         <a href="https://www.linkedin.com/company/trigent-software/" target="_blank">LinkedIn</a> |
#         <a href="https://www.twitter.com/trigentsoftware/" target="_blank">Twitter</a> |
#         <a href="https://www.youtube.com/channel/UCNhAbLhnkeVvV6MBFUZ8hOw" target="_blank">YouTube</a>
#     </p>
# </div>
# """

# # Custom CSS to make the footer sticky
# footer_css = """
# <style>
# .footer {
#     position: fixed;
#     z-index: 1000;
#     left: 0;
#     bottom: 0;
#     width: 100%;
#     background-color: white;
#     color: black;
#     text-align: center;
# }
# </style>
# """


# footer = f"{footer_css}<div class='footer'>{footer_html}</div>"

# # Rendering the footer
# st.markdown(footer, unsafe_allow_html=True)




# import os
# import json
# import requests
# from dotenv import load_dotenv
# import streamlit as st
# from PIL import Image

# # Load environment variables
# load_dotenv()
# edenai_api_key = os.getenv("EDENAI_API_KEY")

# if edenai_api_key is None:
#     raise ValueError("EdenAI API key not found. Please set the EDENAI_API_KEY environment variable.")

# favicon = Image.open("favicon.png")

# st.set_page_config(
#     page_title="GenAI Demo | Trigent AXLR8 Labs",
#     page_icon=favicon,
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Sidebar Logo
# logo_html = """
# <style>
#     [data-testid="stSidebarNav"] {
#         background-image: url(https://trigent.com/wp-content/uploads/Trigent_Axlr8_Labs.png);
#         background-repeat: no-repeat;
#         background-position: 20px 20px;
#         background-size: 80%;
#     }
# </style>
# """
# st.sidebar.markdown(logo_html, unsafe_allow_html=True)
# st.title("Provide your story and wait for your comic. 😀")

# SCENARIO = st.text_area(
#     "Enter your Story and the characters",
#     """Characters: A IT industry Manager named Andy and a Couple of Software developers with a Laptop.
# The manager is a super guy who manages all his Developers.
# Once there was a super powerful task which the manager assigned to one of his new developers, and the developer was able to do it. The Manager was amazed and awarded him with a USA ticket.""",
# )

# STYLE = st.text_input("Enter the style of your characters", "Indian comic, coloured")

# # Function to generate an image using EdenAI API
# def generate_comic_image(prompt):
#     url = "https://api.edenai.run/v2/image/generation"
#     headers = {"Authorization": f"Bearer {edenai_api_key}"}
#     payload = {
#         "providers": "stabilityai",  # You can use "openai" or other providers if needed
#         "text": prompt,
#         "resolution": "1024x1024",
#         "num_images": 1
#     }

#     response = requests.post(url, headers=headers, json=payload)
#     response_data = response.json()

#     if "stabilityai" in response_data and "items" in response_data["stabilityai"]:
#         image_url = response_data["stabilityai"]["items"][0]["image_resource_url"]
#         return image_url
#     else:
#         return None

# if st.button("Generate"):
#     with st.spinner("Making a comic for you..."):
#         st.write(f"Generating panels with style '{STYLE}' for this scenario: \n {SCENARIO}")

#         panels = [
#             {"number": 1, "description": "Manager assigning a tough task to the developer", "text": "Can you complete this challenging task?"},
#             {"number": 2, "description": "Developer working hard on the laptop", "text": "This is really tough, but I will do it!"},
#             {"number": 3, "description": "Developer successfully completing the task", "text": "Done!"},
#             {"number": 4, "description": "Manager awarding the developer a USA ticket", "text": "You did an amazing job!"}
#         ]

#         panel_images = []

#         for panel in panels:
#             panel_prompt = panel["description"] + ", cartoon box, " + STYLE
#             textData = f"Generating panel {panel['number']} with prompt: {panel_prompt}"
#             st.markdown(textData)

#             panel_image_url = generate_comic_image(panel_prompt)

#             if panel_image_url:
#                 panel_images.append(panel_image_url)
#                 st.image(panel_image_url, caption=f"Panel {panel['number']}")
#             else:
#                 st.error(f"Failed to generate image for panel {panel['number']}")

# # Footer
# footer_html = """
# <div style="text-align: right; margin-right: 10%;">
    
#         Abhinav Abhishek
       
   
# </div>
# """

# footer_css = """
# <style>
# .footer {
#     position: fixed;
#     left: 0;
#     bottom: 0;
#     width: 100%;
#     background-color: white;
#     color: black;
#     text-align: center;
# }
# </style>
# """

# footer = f"{footer_css}<div class='footer'>{footer_html}</div>"
# st.markdown(footer, unsafe_allow_html=True)





# import os
# import json
# import requests
# from dotenv import load_dotenv
# import streamlit as st
# from PIL import Image

# # Load environment variables
# load_dotenv()
# edenai_api_key = os.getenv("EDENAI_API_KEY")

# if edenai_api_key is None:
#     raise ValueError("EdenAI API key not found. Please set the EDENAI_API_KEY environment variable.")

# favicon = Image.open("favicon.png")

# st.set_page_config(
#     page_title="GenAI Demo | Trigent AXLR8 Labs",
#     page_icon=favicon,
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Sidebar Logo
# logo_html = """
# <style>
#     [data-testid="stSidebarNav"] {
#         background-image: url(https://trigent.com/wp-content/uploads/Trigent_Axlr8_Labs.png);
#         background-repeat: no-repeat;
#         background-position: 20px 20px;
#         background-size: 80%;
#     }
# </style>
# """
# # st.sidebar.markdown(logo_html, unsafe_allow_html=True)

# # Custom CSS Styling
# st.markdown("""
# <style>
#     /* Main Container */
#     .stApp {
#         background: #f0f2f6;
#         padding-bottom: 100px;
#     }

#     /* Header */
#     h1 {
#         color: #2a3f5f;
#         font-family: 'Helvetica Neue', sans-serif;
#         font-size: 2.5em;
#         text-align: center;
#         margin-bottom: 30px;
#         text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
#     }

#     /* Input Fields */
#     .stTextArea textarea, .stTextInput input {
#         background: #ffffff !important;
#         border-radius: 15px !important;
#         border: 2px solid #e0e0e0 !important;
#         padding: 15px !important;
#         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
#         transition: all 0.3s ease !important;
#     }

#     .stTextArea textarea:focus, .stTextInput input:focus {
#         border-color: #667eea !important;
#         box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.2) !important;
#     }

#     /* Generate Button */
#     .stButton>button {
#         background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#         color: white !important;
#         border-radius: 12px !important;
#         padding: 12px 30px !important;
#         font-weight: bold !important;
#         border: none !important;
#         transition: transform 0.3s ease;
#         width: 100%;
#         margin-top: 20px;
#     }

#     .stButton>button:hover {
#         transform: scale(1.05);
#         box-shadow: 0 8px 15px rgba(102, 126, 234, 0.3);
#     }

#     /* Comic Panels */
#     .stImage {
#         border-radius: 20px;
#         overflow: hidden;
#         box-shadow: 0 10px 20px rgba(0,0,0,0.1);
#         transition: transform 0.3s ease;
#         margin: 20px 0;
#         border: 3px solid white;
#     }

#     .stImage:hover {
#         transform: translateY(-5px);
#     }

#     /* Footer */
#     .footer {
#         background: #2a3f5f !important;
#         padding: 15px !important;
#         color: white !important;
#         position: relative;
#         bottom: 0;
#         width: 100%;
#     }

#     .footer a {
#         color: #a3b8ff !important;
#         text-decoration: none !important;
#         margin: 0 10px;
#         transition: color 0.3s ease;
#     }

#     .footer a:hover {
#         color: #ffffff !important;
#         text-decoration: underline !important;
#     }

#     /* Responsive Design */
#     @media (max-width: 768px) {
#         h1 {
#             font-size: 2em;
#         }
#         .stImage {
#             margin: 10px 0;
#         }
#     }
# </style>
# """, unsafe_allow_html=True)

# # Main Content
# st.title("📖 Your Imagination, Our AI—Let's Create Magic! 😀")

# SCENARIO = st.text_area(
#     "✏️Describe your scene and let AI do the rest!",
#     """""",
#     height=200
# )

# STYLE = st.text_input("🖌️ Realistic, cartoonish, or abstract? Define your world!", "")

# # Function to generate an image using EdenAI API (Unchanged)
# def generate_comic_image(prompt):
#     url = "https://api.edenai.run/v2/image/generation"
#     headers = {"Authorization": f"Bearer {edenai_api_key}"}
#     payload = {
#         "providers": "stabilityai",
#         "text": prompt,
#         "resolution": "1024x1024",
#         "num_images": 1
#     }

#     response = requests.post(url, headers=headers, json=payload)
#     response_data = response.json()

#     if "stabilityai" in response_data and "items" in response_data["stabilityai"]:
#         image_url = response_data["stabilityai"]["items"][0]["image_resource_url"]
#         return image_url
#     else:
#         return None
    


# if st.button("Generate Comic"):
#     with st.spinner("Making a comic for you..."):
#         # st.write(f"Generating panels with style '{STYLE}' for this scenario: \n {SCENARIO}")

#         panels = [
#             {"number": 1, "description": "Manager assigning a tough task to the developer", "text": "Can you complete this challenging task?"},
#             # {"number": 2, "description": "Developer working hard on the laptop", "text": "This is really tough, but I will do it!"},
#             # {"number": 3, "description": "Developer successfully completing the task", "text": "Done!"},
#             # {"number": 4, "description": "Manager awarding the developer a USA ticket", "text": "You did an amazing job!"}
#         ]

#         panel_images = []

#         for panel in panels:
#             panel_prompt = panel["description"] + ", cartoon box, " + STYLE
#             textData = f"Generating Images with prompt: {panel_prompt}"
#             st.markdown(f"<h3 style='color: #2a3f5f; margin: 20px 0;'>{textData}</h3>", unsafe_allow_html=True)

#             panel_image_url = generate_comic_image(panel_prompt)

#             if panel_image_url:
#                 panel_images.append(panel_image_url)
#                 st.image(panel_image_url, caption=f"Panel {panel['number']}")
#             else:
#                 st.error(f"Failed to generate image for panel {panel['number']}")

# # ... (keep all previous imports and setup code the same)

# # Footer
# footer_html = """
# <div class="footer">
#     Created By Abhinav Abhishek
# </div>
# """

# st.markdown(footer_html, unsafe_allow_html=True)








# import os
# import json
# import requests
# from dotenv import load_dotenv
# import streamlit as st
# from PIL import Image

# # Load environment variables
# load_dotenv()
# edenai_api_key = os.getenv("EDENAI_API_KEY")

# if edenai_api_key is None:
#     raise ValueError("EdenAI API key not found. Please set the EDENAI_API_KEY environment variable.")

# favicon = Image.open("favicon.png")

# st.set_page_config(
#     page_title="GenAI Demo | Trigent AXLR8 Labs",
#     page_icon=favicon,
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Custom CSS Styling
# st.markdown("""
# <style>
#     /* Main Container */
#     .stApp {
#         background: #f0f2f6;
#         padding-bottom: 100px;
#     }

#     /* Header */
#     h1 {
#         color: #2a3f5f;
#         font-family: 'Helvetica Neue', sans-serif;
#         font-size: 2.5em;
#         text-align: center;
#         margin-bottom: 30px;
#         text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
#     }

#     /* Input Fields */
#     .stTextArea textarea, .stTextInput input {
#         background: #ffffff !important;
#         border-radius: 15px !important;
#         border: 2px solid #e0e0e0 !important;
#         padding: 15px !important;
#         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
#         transition: all 0.3s ease !important;
#     }

#     .stTextArea textarea:focus, .stTextInput input:focus {
#         border-color: #667eea !important;
#         box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.2) !important;
#     }

#     /* Generate Button */
#     .stButton>button {
#         background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#         color: white !important;
#         border-radius: 12px !important;
#         padding: 12px 30px !important;
#         font-weight: bold !important;
#         border: none !important;
#         transition: transform 0.3s ease;
#         width: 100%;
#         margin-top: 20px;
#     }

#     .stButton>button:hover {
#         transform: scale(1.05);
#         box-shadow: 0 8px 15px rgba(102, 126, 234, 0.3);
#     }

#     /* Image Display */
#     .stImage {
#         border-radius: 20px;
#         overflow: hidden;
#         box-shadow: 0 10px 20px rgba(0,0,0,0.1);
#         transition: transform 0.3s ease;
#         margin: 20px 0;
#         border: 3px solid white;
#     }

#     /* Footer */
#     .footer {
#         background: #2a3f5f !important;
#         padding: 15px !important;
#         color: white !important;
#         position: relative;
#         bottom: 0;
#         width: 100%;
#     }

#     .footer a {
#         color: #a3b8ff !important;
#         text-decoration: none !important;
#         margin: 0 10px;
#         transition: color 0.3s ease;
#     }
# </style>
# """, unsafe_allow_html=True)

# # Main Content
# st.title("📖 Your Imagination, Our AI—Let's Create Magic! 😀")

# SCENARIO = st.text_area(
#     "✏️Describe your scene and let AI do the rest!",
#     height=200,
#     placeholder="Example: A mystical forest with glowing mushrooms under a twilight sky..."
# )

# STYLE = st.text_input(
#     "🖌️ Realistic, cartoonish, or abstract? Define your world!",
#     placeholder="Example: fantasy watercolor painting style"
# )

# def generate_comic_image(prompt):
#     url = "https://api.edenai.run/v2/image/generation"
#     headers = {"Authorization": f"Bearer {edenai_api_key}"}
#     payload = {
#         "providers": "stabilityai",
#         "text": prompt,
#         "resolution": "1024x1024",
#         "num_images": 1
#     }

#     try:
#         response = requests.post(url, headers=headers, json=payload)
#         response.raise_for_status()
#         response_data = response.json()
        
#         if "stabilityai" in response_data and "items" in response_data["stabilityai"]:
#             return response_data["stabilityai"]["items"][0]["image_resource_url"]
#         return None
#     except Exception as e:
#         st.error(f"Error generating image: {str(e)}")
#         return None

# if st.button("Generate Image"):
#     if not SCENARIO.strip() or not STYLE.strip():
#         st.warning("Please fill in both the scene description and style fields!")
#     else:
#         with st.spinner("Creating your masterpiece..."):
#             full_prompt = f"{SCENARIO}, {STYLE}"
            
#             # Display prompt
#             st.markdown(f"""
#             <div style='background: #f8f9fa; padding: 15px; border-radius: 10px; margin: 15px 0;'>
#                 <h4 style='color: #2a3f5f; margin: 0;'>Generating Image with prompt:</h4>
#                 <p style='color: #4a5568; margin: 10px 0 0 0;'>{full_prompt}</p>
#             </div>
#             """, unsafe_allow_html=True)

#             # Generate and display image
#             image_url = generate_comic_image(full_prompt)
            
#             if image_url:
#                 st.image(image_url, 
#                         caption="Your Custom Creation",
#                         use_column_width=True)
#             else:
#                 st.error("Failed to generate image. Please try again with a different prompt.")


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

favicon = Image.open("favicon.png")

# Streamlit page configuration
st.set_page_config(
    page_title="GenAI Demo | Trigent AXLR8 Labs",
    page_icon=favicon,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for a sleek UI
st.markdown("""
<style>
    /* Main Container */
    .stApp {
        background: linear-gradient(135deg, #f0f2f6 0%, #e2e8f0 100%);
        padding-bottom: 100px;
        font-family: "Helvetica Neue", sans-serif;
    }

    /* Header Title */
    h1 {
        color: #2a3f5f;
        text-align: center;
        margin-bottom: 30px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }

    /* Text Area & Text Input */
    .stTextArea textarea, .stTextInput input {
        background: #ffffff !important;
        border-radius: 15px !important;
        border: 2px solid #e0e0e0 !important;
        padding: 15px !important;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease !important;
    }
    .stTextArea textarea:focus, .stTextInput input:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.2) !important;
    }

    /* Generate Button */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white !important;
        border-radius: 12px !important;
        padding: 12px 30px !important;
        font-weight: bold !important;
        border: none !important;
        transition: transform 0.3s ease, box-shadow 0.3s ease !important;
        width: 100%;
        margin-top: 20px;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 15px rgba(102, 126, 234, 0.3);
    }

    /* Generated Image */
    .stImage {
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
        margin: 20px 0;
        border: 3px solid white;
    }
    .stImage:hover {
        transform: scale(1.01);
    }

    /* Footer */
    .footer {
        background: #2a3f5f !important;
        padding: 15px !important;
        color: white !important;
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
    }
    .footer a {
        color: #a3b8ff !important;
        text-decoration: none !important;
        margin: 0 10px;
        transition: color 0.3s ease;
    }
    .footer a:hover {
        color: #fff !important;
    }
</style>
""", unsafe_allow_html=True)

# App Title
st.title("📖 Your Imagination, Our AI—Let's Create Magic! 😀")

# Two-column layout for prompts
col1, col2 = st.columns(2)

with col1:
    SCENARIO = st.text_area(
        "✏️Describe your scene and let AI do the rest!",
        height=200,
        placeholder="Example: A mystical forest with glowing mushrooms under a twilight sky..."
    )

with col2:
    STYLE = st.text_input(
        "🖌️ Realistic, cartoonish, or abstract? Define your world!",
        placeholder="Example: fantasy watercolor painting style"
    )

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

# Generate Image Button
if st.button("Generate Image"):
    if not SCENARIO.strip() or not STYLE.strip():
        st.warning("Please fill in both the scene description and style fields!")
    else:
        with st.spinner("Creating your masterpiece..."):
            full_prompt = f"{SCENARIO}, {STYLE}"
            
            st.markdown(f"""
            <div style='background: #f8f9fa; padding: 15px; border-radius: 10px; margin: 15px 0;'>
                <h4 style='color: #2a3f5f; margin: 0;'>Generating Image with prompt:</h4>
                <p style='color: #4a5568; margin: 10px 0 0 0;'>{full_prompt}</p>
            </div>
            """, unsafe_allow_html=True)

            image_url = generate_comic_image(full_prompt)
            
            if image_url:
                st.image(
                    image_url,
                    caption="Your Custom Creation",
                    use_column_width=True
                )
            else:
                st.error("Failed to generate image. Please try again with a different prompt.")


# Footer
st.markdown("""
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #f1f1f1;
            color: #333;
            text-align: center;
            padding: 10px;
            font-size: 16px;
            font-weight: bold;
            box-shadow: 0px -2px 5px rgba(0, 0, 0, 0.1);
        }
        .footer a {
            color: #007BFF;
            text-decoration: none;
        }
        .footer a:hover {
            text-decoration: underline;
        }
    </style>
    <div class="footer">
        <p class="footer-text">
            Made with <span style="color: #e25555;">♥</span> by
            <a href="https://github.com/AbhinavAbhishek77/AI-Comic-Strip-Creator" target="_blank">Abhinav Abhishek</a>
            @ <span class="highlight">National Institute of Technology Agartala</span>
        </p>
    </div>
""", unsafe_allow_html=True)