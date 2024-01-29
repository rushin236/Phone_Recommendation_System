import os

import streamlit as st
from streamlit_option_menu import option_menu

from st_templates.recommend import main

st.set_page_config(layout="wide")

selected = option_menu(
    menu_title="Phone Recommendation",
    options=["Home", "Recommend", "About"],
    icons=["house", "phone", "file-person"],
    orientation="horizontal",
    default_index=0,
)

if selected == "Home":
    with open(
        "./st_templates/markdown/home_content.md", "r", encoding="UTF-8"
    ) as home_md:
        home_content = home_md.read()

    st.markdown(home_content, unsafe_allow_html=True)

elif selected == "Recommend":
    with open(
        "./st_templates/markdown/recommend_content.md", "r", encoding="UTF-8"
    ) as recommend_md:
        recommend_content = recommend_md.read()

    st.markdown(
        f"""{recommend_content}""",
        unsafe_allow_html=True,
    )
    main()

elif selected == "About":
    with open(
        "./st_templates/markdown/about_content.md", "r", encoding="UTF-8"
    ) as about_md:
        about_content = about_md.read()

    st.markdown(about_content, unsafe_allow_html=True)
