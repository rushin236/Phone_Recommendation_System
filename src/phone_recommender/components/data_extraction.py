import os

import pandas as pd

from src.phone_recommender.entity import DataExtractionConfig
from src.phone_recommender.logging import logger


class DataExtraction:
    def __init__(self, config: DataExtractionConfig):
        self.config = config

    def get_local_data(self):
        local_data_file = self.config.local_data_file
        if not os.path.exists(local_data_file):
            logger.info("No local data file exists please check if data ingestion is complete!")
        else:
            df = pd.read_csv(local_data_file)
            return df

    def save_extracted_data(self, df: pd.DataFrame):
        extracted_data_file = self.config.extracted_data_file
        df.to_csv(extracted_data_file, index=False)
