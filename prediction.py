import streamlit as st
import pandas as pd
import pickle
from PIL import Image

# Load model

with open('model_pipeline.pkl', 'rb') as file_1:
  model_pipeline = pickle.load(file_1)



def run():

    # Add title
    st.title("Heart Disease Prediction")

    # Add image
    img = Image.open('jantung.png')
    st.image(img)

    with st.form('form_fifa_2022'):
        age = st.slider('Age: ', min_value = 16, max_value = 100, value = 25)
        sex = st.selectbox('Gender: ', ('M', 'F'))
        chestpaintype = st.selectbox('Chest Pain Type [TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic]: ', ('TA', 'ATA', 'NAP', 'ASY'))
        restingbp = st.number_input('Resting Blood Pressure (mmHg): ', min_value = 0, max_value = 200, value = 100)
        cholesterol = st.number_input('Cholesterol (mm/dl): ', min_value = 0, max_value = 1000, value = 200)
        fastingbs = st.selectbox('Fasting blood sugar [1: if FastingBS > 120 mg/dl, 0: otherwise]: ', (0, 1))
        restingecg = st.selectbox('resting electrocardiogram results [Normal: Normal, ST: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV), LVH: showing probable or definite left ventricular hypertrophy by Estes criteria]', ('Normal', 'ST', 'LVH'))
        maxHR = st.number_input('Maximum heart rate', min_value = 60, max_value = 220, value =180)
        exerciseangina = st.selectbox('Exercise-induced angina: ', ('Y', 'N'))
        oldpeak = st.number_input('Oldpeak: ', min_value = -5, max_value = 10, value = 1)
        ST_slope = st.selectbox('The slope of the peak exercise ST segment [Up: upsloping, Flat: flat, Down: downsloping]: ', ('Up', 'Flat', 'Down'))

        submit = st.form_submit_button('Predict')

    data_inf = {
    'Age': age,
    'Sex': sex,
    'ChestPainType': chestpaintype,
    'RestingBP': restingbp,
    'Cholesterol': cholesterol,
    'FastingBS': fastingbs,
    'RestingECG': restingecg,
    'MaxHR': maxHR,
    'ExerciseAngina': exerciseangina,
    'Oldpeak': oldpeak,
    'ST_Slope': ST_slope}

    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submit:
        # Predict using Linear Regression
        y_pred_inf = model_pipeline.predict(data_inf)
        if y_pred_inf[0] == 1:
           result = "You have been diagnosed with heart disease"
        else:
           result = "You do not have heart disease"

        st.write(result)

if __name__ == '__main__':
  run()