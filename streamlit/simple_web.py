"""
Author: Chieh
"""

import streamlit as st
st.set_option('deprecation.showfileUploaderEncoding', False)

if __name__ == '__main__':
    # Title
    st.title('Simple web page')

    st.write("Here are some basic features for streamlit")
    st.write("You can check out more features from webside https://docs.streamlit.io/library/api-reference")
    st.write("Choosing features depend on your purpose.")
    st.write("BTW streamlit does support markdown language.")

    st.markdown("---")
    a = st.button("It is a trigger button")
    if a:
        st.wrtie("success.")

    b = st.slider("It is a slider.", 0, 130, 25)
    st.write(b)


    st.write("Upload a file to server side")
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        st.write(bytes_data)

        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        st.write(stringio)

        # To read file as string:
        string_data = stringio.read()
        st.write(string_data)

        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)


    number = st.number_input('Insert a number')
    st.write('The current number is ', number)

    title = st.text_input('Movie title', 'Life of Brian')
    st.write('The current movie title is', title)


    genre = st.radio(
        "What's your favorite movie genre",
        ('Comedy', 'Drama', 'Documentary'))

    if genre == 'Comedy':
        st.write('You selected comedy.')
    else:
        st.write("You didn't select comedy.")

    agree = st.checkbox('I agree')

    if agree:
        st.write('Great!')

    st.warning('This is a warning')


    ## Of course, you can put on the sidebe

    side_button = st.sidebar.button("The button on the sidebar")
    st.sidebar.write("Result: ", side_button)