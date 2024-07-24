import streamlit as st
import plotly.express as px
from backend import get_data


st.title('Weather Forecast for the next days')


place = st.text_input('Place', placeholder='Type the city name here')
days = st.slider('Forcast Days', 1, 5)
selection = st.selectbox('Select data to view', ('Temperature', 'Sky'))
st.subheader(f"{selection} for the next {days} days in {place}")


def get_data(days):
    dates = ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05']
    temperatures = [10, 20, 30, 4, 23]
    temperatures = [days* i for i in temperatures]
    return dates , temperatures


data = get_data(place, days, selection)


d , t = get_data(days)


figure = px.line(x=d, y=t, title='Temperature Forecast', 
                 labels={'x': 'Date', 'y': 'Temperature'})
st.plotly_chart(figure)
