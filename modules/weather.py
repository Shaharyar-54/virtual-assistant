# # modules/weather.py
# import requests

# def get_weather(city):
#     try:
#         api_key = "1df5b32efffdee7f3ee4ac6334051df4"  
#         url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
#         response = requests.get(url)
#         data = response.json()

#         if data["cod"] != "404":
#             weather = data["weather"][0]["description"]
#             temp = data["main"]["temp"]
#             return f"The weather in {city} is {weather} with a temperature of {temp}°C."
#         else:
#             return "City not found. Please try again."
#     except Exception as e:
#         return f"Failed to get weather information: {str(e)}"


import requests
import os
from dotenv import load_dotenv

load_dotenv() 

def get_weather(city):
    try:
        api_key = os.getenv("WEATHER_API_KEY")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        print(data)  

        if data["cod"] != 404:
            weather = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            return f"The weather in {city} is {weather} with a temperature of {temp}°C."
        else:
            return "City not found. Please try again."
    except Exception as e:
        return f"Failed to get weather information: {str(e)}"
