"""
Source from here: https://github.com/lit26/streamlit-img-label/tree/main
"""
import streamlit as st
from streamlit_img_label.manage import ImageManager
from streamlit_img_label import st_img_label
from PIL import Image

def run(labels):
    st.set_option("deprecation.showfileUploaderEncoding", False)

    # Main content: annotate images
    uploaded_image = st.file_uploader("Upload images: ", type=['jpg', 'jpeg', 'png'])
    if uploaded_image is not None:
        # 轉換為PIL圖像物件
        # image = Image.open(uploaded_image)
        # st.image(image, use_column_width=True)
        filename = uploaded_image.name
        st.write(filename)
        st.session_state["annotation_files"] = []
        # 顯示上傳的圖片
        im = ImageManager(uploaded_image, filename)

        img = im.get_img()
        resized_img = im.resizing_img()
        resized_rects = im.get_resized_rects()
        rects = st_img_label(resized_img, box_color="red", rects=resized_rects)

        def annotate():
            im.save_annotation()
            image_annotate_file_name = filename.split(".")[0] + ".xml"
            if image_annotate_file_name not in st.session_state["annotation_files"]:
                st.session_state["annotation_files"].append(image_annotate_file_name)

        if rects:
            st.button(label="Save", on_click=annotate)
            preview_imgs = im.init_annotation(rects)
            # st.write(rects)

            for i, prev_img in enumerate(preview_imgs):
                prev_img[0].thumbnail((200, 200))
                col1, col2 = st.columns(2)
                with col1:
                    col1.image(prev_img[0])
                with col2:
                    default_index = 0
                    if prev_img[1]:
                        default_index = labels.index(prev_img[1])

                    select_label = col2.selectbox(
                        "Label", labels, key=f"label_{i}", index=default_index
                    )
                    im.set_annotation(i, select_label)

if __name__ == "__main__":
    custom_labels = ["", "dog", "cat"]
    run(custom_labels)