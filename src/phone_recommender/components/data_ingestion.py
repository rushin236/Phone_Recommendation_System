import os
import urllib.request as request
from pathlib import Path

from src.phone_recommender.entity import DataIngestionConfig
from src.phone_recommender.logging import logger
from src.phone_recommender.utils.common import get_size


class DataIngestion:
    def __init__(self, config: DataIngestionConfig) -> None:
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(url=self.config.source_URL, filename=self.config.local_data_file)
            logger.info(f"{filename} downloaded! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
