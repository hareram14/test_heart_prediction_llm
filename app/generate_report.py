def build_summary_prompt(data, prediction):
    risk_status = "has a risk of heart disease" if prediction else "is not at risk of heart disease"
    
    return f"""
Patient Health Summary:
The patient {risk_status}. Use the details below to generate a heart health summary in simple terms (150–200 words).

- Age: {data['age']} years
- Gender: {"Male" if data['gender'] == 1 else "Female"}
- Resting Blood Pressure: {data['restingBP']} mmHg
- Cholesterol: {data['serumcholestrol']} mg/dL
- Max Heart Rate: {data['maxheartrate']} bpm
- ST Depression (Oldpeak): {data['oldpeak']}
- Major Vessels Detected: {data['noofmajorvessels_2'] + 2}
- Chest Pain Type: {'Asymptomatic' if data.get('chestpain_3', 0) == 1 else 'Other'}
"""
