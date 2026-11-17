# **English**


# Heart Disease Prediction

## Model Deployment (Streamlit App)

[https://heartdiseasepredictioning.streamlit.app/](https://heartdiseasepredictioning.streamlit.app/)

## Repository Outline

```
1. README.md - Overview explanation of the project
2. heart_disease_prediction.ipynb - Notebook containing EDA through model building
3. inference.ipynb - Notebook containing inference data
4. data.csv - Dataset used for the project
5. model_pipeline.pkl - Model file for prediction
6. eda.py - Python file containing EDA (Streamlit)
7. prediction.py - Python file for Streamlit prediction
8. streamlit_app.py - Main Streamlit application file
9. requirements.txt - Libraries used in the program

```

## Problem Background

Cardiovascular Diseases (CVDs) are the leading cause of death globally. Every year, an estimated 17.9 million people die from these diseases. Statistically, about one-third of CVD-related deaths occur in people under 70 years old. This is quite concerning given that the average global life expectancy in recent years has hovered around 73 years. Therefore, identifying individuals at risk for CVDs—such as heart failure—can help minimize premature mortality (under age 73) by ensuring proper medical treatment. The program developed in this project aims to predict whether an individual has potential heart disease. This enables individuals at risk of heart failure to seek immediate medical consultation for appropriate intervention. Meanwhile, individuals who are not at risk are still encouraged to exercise regularly and maintain a healthy lifestyle.

## Project Output

The output of this project is a machine learning model to predict whether a person is at risk for heart disease. The developed model is deployed using Streamlit.

## Data

The [Dataset](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction) used to predict heart disease was obtained from Kaggle. It consists of 918 rows and 12 columns detailed as follows:

1. Age: age of the patient [years]
2. Sex: sex of the patient [M: Male, F: Female]
3. ChestPainType: chest pain type [TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic]
4. RestingBP: resting blood pressure [mm Hg]
5. Cholesterol: serum cholesterol [mm/dl]
6. FastingBS: fasting blood sugar [1: if FastingBS > 120 mg/dl, 0: otherwise]
7. RestingECG: resting electrocardiogram results [Normal: Normal, ST: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV), LVH: showing probable or definite left ventricular hypertrophy by Estes' criteria]
8. MaxHR: maximum heart rate achieved [Numeric value between 60 and 202]
9. ExerciseAngina: exercise-induced angina [Y: Yes, N: No]
10. Oldpeak: oldpeak = ST [Numeric value measured in depression]
11. ST_Slope: the slope of the peak exercise ST segment [Up: upsloping, Flat: flat, Down: downsloping]
12. HeartDisease: output class [1: heart disease, 0: Normal]

## Method

This project evaluates 5 supervised machine learning models: K-Nearest Neighbors (KNN), Support Vector Machine (SVM), Decision Tree, Random Forest, and Gradient Boosting. The best-performing base model is selected via cross-validation, followed by hyperparameter tuning. The model with the optimal hyperparameter combination is selected as the final predictive model.

## Tech Stack

* Programming Language: Python
* Tools: Visual Studio Code
* Libraries: detailed in `requirements.txt`

## References

* [Bonett G., 2020](https://pubmed.ncbi.nlm.nih.gov/31565811/)
* [https://adatawinter.site.wesleyan.edu/schedule-2/chi-square-and-correlation/](https://adatawinter.site.wesleyan.edu/schedule-2/chi-square-and-correlation/)
* [https://www.who.int/health-topics/cardiovascular-diseases#tab=tab_1](https://www.who.int/health-topics/cardiovascular-diseases#tab=tab_1)
* [https://www.macrotrends.net/global-metrics/countries/wld/world/life-expectancy](https://www.macrotrends.net/global-metrics/countries/wld/world/life-expectancy)
* [https://www.cdc.gov/heart-disease/prevention/index.html](https://www.cdc.gov/heart-disease/prevention/index.html)
* [Model Deployment](https://heartdiseasepredictioning.streamlit.app/)



# **Indonesia**

# Prediksi Penyakit Jantung

## Model deployment (Streamlit app)
https://heartdiseasepredictioning.streamlit.app/

## Repository Outline

```
1. README.md - Penjelasan gambaran umum project
2. heart_disease_prediction.ipynb - Notebook yang berisi EDA hingga pembuatan model
3. inference.ipynb - Notebook yang berisi data inference
4. data.csv - Dataset yang digunakan
5. model_pipeline.pkl - File model untuk prediksi
6. eda.py - File python berisi EDA (streamlit)
7. prediction.py - File python untuk prediksi streamlit
8. steamlit_app.py - File utama streamlit
9. requirements.txt - Library yang digunakan untuk program
```

## Problem Background
Penyakit kardiovaskular (Cardiovascular Diseases)/CVD merupakan penyebab kematian paling umum di dunia. Setiap tahunnya, sekitar 17.9 juta jiwa mengalami kematian disebabkan oleh penyakit ini. Secara statistik, sekitar satu pertiga dari kematian yang disebabkan oleh penyakit ini terjadi pada orang berusia di bawah 70 tahun. Hal ini cukup memprihatinkan karena rata-rata angka harapan hidup di dunia beberapa tahun terakhir berada di angka sekitar 73 tahun. Oleh karena itu, mengidentifikasi orang dengan potensi terkena penyakit CVD seperti gagal jantung diharapkan dapat meminimalsir angka kematian prematur (di bawah 73 tahun) dengan memastikan pengobatan yang tepat untuk penderita penyakit tersebut. Program yang akan dibuat kali ini bertujuan untuk memprediksi apakah seseorang berpotensi memiliki penyakit jantung atau tidak. Dengan begitu, orang dengan potensi gagal jantung dapat segera berkonsultasi dengan dokter agar dilakukan penanganan yang tepat. Sementara itu, orang yang tidak berpotensi gagal jantung tetap dianjurkan untuk rutin berolahraga dan menjaga pola hidup sehat.

## Project Output
Output dari project ini ialah model machine learning untuk memprediksi apakah seseorang berpotensi memiliki penyakit jantung atau tidak. Model yang dibuat akan di deploy menggunakan streamlit

## Data
[Dataset](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction) merupakan data untuk memprediksi penyakit jantung yang diperoleh dari Kaggle. Data ini terdiri dari 918 baris dan 12 kolom dengan rincian sebagai berikut:
1. Age: age of the patient [years]
2. Sex: sex of the patient [M: Male, F: Female]
3. ChestPainType: chest pain type [TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic]
4. RestingBP: resting blood pressure [mm Hg]
5. Cholesterol: serum cholesterol [mm/dl]
6. FastingBS: fasting blood sugar [1: if FastingBS > 120 mg/dl, 0: otherwise]
7. RestingECG: resting electrocardiogram results [Normal: Normal, ST: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV), LVH: showing probable or definite left ventricular hypertrophy by Estes' criteria]
8. MaxHR: maximum heart rate achieved [Numeric value between 60 and 202]
9. ExerciseAngina: exercise-induced angina [Y: Yes, N: No]
10. Oldpeak: oldpeak = ST [Numeric value measured in depression]
11. ST_Slope: the slope of the peak exercise ST segment [Up: upsloping, Flat: flat, Down: downsloping]
12. HeartDisease: output class [1: heart disease, 0: Normal]

## Method
Metode yang digunakan pada project ini adalah 5 model supervised machine learning yaitu K-Nearest Neighbours (KNN), Support Vector Machine (SVM), Decision Tree, Random Forest dan Gradient Boost. Dari kelima base model tersebut dipilih model terbaik berdasarkan cross validation dan dilakukan hyperparameter tuning untuk model tersebut. Model dengan kombinasi hyperparameter terbaik akan dijadikan model prediksi final.

## Stacks
- Bahasa Pemrograman: Python
- tools: Visual Studio Code

- library: dapat dilihat pada `requirements.txt`

## Reference
- [Bonett G., 2020](https://pubmed.ncbi.nlm.nih.gov/31565811/)
- https://adatawinter.site.wesleyan.edu/schedule-2/chi-square-and-correlation/
- https://www.who.int/health-topics/cardiovascular-diseases#tab=tab_1
- https://www.macrotrends.net/global-metrics/countries/wld/world/life-expectancy
- https://www.cdc.gov/heart-disease/prevention/index.html
- [Model Depoyment](https://heartdiseasepredictioning.streamlit.app/) 

---
