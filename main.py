import streamlit as st

st.set_page_config(
    page_title="Portfolio",
    page_icon=":briefcase:",
    layout="wide",
)
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Robert Otec")
    content = """
    I am a software engineer with a passion for building web applications and exploring new technologies.
    """
    st.info(content)

content2 = """
Below you can find som of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)