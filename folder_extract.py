import streamlit as st
from PIL import Image
import io
import numpy as np
import base64
import cv2
from copy import copy
# from visualize_box import visualize_box
import pandas as pd
import requests
import json
import os

def name():
    st.markdown("Enter full name:")
    # Folder input widget
    full_name = st.text_input("Full name:", 'Nick James Ye')
    if not full_name:
        st.warning('Name is not inputted correctly')
    else:
        st.write(f'Full Name:; {full_name}')

def ic_num():
    st.markdown('IC Number:')
    if st.button('Enter full IC number'):
        ic_num = st.text_input('IC Number:', '123456-78-1119')
        st.markdown('IC number is', ic_num)

def read_image(file_path):
    try:
        image = Image.open(file_path)
        return image
    except:
        st.warning(f'Unable to process the file given at: {file_path}')

"""
file = open('hi.txt', 'r')
content = file.read()
file.close()

with open('hi.txt', 'r') as file:
    content = file.read()

"""

def read_image_cv2(file_path):
    return cv2.imread(file_path)

def extract_images_from_folder(folder_path):
    valid_extensions = (".jpg", ".jpeg", ".png")
    images = []
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path) and file_path.lower().endswith(valid_extensions):
            img = read_image(file_path)
            print(img)
            images.append(img)
    return images

def main():
    st.title("Folder Image Extraction")
    # Folder input widget
    folder_path = st.text_input("Enter folder path:", 'D:\\Wallpaper')
    
    # Extract images button
    if st.button("Extract Images"):
        if os.path.isdir(folder_path):
            images = extract_images_from_folder(folder_path)
            st.markdown(f"**{len(images)} image(s) extracted**")
            st.session_state.preview_images = images
        else:
            st.warning("Invalid folder path.")
    
    # Preview button
    preview_images = st.session_state.get('preview_images', [])
    if st.button('Preview Images') and preview_images:
        for i, image in enumerate(preview_images):
            st.image(image, caption=f"Image {i+1}", use_column_width=True)

if __name__ == "__main__":
    main()