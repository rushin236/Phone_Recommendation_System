import os
import pickle

import pandas as pd
from keras.layers import LSTM, Dense, Embedding
from keras.models import Sequential
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split

from phone_recommender.entity import ModelTrainConfig, ModelTrainParams
from phone_recommender.logging import logger


class ModelTrainer:
    def __init__(self, config=ModelTrainConfig, params=ModelTrainParams) -> None:
        self.config = config
        self.params = params

    def get_transformed_data(self):
        transform_data_file = self.config.transform_data_file
        if not os.path.exists(transform_data_file):
            logger.info("No transform data file please check if data transform is complete")
        else:
            df = pd.read_csv(self.config.transform_data_file)
            return df

    def build_model(self, df: pd.DataFrame):
        text = list(df['text'])
        clusters = df['class']

        # Initialize the Tokenizer
        tokenizer = Tokenizer()
        tokenizer.fit_on_texts(text)

        # Convert text to sequences of integers
        sequences = tokenizer.texts_to_sequences(text)

        # Pad sequences to make them of equal length (required for neural networks)
        max_sequence_length = max(map(len, sequences))
        padded_sequences = pad_sequences(sequences, maxlen=max_sequence_length, padding='post')

        # Data Sampling
        X = pd.DataFrame(padded_sequences)
        X.head()

        y = to_categorical(clusters)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        embedding_dim = self.params.embedding_dim
        vocab_size = len(tokenizer.word_index) + 1
        output_classes = self.params.output_classes

        model = Sequential()
        model.add(Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=X.shape[1]))
        model.add(LSTM(100))
        model.add(Dense(output_classes, activation='softmax'))

        # Compile the model
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        # Train the model
        epochs = self.params.epochs
        batch_size = self.params.batch_size
        model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, validation_split=0.2)

        accuracy = model.evaluate(X_test, y_test)[1]
        with open(self.config.model_evaluation_file, "w") as f:
            f.write(f'Test Accuracy: {accuracy * 100:.2f}%')

        return model, tokenizer

    def save_model_tokenizer(self, model: Sequential, tokenizer: Tokenizer):
        model.save(self.config.model_file)

        # Save the tokenizer using pickle
        tokenizer_file = self.config.tokenizer_file

        with open(tokenizer_file, 'wb') as handle:
            pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
