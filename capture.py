import cv2
import streamlit as st

def capture_image():
    # Capture an image from the camera
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    camera.release()

    # Display the image in the Streamlit app
    st.image(frame)

if __name__ == "__main__":
    # Title of the app
    st.title("Capture Image from Camera")

    # Button to capture an image
    button = st.button("Capture Image")

    # If the button is clicked, capture an image and display it in the app
    if button:
        capture_image()
