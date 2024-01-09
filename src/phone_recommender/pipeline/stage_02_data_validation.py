from src.phone_recommender.components.data_validation import DataValidation
from src.phone_recommender.config.configuration import ConfigurationManager


class DataValidationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(data_validation_config)
        data_validation.validate_all_file_exist()
