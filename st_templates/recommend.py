import streamlit as st

from src.phone_recommender.pipeline.stage_06_prediction import UserPredictionPipeline


def main():
    st.title("Welcome to Phone Recommendation System")

    col1, col2, col3 = st.columns(spec=3, gap="large")

    with col1:
        network = st.text_input("Network", "")
        display_type = st.text_input("Display Type", "")
        storage = st.text_input("Storage", "")
        battery = st.text_input("Battery", "")

    with col2:
        screen_size = st.text_input("Screen Size", "")
        chipset = st.text_input("Chipset", "")
        main_camera = st.text_input("Main Camera", "")
        upper_price_limit = st.text_input("Upper Price Limit", "")

    with col3:
        screen_resolution = st.text_input("Screen Resolution", "")
        ram = st.text_input("RAM", "")
        selfie_camera = st.text_input("Selfie Camera", "")
        lower_price_limit = st.text_input("Lower Price Limit", "")

    user_input = {
        "network": network,
        "display_size_str": screen_size,
        "resolution": screen_resolution,
        "display_type": display_type,
        "chipset": chipset,
        "ram": ram,
        "storage": storage,
        "main_camera": main_camera,
        "selfie_camera": selfie_camera,
        "battery": battery,
        "lower_price": lower_price_limit,
        "upper_price": upper_price_limit,
    }

    # st.write(user_input)

    if st.button(
        label="Submit",
    ):
        prediction = UserPredictionPipeline()
        recommendations = prediction.main(user_data=user_input)
        st.dataframe(recommendations)
