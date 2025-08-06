from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin

class DataPreprocessor(BaseEstimator, TransformerMixin):
    def __init__(self, config=None):
        self.is_fitted = False
        self.config = config

    def fit(self, X, y=None):

    def transform(self, X):
        return X
    
    def fit_transform(self, X, y=None):
