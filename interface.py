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

# Adding the script to the Streamlit app
st.markdown(
    f"""
    <div style="display: flex; justify-content: center; align-items: center; flex-direction: column; margin-top: -40px; position: relative;">
        <img src="data:image/png;base64,{main_img_str}" style="width: 180px; height: 180px; margin-left: -40px; margin-top: -20px;" />
        <h3 style="margin-bottom: 0; position: relative;">Dansk Lov - Danish Law</h3>
        <hr style="width: 250px; height: 3px; background-color: black; border: none; position: absolute; top: 172px; margin-left: -23px;" />
        <div style="display: flex; justify-content: center; align-items: flex-start; margin-top: 80px;">
            <div style="text-align: center; margin-right: 20px;">
                <div style="margin-bottom: 10px; position: relative; top: -160px; left: -3ch;">
                    <a href="https://danishjura.streamlit.app" target="_blank">
                        <img src="data:image/png;base64,{danish_flag_str}" style="width: 80px; height: 80px;" />
                    </a>
                </div>
                <div style="font-size: 18px; position: relative; top: -140px; padding-left: 12ch; border: 1px solid black; user-select: none; background-color: #f0f0f0; padding: 10px; width: 480px;">
                    <p style="margin-bottom: 0;"><b>Klik på flaget for at vælge et sprog</b></p>
                    <p style="margin-top: 0;">Denne app er designet til at hjælpe advokater og jurastuderende med at udforske Danske juridiske paragraffer og relevante punkter relateret til deres forespørgsler. Ved at bruge denne app kan de bygge deres sager mere effektivt og opnå bedre resultater.</p>
                </div>
            </div>
            <div style="text-align: center; margin-left: 20px;">
                <div style="margin-bottom: 10px; position: relative; top: -160px;">
                    <a href="https://danishlaw-en.streamlit.app" target="_blank">
                        <img src="data:image/png;base64,{british_flag_str}" style="width: 80px; height: 80px;" />
                    </a>
                </div>
                <div style="font-size: 18px; position: relative; top: -140px; padding-left: 12ch; border: 1px solid black; user-select: none; background-color: #f0f0f0; padding: 10px; width: 480px;">
                    <p style="margin-bottom: 0;"><b>Click on the flag to choose a language</b></p>
                    <p style="margin-top: 0;">This app is designed to assist lawyers and law students in exploring Danish legal paragraphs and relevant points related to their inquiries. By using this app, they can build their cases more efficiently and achieve better results.</p>
                </div>
            </div>
        </div>
        <div style="margin-top: -120px; text-align: center; color: gray;">
            <p>This AI application is expertly designed and trained to serve as a legal expert in the Danish legal system, drawing from an extensive knowledge base of over one million pages</p>
            <p>Developed by Sakis Athan. For inquiries, please contact sakis@post.com."</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
