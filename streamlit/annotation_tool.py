import streamlit as st
import numpy as np
from PIL import Image

# st.set_option('deprecation.showfileUploaderEncoding', False)
# img_file_buffer = st.file_uploader("Upload an image")
# if img_file_buffer is not None:
#     image = Image.open(img_file_buffer)
#     img_array = np.array(image) # if you want to pass it to OpenCV
#     st.image(image, caption="The caption", use_column_width=True)
    
import streamlit.components.v1 as components

max_width = st.sidebar.slider("Adjust max width of page:", 400, 1800, 1300, 100)
max_height = st.sidebar.slider("Adjust max height of page:", 800, 2000, 1300, 100)
st.markdown(
f"""
<style>
    .reportview-container .main .block-container{{
        max-width: {max_width}px;
        padding-top: 5 rem;
    }}
</style>
""",
        unsafe_allow_html=True,
    )
st.markdown("# Annotation area \n Here is a simple online annotation area.")

HtmlFile = open("via_face_demo.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
components.html(source_code,  height = max_height)