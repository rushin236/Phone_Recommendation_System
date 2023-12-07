from phone_recommender.constants import *
from phone_recommender.entity import (
    DataExtractionConfig,
    DataIngestionConfig,
    DataTransformConfig,
    DataValidationConfig,
    ModelTrainConfig,
    ModelTrainParams,
)
from phone_recommender.utils.common import create_directories, read_yaml


class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH) -> None:
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir, source_URL=config.source_URL, local_data_file=config.local_data_file
        )

        return data_ingestion_config

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir, STATUS_FILE=config.STATUS_FILE, ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES
        )

        return data_validation_config

    def get_data_extraction_config(self) -> DataExtractionConfig:
        config = self.config.data_extraction

        create_directories([config.root_dir])

        data_extraction_config = DataExtractionConfig(
            root_dir=config.root_dir,
            local_data_file=config.local_data_file,
            extracted_data_file=config.extracted_data_file,
        )

        return data_extraction_config

    def get_data_transform_config(self) -> DataTransformConfig:
        config = self.config.data_transform

        create_directories([config.root_dir])

        data_transform_config = DataTransformConfig(
            root_dir=config.root_dir,
            extracted_data_file=config.extracted_data_file,
            transform_data_file=config.transform_data_file,
            vectorizer_file=config.vectorizer_file,
        )

        return data_transform_config

    def get_model_build_config(self):
        config = self.config.model_training
        params = self.params.parameters

        create_directories([config.root_dir])

        model_train_config = ModelTrainConfig(
            root_dir=config.root_dir,
            model_file=config.model_file,
            tokenizer_file=config.tokenizer_file,
            transform_data_file=config.transform_data_file,
            model_evaluation_file=config.model_evaluation_file,
        )

        model_train_params = ModelTrainParams(
            embedding_dim=params.embedding_dim,
            output_classes=params.output_classes,
            epochs=params.epochs,
            batch_size=params.batch_size,
        )

        return model_train_config, model_train_params
