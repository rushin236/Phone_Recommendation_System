from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: Path
    ALL_REQUIRED_FILES: str


@dataclass
class DataExtractionConfig:
    root_dir: Path
    local_data_file: Path
    extracted_data_file: Path


@dataclass
class DataTransformConfig:
    root_dir: Path
    extracted_data_file: Path
    transform_data_file: Path
    vectorizer_file: Path


@dataclass
class ModelTrainConfig:
    root_dir: Path
    model_file: Path
    tokenizer_file: Path
    transform_data_file: Path
    model_evaluation_file: Path


@dataclass
class ModelTrainParams:
    embedding_dim: int
    output_classes: int
    epochs: int
    batch_size: int
