import streamlit as st
from io import BytesIO
from PIL import Image
from rembg import remove
from cartooner import cartoonize
import numpy as np

st.set_page_config(layout="wide", page_title="Image Background Remover")
st.write("# Remove Background From Images")
st.write("Upload an image and see the background disappear like magic!")

st.sidebar.write("## Upload and Download :gear:")
my_upload = st.sidebar.file_uploader("Upload an Image", type=["png", "jpg", "jpeg", "gif", "bmp", "webp", "tiff"])
alpha_matting = st.sidebar.checkbox("Use Alpha Matting", value=True)
threshold = st.sidebar.slider("Background Removal Threshold", 0, 255, step=50)

def convert_images(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

def remove_bg(my_upload, threshold, alpha_matting):
    image = Image.open(my_upload)
    col1, col2 = st.columns(2)
    col1.write("Original Image :camera:")
    col1.image(image)
    col2.write("Fixed Image :ok_hand:")
    fixed = remove(image, alpha_matting=alpha_matting, alpha_matting_foreground_threshold=threshold)
    col2.image(fixed)

    st.write("# Cartoonize Image")

    # Debugging: print the shape of the image before cartoonizing
    print("Image shape before cartoonizing:", image.size)

    cartoon = cartoonize(image)

    # Debugging: print the shape of the cartoonized image
    print("Cartoonized image shape:", cartoon.shape)

    img = Image.fromarray(cartoon)
    st.image(img)
    st.sidebar.download_button("Download Fixed Image", convert_images(fixed), "fixed.png", "image/png")
    st.sidebar.download_button("Download Cartoonized Image", convert_images(img), "cartoon.png", "image/png")

if my_upload:
    remove_bg(my_upload, threshold, alpha_matting)
else:
    remove_bg("./images/cat.jpg", threshold, alpha_matting)

st.snow()
st.balloons()
