from pydantic import BaseModel, Field
from typing import List, Optional


## FEATURES
class PreprocessingConfig(BaseModel):
    """
    Configuration for data preprocessing steps.
    """

class FeatureConfig(BaseModel):
    """
    Configuration for feature engineering steps.
    """
    numerical: List[str] = Field(default_factory=list, description="List of numerical feature names")
    categorical: List[str] = Field(default_factory=list, description="List of categorical feature names")


## STEPS CONFIGURATION
class CategoricalStepsConfig(BaseModel):
    """
    Configuration for categorical preprocessing steps.
    """
    imputer: Optional[str] = None
    encoder: Optional[str] = None

class NumericalStepsConfig(BaseModel):
    """
    Configuration for numerical preprocessing steps.
    """
    imputer: Optional[str] = None
    scaler: Optional[str] = None

class StepsConfig(BaseModel):
    """
    Configuration for preprocessing steps.
    """
    categorical: Optional[CategoricalStepsConfig] = None
    numerical: Optional[NumericalStepsConfig] = None