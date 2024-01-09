import numpy as np
import pandas as pd
from keras.preprocessing.sequence import pad_sequences
from sklearn.metrics.pairwise import cosine_similarity

from src.phone_recommender.components.user_prediction import Prediction
from src.phone_recommender.config.configuration import ConfigurationManager


def get_class_prediction(model, trans_df, tokenizer, max_sequence_length, user_data):
    user_features = ""
    for feat, spec in user_data.items():
        if feat not in ['lower_price', 'upper_price']:
            if spec in set(trans_df[feat]):
                user_features += spec + " "

            else:
                user_features += "0" + " "

    lower_price = float(user_data['lower_price'])
    upper_price = float(user_data['upper_price'])

    if lower_price == upper_price:
        upper_price += 2000

    user_features = user_features.strip()
    user_input = tokenizer.texts_to_sequences([user_features])
    user_input = pad_sequences(sequences=user_input, maxlen=max_sequence_length, padding="post")
    user_prediction = model.predict(user_input)
    user_prediction = np.argmax(user_prediction, axis=1)
    return user_features, user_prediction[0], lower_price, upper_price


def get_recommendation(trans_df: pd.DataFrame(), cv, dtm, user_features, user_prediction, lower_price, upper_price):
    idx = trans_df[(trans_df['class'] == user_prediction) & (trans_df['price'].between(lower_price, upper_price))].index
    user_cv = cv.transform([user_features])
    dtm = pd.DataFrame(dtm.toarray(), columns=cv.get_feature_names_out())
    recommendation = (
        pd.DataFrame(cosine_similarity(dtm.iloc[idx, :], user_cv.toarray()), index=idx)
        .sort_values(0, ascending=False)
        .head()
        .index
    )
    recommendation = trans_df.loc[
        recommendation,
        [
            'brand',
            'phone_name',
            'network',
            'released_year',
            'resolution',
            'display_size_str',
            'display_type',
            'os',
            'chipset',
            'ram',
            'storage',
            'type',
            'main_camera',
            'selfie_camera',
            'bluetooth',
            'battery',
            'price',
        ],
    ]

    return recommendation


# def get_test_data(user_data, trans_df):
#     user_features = ""
#     for feat, spec in user_data.items():
#         if feat not in ['lower_price', 'upper_price']:
#             if spec in set(trans_df[feat]):
#                 user_features += spec + " "

#             else:
#                 user_features += "0" + " "

#     lower_price = user_data['lower_price']
#     upper_price = user_data['upper_price']

#     print(user_features, upper_price, lower_price)


class UserPredictionPipeline:
    def __init__(self) -> None:
        pass

    def main(self, user_data: dict):
        config = ConfigurationManager()
        prediction_config = config.get_prediction_config()
        prediction = Prediction(prediction_config)
        trans_df, cv, tokenizer, model, max_sequence_length, dtm = prediction.get_objects()
        user_features, user_prediction, lower_price, upper_price = get_class_prediction(
            model, trans_df, tokenizer, max_sequence_length, user_data
        )
        recommendation = get_recommendation(trans_df, cv, dtm, user_features, user_prediction, lower_price, upper_price)
        # print(recommendation)
        return recommendation


if __name__ == "__main__":
    user_data = {
        "network": "lte",
        "display_size_str": "6.7",
        "resolution": "1080 2400",
        "display_type": "oled 120hz",
        "chipset": "snapdragon870",
        "ram": "8gb",
        "storage": "128gb",
        "main_camera": "50mp",
        "selfie_camera": "16mp",
        "battery": "5000mah",
        "lower_price": 20000,
        "upper_price": 30000,
    }
    prediction = UserPredictionPipeline()
    prediction.main(user_data=user_data)
