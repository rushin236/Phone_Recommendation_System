from phone_recommender.logging import logger
from phone_recommender.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from phone_recommender.pipeline.stage_02_data_validation import DataValidationPipeline
from phone_recommender.pipeline.stage_03_data_extraction import DataExtractionPipeline
from phone_recommender.pipeline.stage_04_data_transform import DataTransformPipeline
from phone_recommender.pipeline.stage_05_model_train import ModelTrainerPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>{STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>> {STAGE_NAME} completed <<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>{STAGE_NAME} started <<<<<")
    data_ingestion = DataValidationPipeline()
    data_ingestion.main()
    logger.info(f">>>>> {STAGE_NAME} completed <<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Extraction Stage"
try:
    logger.info(f">>>>>{STAGE_NAME} started <<<<<")
    data_ingestion = DataExtractionPipeline()
    data_ingestion.main()
    logger.info(f">>>>> {STAGE_NAME} completed <<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transform Stage"
try:
    logger.info(f">>>>>{STAGE_NAME} started <<<<<")
    data_ingestion = DataTransformPipeline()
    data_ingestion.main()
    logger.info(f">>>>> {STAGE_NAME} completed <<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer Stage"
try:
    logger.info(f">>>>>{STAGE_NAME} started <<<<<")
    data_ingestion = ModelTrainerPipeline()
    data_ingestion.main()
    logger.info(f">>>>> {STAGE_NAME} completed <<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e
