import streamlit as st
import requests

# App Title
st.title("Weather Dashboard")
st.markdown("Get current weather information for any city worldwide.")

# Input for city name
city = st.text_input("Enter the city name:", "")

# API Key (Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key)
API_KEY = "YOUR_API_KEY"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

if st.button("Get Weather"):
    if city:
        # API request
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            data = response.json()
            st.subheader(f"Weather in {city.title()}:")
            st.write(f"**Temperature:** {data['main']['temp']}°C")
            st.write(f"**Feels Like:** {data['main']['feels_like']}°C")
            st.write(f"**Humidity:** {data['main']['humidity']}%")
            st.write(f"**Weather:** {data['weather'][0]['description'].capitalize()}")
            st.write(f"**Wind Speed:** {data['wind']['speed']} m/s")
        else:
            st.error("City not found. Please check the city name and try again.")
    else:
        st.warning("Please enter a city name!")
