from src.phone_recommender.components.model_trainer import ModelTrainer
from src.phone_recommender.config.configuration import ConfigurationManager


class ModelTrainerPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        model_build_config, model_params_config = config.get_model_train_params_config()
        model_trainer = ModelTrainer(model_build_config, model_params_config)
        df = model_trainer.get_transformed_data()
        model, tokenizer = model_trainer.train_model(df)
        model_trainer.save_model_tokenizer(model, tokenizer)
