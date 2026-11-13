import os
import sys

import pandas as pd

from src.exception import CustomException
from src.utils import load_object
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

data = CustomData(
    gender="male",
    race_ethnicity="group A",
    parental_level_of_education="associate's degree",
    lunch="standard",
    test_preparation_course="none",
    reading_score=70,
    writing_score=60,
)
df = data.get_data_as_data_frame()
print(PredictPipeline().predict(df))