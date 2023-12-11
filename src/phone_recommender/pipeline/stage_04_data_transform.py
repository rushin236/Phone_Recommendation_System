# Data handling libraries
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Setup libraries
from phone_recommender.components.data_transform import DataTransform
from phone_recommender.config.configuration import ConfigurationManager


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

        clusters = KMeans(n_clusters=3, random_state=42).fit_predict(df_dtm)

        data_transform.save_vectorizer(cv)

        df_trans['class'] = clusters
        df_cate['class'] = clusters
        data_transform.save_transformed_data(df_cate)
