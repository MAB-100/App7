import streamlit as st
import plotly.express as px
from backend import get_data


st.title('Weather Forecast for the next days')


place = st.text_input('Place', placeholder='Type the city name here')
days = st.slider('Forcast Days', 1, 5)
selection = st.selectbox('Select data to view', ('Temperature', 'Sky'))
st.subheader(f"{selection} for the next {days} days in {place}")



data = get_data(place, days, selection)



figure = px.line(x=d, y=t, title='Temperature Forecast', 
                 labels={'x': 'Date', 'y': 'Temperature'})
st.plotly_chart(figure)
