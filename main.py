# main.py

from app.predict_heart_disease import predict
from app.generate_report import build_summary_prompt
from llm.summarizer import get_medical_summary

# Sample input for testing
patient_input = {
    'restingBP': 135,
    'serumcholestrol': 260,
    'maxheartrate': 135,
    'oldpeak': 1.8,
    'age': 59,
    'slope_1': 1,
    'chestpain_0': 0,
    'chestpain_2': 1,
    'gender': 1,
    'restingelectro_0': 0,
    'noofmajorvessels_2': 1,
}

# Step 1: Get prediction
prediction = predict(patient_input)

# Step 2: Build prompt
prompt = build_summary_prompt(patient_input, prediction)

# Step 3: Generate summary
summary = get_medical_summary(prompt)

print("\n📊 Prediction:", "✅ Heart Disease" if prediction else "❌ No Heart Disease")
print("\n📝 Summary:\n", summary)
