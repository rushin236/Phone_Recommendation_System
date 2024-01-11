import os

import streamlit as st
from streamlit_option_menu import option_menu

from streamlit_pages.recommend import main

st.set_page_config(layout="wide")

selected = option_menu(
    menu_title="Phone Recommendation",
    options=["Home", "Recommend", "About"],
    icons=["house", "phone", "file-person"],
    orientation="horizontal",
    default_index=0,
)

if selected == "Home":
    with open("./streamlit_pages/markdown/home_content.md", "r", encoding="UTF-8") as home_md_file:
        home_content = home_md_file.read()

    st.markdown(home_content, unsafe_allow_html=True)

elif selected == "Recommend":
    main()

elif selected == "About":
    with open("./streamlit_pages/markdown/about_content.md", "r", encoding="UTF-8") as about_md_file:
        about_content = about_md_file.read()

    st.markdown(about_content)
