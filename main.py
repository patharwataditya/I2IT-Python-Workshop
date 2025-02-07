import numpy as np
import pandas as pd
import streamlit as st

st.title("Welcome Everyone we are learning Python")
st.write("Python Requires Practice!!!")

data = pd.DataFrame({'c1':[10, 20, 30, 40], 'c2':['A', 'B', 'C', 'D']})

st.write("Below is Table for Data")
st.write(data)

st.write("Nilya BSDK")
chart_data = pd.DataFrame(np.random.randn(20,3),
                          columns=['A','B','C'])

st.bar_chart(chart_data)
