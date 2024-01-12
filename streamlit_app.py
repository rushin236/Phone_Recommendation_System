import os

import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")

selected = option_menu(
    menu_title="Phone Recommendation",
    options=["Home", "Recommend", "About"],
    icons=["house", "phone", "file-person"],
    orientation="horizontal",
    default_index=0,
)

if selected == "Home":
    with open("./st_templates/markdown/home_content.md", "r", encoding="UTF-8") as home_md:
        home_content = home_md.read()

    st.markdown(home_content)

elif selected == "Recommend":
    pass

elif selected == "About":
    with open("./st_templates/markdown/about_content.md", "r", encoding="UTF-8") as about_md:
        about_content = about_md.read()

    st.markdown(about_content)
