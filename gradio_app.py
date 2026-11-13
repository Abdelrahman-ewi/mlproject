import gradio as gr
from src.pipeline.predict_pipeline import CustomData, PredictPipeline


def predict(gender, ethnicity, parental_education, lunch,
            test_prep, reading_score, writing_score):
    data = CustomData(
        gender=gender,
        race_ethnicity=ethnicity,
        parental_level_of_education=parental_education,
        lunch=lunch,
        test_preparation_course=test_prep,
        reading_score=float(reading_score),
        writing_score=float(writing_score),
    )
    df = data.get_data_as_data_frame()
    result = PredictPipeline().predict(df)
    return round(float(result[0]), 2)


demo = gr.Interface(
    fn=predict,
    inputs=[
        gr.Dropdown(["male", "female"], label="Gender"),
        gr.Dropdown(["group A", "group B", "group C", "group D", "group E"], label="Race/Ethnicity"),
        gr.Dropdown(["associate's degree", "bachelor's degree", "high school",
                     "master's degree", "some college", "some high school"],
                    label="Parental Level of Education"),
        gr.Dropdown(["free/reduced", "standard"], label="Lunch"),
        gr.Dropdown(["none", "completed"], label="Test Preparation Course"),
        gr.Slider(0, 100, value=70, label="Reading Score"),
        gr.Slider(0, 100, value=70, label="Writing Score"),
    ],
    outputs=gr.Number(label="Predicted Math Score"),
    title="Student Exam Performance Predictor",
)

if __name__ == "__main__":
    demo.launch()