import pickle
from pathlib import Path

import numpy as np
import pandas as pd
from keras.models import load_model

from phone_recommender.entity import PredictionConfig


def get_dataframe(path: Path):
    trans_df = pd.read_csv(path)
    trans_df['display_size_str'] = trans_df['display_size_str'].astype('str')
    return trans_df


def get_count_vectorizer(path: Path):
    with open(path, "rb") as handle:
        cv = pickle.load(handle)
        return cv


def get_dtm(cv, trans_df):
    dtm = trans_df[
        [
            'network',
            'released_year',
            'resolution',
            'display_size_str',
            'display_type',
            'chipset',
            'ram',
            'storage',
            'type',
            'main_camera',
            'selfie_camera',
            'bluetooth',
            'battery',
        ]
    ]

    dtm['new_text'] = dtm.apply(lambda x: " ".join(map(str, x)), axis=1)

    dtm = cv.transform(dtm['new_text'])
    return dtm


def get_tokenizer(path: Path):
    with open(path, "rb") as handle:
        tokenizer = pickle.load(handle)
        return tokenizer


def get_model(path: Path):
    model = load_model(path)
    return model


class Prediction:
    def __init__(self, config: PredictionConfig) -> None:
        self.config = config

    def get_objects(self):
        trans_df = get_dataframe(self.config.transform_data_file)
        cv = get_count_vectorizer(self.config.vectorizer_file)
        tokenizer = get_tokenizer(self.config.tokenizer_file)
        model = get_model(self.config.model_file)
        max_sequence_length = self.config.max_sequence_length
        dtm = get_dtm(cv, trans_df)

        return trans_df, cv, tokenizer, model, max_sequence_length, dtm
