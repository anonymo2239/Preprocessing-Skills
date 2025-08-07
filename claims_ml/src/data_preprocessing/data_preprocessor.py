from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import (
    ColumnTransformer,
)  # Hangi columna hangi transformer uygulanacağını belirler
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from .load_config import PreprocessorConfig, load_config
from sklearn.impute import SimpleImputer


class DataPreprocessor(BaseEstimator, TransformerMixin):
    def __init__(self, config=None):
        self.is_fitted = False
        self.config = config

    def _build_column_transformer(self):
        transformers = []
        for feature in self.config.features.numerical:
            numerical_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="mean")),
                    ("scaler", self.config.steps.numerical.scaler),
                ]
            )
            transformers.append((feature, numerical_pipeline, [feature]))

        for feature in self.config.features.categorical:
            categorical_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    (
                        "encoder",
                        OneHotEncoder(handle_unknown="ignore"),
                    ),  # TODO: Model yazımında değinilip, değiştirilecek.
                ]
            )
            transformers.append((feature, categorical_pipeline, [feature]))

        return ColumnTransformer(
            transformers=transformers, remainder="drop"
        )  # remainder='drop' ile ismini girmediğimiz kolonlar düşürülür.

    def fit(self, X, y=None):
        self.pipeline = self._build_column_transformer()
        self.pipeline.fit(X, y)
        self.is_fitted = True
        return self

    def transform(self, X):
        if not self.is_fitted:
            raise RuntimeError(
                "You must fit the preprocessor before transforming data."
            )
        return self.pipeline.transform(X)

    def fit_transform(self, X, y=None):
        self.fit(X, y)
        return self.transform(X)
