import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from PIL import Image

def run():
    st.title("Data Overview for Hearth Disease Prediction Model")

    # Add image
    img = Image.open('jantung.png')
    st.image(img)

    # load data
    data = pd.read_csv('heart.csv')
    st.dataframe(data)

    # chart 1
    st.write('### Plot Satcked Bar Chart')
    fig = plt.figure(figsize = (10,5))
    options = st.selectbox("Select Column for Histogram", ('Age', 'Sex'))
    sns.histplot(data=data, x= options, hue="HeartDisease", multiple = 'stack')
    st.pyplot(fig)

    # chart 2
    # barplot
    st.write("### Plot ChestPainType")
    fig = plt.figure(figsize = (10,5))
    sns.countplot(x='ChestPainType', data = data)
    st.pyplot(fig)


    # chart 3, plotly express
    st.write('### Scatterplot Cholesterol vs Age')
    fig = px.scatter(data, x = 'Age', y ='Cholesterol', hover_data = ['Sex'])
    st.plotly_chart(fig)
    
if __name__ == "__main__":
    run()