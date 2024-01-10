import os

import streamlit as st

with open("./markdown/home_content.md", "r", encoding="UTF-8") as md_file:
    home_content = md_file.read()


def main():
    st.markdown(home_content)


if __name__ == "__main__":
    main()
