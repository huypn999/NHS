import streamlit as st
import cv2

# Initialize the camera
camera = cv2.VideoCapture(0)

# Create a button to capture an image
st.button("Capture Image")

# If the button is clicked, capture an image and display it
if st.button_clicked("Capture Image"):
    # Capture an image from the camera
    ret, frame = camera.read()

    # Convert the image to a NumPy array
    image = frame.astype(np.uint8)

    # Display the image
    st.image(image)

# Close the camera
camera.release()