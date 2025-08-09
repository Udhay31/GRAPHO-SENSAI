import streamlit as st
import google.generativeai as genai
from PIL import Image
import numpy as np

genai.configure(api_key="AIzaSyBO7KrIAQdIo2FXbYgciKIvBYrCUval1qc")
model = genai.GenerativeModel("gemini-1.5-flash")

st.title("GRAPHO SENSAI 🧠")
st.subheader(" - Mental Health Checker Using Handwriting Samples")
st.write("Upload A Signature Image The Ai is Ready To Describe The Soul Of Your Handwritting.")

uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image",width=365)
    
    img_array = np.array(image)

    prompt = (
        "Analyze the following signature sample to detect potential mental health indicators "
        "such as stress, anxiety, depression, or emotional stability. Consider factors like pressure, "
        "slant, size, spacing, and legibility. Return a brief analysis of the individual's possible mental state "
        "based on handwriting psychology and signature features."
    )

    response = model.generate_content([prompt, image])
    
    st.subheader("🧠 Grapho SensAI's Answer")
    st.write(response.text)
else:
    st.info("Please upload an image to begin.")