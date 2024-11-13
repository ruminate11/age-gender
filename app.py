import streamlit as st
import cv2
import numpy as np
import base64
from detect import detect_gender_age  # Import the detect_gender_age function from detect.py

# Streamlit App
st.title("Age and Gender Detection")

# Image upload widget
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Convert the uploaded image into a format OpenCV can work with
    file_bytes = uploaded_file.read()
    np_arr = np.frombuffer(file_bytes, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    # Process the image with the detect_gender_age function
    processed_img, results = detect_gender_age(img)

    # Display the results
    st.image(processed_img, channels="BGR", caption="Processed Image")
    
    # Show the results (age, gender)
    for result in results:
        st.write(result)

