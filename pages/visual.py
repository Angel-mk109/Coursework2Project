import streamlit as st
import pandas as pd
import numpy as np

data = pd.DataFrame(
np.random.randn(20,3),
 columns=['x','y','z']
)


data = pd.DataFrame(
np.random.randn(25,3),
 columns=['a','b','c']
)

col1, col2 = st.columns(2)

with col1:
 st.subheader("Line Chart")
 st.line_chart(data)

with col2:
 st.subheader("Area Chart")
 st.area_chart(data)
