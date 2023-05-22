from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

def get_weather_data(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    return response.json()

def display_weather(weather_data):
    if "main" in weather_data:
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]

        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")
    else:
        print("Failed to retrieve weather data. Please try again.")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def get_weather():
    api_key = "d161d142f9a9056480d04d9c64c51a98"  # Replace with your actual API key
    location = request.form["location"]
    weather_data = get_weather_data(api_key, location)
    return render_template("index.html", weather_data=weather_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
