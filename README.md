---
title: mlproject
sdk: gradio
app_file: app.py
---
# Student Exam Performance Predictor

End-to-end ML project that predicts a student's math score from
gender, ethnicity, parental education, lunch type, test preparation,
reading score and writing score.

## Pipeline
1. Data ingestion: read the CSV and split into train/test
2. Data transformation: impute, scale and one-hot encode
3. Model training: tune 7 regressors with GridSearchCV and keep the best (R2 ≈ 0.88)
4. Prediction pipeline and Flask web app

## Run locally
```bash
pip install -r requirements.txt
python -m src.component.data_ingestion
python app.py
```
Then open http://127.0.0.1:5000/predictdata