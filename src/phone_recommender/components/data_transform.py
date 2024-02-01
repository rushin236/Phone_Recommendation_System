import os
import pickle
import string

import pandas as pd

from phone_recommender.entity import DataTransformConfig
from phone_recommender.logging import logger


class DataTransform:
    def __init__(self, config: DataTransformConfig) -> None:
        self.config = config

    def get_extracted_data(self):
        extracted_data_file = self.config.extracted_data_file
        if not os.path.exists(extracted_data_file):
            logger.info(
                "No extracted data file exists please check if data extraction is complete!"
            )
        else:
            df = pd.read_csv(extracted_data_file)
            return df

    def get_transform_dataframe(self, df_cate: pd.DataFrame):
        trans_columns = [
            "network",
            "released_year",
            "resolution",
            "display_size_str",
            "display_type",
            "chipset",
            "ram",
            "storage",
            "type",
            "main_camera",
            "selfie_camera",
            "bluetooth",
            "battery",
        ]
        df_trans = df_cate[trans_columns]

        return df_trans

    def transform_dataframe(self, df_cate, df_trans):
        df_trans["text"] = df_trans.apply(lambda row: " ".join(map(str, row)), axis=1)
        df_cate["text"] = df_trans.apply(lambda row: " ".join(map(str, row)), axis=1)
        df_trans["text"] = df_trans["text"].apply(lambda x: " ".join(x.split()))
        df_trans["text"] = df_trans["text"].apply(
            lambda x: "".join([char for char in x if char not in string.punctuation])
        )

        return df_trans, df_cate

    def save_vectorizer(self, vectorizer):
        with open(self.config.vectorizer_file, "wb") as handle:
            pickle.dump(vectorizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def save_transformed_data(self, df: pd.DataFrame):
        df.to_csv(self.config.transform_data_file, index=False)
