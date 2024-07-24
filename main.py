import streamlit as st
import plotly.express as px
from backend import get_data


st.title('Weather Forecast for the next days')


place = st.text_input('Place', placeholder='Type the city name here')
days = st.slider('Forcast Days', 1, 5)
selection = st.selectbox('Select data to view', ('Temperature', 'Sky'))
st.subheader(f"{selection} for the next {days} days in {place}")


if place:        
    filtered_data = get_data(place, days)

    if selection == "Temperature":
        temperatures = [dict["main"]["temp"] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates, y=temperatures, title='Temperature Forecast', labels={'x': 'Date', 'y': 'Temperature'})
        st.plotly_chart(figure)

    elif selection == "Sky":
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png", "Snow": "images/snow.png"}
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        image_paths = [images[condition] for condition in sky_conditions]
        st.image(image_paths, width=115)
