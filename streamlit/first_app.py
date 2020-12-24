"""
Source from : https://docs.streamlit.io/en/latest/getting_started.html#set-up-your-virtual-environment
"""

import streamlit as st
import numpy as np
import pandas as pd

# Title
st.title('My first app')

st.write("Here's our first attempt at using data to create a table:")

st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

st.write("Draw a line chart")

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.write("Plot a map")

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

# Use checkboxes to show/hide data
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

# Use a selectbox for options
# option = st.selectbox(
#     'Which number do you like best?',
#      df['first column'])

# 'You selected: ', option

