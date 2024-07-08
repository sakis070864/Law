import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# Set the page layout to centered
st.set_page_config(layout="centered")

# Function to convert image to base64
def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Load and resize the main image
main_image_path = "images/Screenshot_2024-06-04_232939-removebg-preview.png"
main_image = Image.open(main_image_path)
main_image = main_image.resize((180, 180))
main_img_str = image_to_base64(main_image)

# Load and resize the flag images
flag_size = (80, 80)  # Set the size as needed
danish_flag_path = "images/DanishFlag.png"
british_flag_path = "images/BritishFlag.png"

danish_flag = Image.open(danish_flag_path)
danish_flag = danish_flag.resize(flag_size)
danish_flag_str = image_to_base64(danish_flag)

british_flag = Image.open(british_flag_path)
british_flag = british_flag.resize(flag_size)
british_flag_str = image_to_base64(british_flag)

# HTML and CSS for layout
st.markdown(
    f"""
    <style>
    .container {{
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: -40px;
        position: relative;
    }}
    .main-image {{
        width: 180px;
        height: 180px;
        margin-left: -40px;
        margin-top: -20px;
    }}
    h3 {{
        margin-bottom: 0;
        position: relative;
    }}
    hr {{
        width: 250px;
        height: 3px;
        background-color: black;
        border: none;
        position: absolute;
        top: 172px;
        margin-left: -23px;
    }}
    .flags-container {{
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 80px;
    }}
    .flag-section {{
        text-align: center;
        margin: 10px 0;
    }}
    .flag-image {{
        width: 80px;
        height: 80px;
    }}
    .info-box {{
        font-size: 18px;
        position: relative;
        padding: 10px;
        border: 1px solid black;
        background-color: #f0f0f0;
        width: 100%;
        max-width: 480px;
        text-align: left;
        word-wrap: break-word;
        white-space: pre-wrap;
        overflow-wrap: break-word;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }}
    .danish-info {{
        min-height: 150px;
    }}
    .english-info {{
        min-height: 170px;
    }}
    .footer {{
        margin-top: 20px;
        text-align: center;
        color: gray;
    }}
    @media (min-width: 768px) {{
        .flags-container {{
            flex-direction: row;
            justify-content: center;
            align-items: flex-start;
        }}
        .flag-section {{
            margin: 0 20px;
        }}
        .info-box {{
            padding-left: 1em;
        }}
    }}
    .button-container {{
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }}
    .custom-button {{
        background-color: white;
        color: black;
        padding: 10px 20px;
        border: 2px solid black;
        border-radius: 5px;
        cursor: pointer;
        text-decoration: none;
        font-size: 16px;
    }}
    .custom-button:hover {{
        background-color: #f0f0f0;
    }}
    </style>

    <div class="container">
        <img src="data:image/png;base64,{main_img_str}" class="main-image" />
        <h3>Dansk Lov</h3>
        <h3>Danish Law</h3>
        <hr />
        <div class="button-container">
            <a href="https://youtu.be/tjge7oYNrn4" target="_blank" class="custom-button">Instruction Video</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Continue with the rest of the HTML and CSS code
st.markdown(
    f"""
    <div class="flags-container">
        <div class="flag-section">
            <a href="https://danishjura.streamlit.app" target="_blank">
                <img src="data:image/png;base64,{danish_flag_str}" class="flag-image" />
            </a>
            <div class="info-box danish-info">
                <p><b>Klik på flaget for at vælge et sprog</b></p>
                <p>Denne app er designet til at hjælpe advokater og jurastuderende med at udforske Danske juridiske paragraffer og relevante punkter relateret til deres forespørgsler. Ved at bruge denne app kan de bygge deres sager mere effektivt og opnå bedre resultater.</p>
            </div>
        </div>
        <div class="flag-section">
            <a href="https://danishlaw-en.streamlit.app" target="_blank">
                <img src="data:image/png;base64,{british_flag_str}" class="flag-image" />
            </a>
            <div class="info-box english-info">
                <p><b>Click on the flag to choose a language</b></p>
                <p>This app is designed to assist lawyers and law students in exploring Danish legal paragraphs and relevant points related to their inquiries. By using this app, they can build their cases more efficiently and achieve better results.</p>
            </div>
        </div>
    </div>
    <div class="footer">
        <p>This AI application is expertly designed and trained to serve as a legal expert in the Danish legal system, drawing from an extensive knowledge base of over one million pages</p>
        <p>Developed by Sakis Athan. For inquiries, please contact sakis@post.com.</p>
    </div>
    """,
    unsafe_allow_html=True
)
