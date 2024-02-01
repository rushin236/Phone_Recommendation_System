import streamlit as st

from phone_recommender.pipeline.stage_06_prediction import UserPredictionPipeline


def main():
    st.header("Welcome to Phone Recommendation System")

    col1, col2, col3 = st.columns(spec=3, gap="large")

    with col1:
        network = st.text_input(
            "Network",
            "",
            help="This field requires input of what network do you prefer 4G or 5G, input like Example: lte or lte 5g",
        )
        display_type = st.text_input(
            "Display Type",
            "",
            help="This field is for the type of display you prefer oled, ips, tft. Example input: oled or ips or tft",
        )
        storage = st.text_input(
            "Storage",
            "",
            help="This field requires the storage size you prefer like 128gb, 256gb. Example input: 128gb or 256gb",
        )
        battery = st.text_input(
            "Battery",
            "",
            help="This field requires the battery size you prefer 5000mah. Example input: 5000mah or 4000mah",
        )

    with col2:
        screen_size = st.text_input(
            "Screen Size",
            "",
            help="This field requires the size of screen you prefer like 6.7. Example input: 6.5 or 6.7",
        )
        chipset = st.text_input(
            "Chipset",
            "",
            help="This field requires the name of chipset you prefer like snapdragon, mediatek. Example input: snapdragon778g or dimensity1000 etc",
        )
        main_camera = st.text_input(
            "Main Camera",
            "",
            help="This field requires the size of main camera you prefer like 50mp. Example input: 50mp or 12mp etc",
        )
        upper_price_limit = st.text_input(
            "Upper Price Limit",
            "",
            help="This field requires the upper prices limit in rupees. Example input: 30000",
        )

    with col3:
        screen_resolution = st.text_input(
            "Screen Resolution",
            "",
            help="This field requires screen resolution you prefer like 1080p, 1440p. Example input: 2200 1080 or 2600 1440",
        )
        ram = st.text_input(
            "RAM",
            "",
            help="This field requires the how ram you prefer like 8gb, 6gb, 12gb. Example input: 8gb or 6gb",
        )
        selfie_camera = st.text_input(
            "Selfie Camera",
            "",
            help="This field requires the size of selfie camera you prefer like 8mp, 16mp. Example input: 16mp",
        )
        lower_price_limit = st.text_input(
            "Lower Price Limit",
            "",
            help="This field requires the lower price limit in rupee.",
        )

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

    submit = st.button(label="Submit")

    st.markdown(
        "Note hover over the ? icon to look at the example of what he input should be like! for the respective input fields."
    )

    if submit:
        prediction = UserPredictionPipeline()
        recommendations = prediction.main(user_data=user_input)
        st.dataframe(recommendations)
