import streamlit as st

st.title('Weather Forecast for the next days')

col1 = st.columns(1)

with col1[0]:
    place = st.text_input('Place', placeholder='Type the city name here')
    days = st.slider('Forcast Days', 1, 5)
    selection = st.selectbox('Select data to view', ('Temperature', 'Sky'))
    st.subheader(f"{selection} for the next {days} days in {place}")

