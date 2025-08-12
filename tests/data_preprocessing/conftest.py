import pytest
from claims_ml.src.data_preprocessing import DataPreprocessor, load_config


@pytest.fixture
def preprocessor(config_path):
    return DataPreprocessor(config=load_config(config_path))
