import pickle
import re
import string

# Visualization Libraries
import matplotlib.pyplot as plt
import numpy as np

# Data handling libraries
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import silhouette_samples

from phone_recommender.components.data_transform import DataTransform
from phone_recommender.config.configuration import ConfigurationManager
from phone_recommender.logging import logger

# Setup Libraries


class DataTransformPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()

        data_transform_config = config.get_data_transform_config()
        data_transform = DataTransform(data_transform_config)
        df = data_transform.get_extracted_data()
        df['display_size_str'] = df['display_size_str'].astype('str')
        df_cate = df[df.select_dtypes(include='object').columns]
        df_trans = data_transform.get_transform_dataframe(df_cate)
        df_trans, df_cate = data_transform.transform_dataframe(df_cate=df_cate, df_trans=df_trans)
        cv = CountVectorizer()
        df_cv = cv.fit_transform(df_trans['text'])
        df_dtm = pd.DataFrame.sparse.from_spmatrix(df_cv, columns=cv.get_feature_names_out())
        tdm = df_dtm.T
        tdm['freq'] = tdm.sum(axis=1)
        tdm.reset_index(inplace=True)
        tdm.rename(columns={'index': 'words'}, inplace=True)
        tdm1 = tdm[['words', 'freq']]
        tdm1 = tdm1.sort_values('freq', ascending=False)
        tdm1.reset_index(inplace=True)
        tdm1.drop("index", inplace=True, axis=1)

        ssd = []
        for i in range(1, 11):
            kmeans = KMeans(n_clusters=i, random_state=42)
            kmeans.fit(df_dtm)
            scr = kmeans.score(df_dtm)
            ssd.append(scr)
            print(f"cluster number {i} cluster remaining {10 - i}")

        clusters = KMeans(n_clusters=3, random_state=42).fit_predict(df_dtm)

        idf = TfidfVectorizer()
        df_tfidf = idf.fit_transform(df_trans['text'])
        tfidf = pd.DataFrame.sparse.from_spmatrix(df_tfidf, columns=idf.get_feature_names_out())

        ssd = []
        for i in range(1, 11):
            kmeans = KMeans(n_clusters=i, random_state=42)
            kmeans.fit(tfidf)
            scr = kmeans.score(tfidf)
            ssd.append(scr)
            print(f"cluster number {i} cluster remaining {10 - i}")

        cluster2 = KMeans(n_clusters=3, random_state=42).fit_predict(tfidf)

        data_transform.save_vectorizer(cv)

        df_trans['class'] = clusters
        df_cate['class'] = clusters
        data_transform.save_transformed_data(df_cate)
