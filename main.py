import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Portfolio",
    page_icon="briefcase",
    layout="wide",
)
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Robert Otec")
    content = """
    I am a Python programmer with a passion for building web applications and exploring new technologies.
    """
    st.info(content)

content2 = """
Below you can find som of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)

col3, col4 = st.columns(2)

df = pd.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])