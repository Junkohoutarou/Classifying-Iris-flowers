import streamlit as st
import pickle as pkl
from PIL import Image
import numpy as np

class_list = {'0': 'Setosa', '1': 'Versicolor', '2': 'Virginica'}
with open("styles.css") as f:
    custom_css = f.read()
st.title('Iris classification based on sepal and petal size')
st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)

st.image("image.jpg", use_column_width=True)
input = open('lrc_iris.pkl', 'rb')
model = pkl.load(input)

st.header('Choose the size of sepal and petal size')

sepal_length = st.slider('Sepal length (cm)', 0.0, 20.0, 0.0, 0.1)
sepal_width = st.slider('Sepal width (cm)', 0.0, 20.0, 0.0, 0.1)
petal_length = st.slider('Petal length (cm)', 0.0, 20.0, 0.0, 0.1)
petal_width = st.slider('Petal width (cm)', 0.0, 20.0, 0.0, 0.1)
