import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")

def get_weather(city):
    """Retrieves weather information from OpenWeatherMap API."""
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + API_KEY + "&q=" + city + "&units=metric"  # Use metric units

    try:
        response = requests.get(complete_url)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        x = response.json()

        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]

            print(" Temperature (in Celsius unit) = " + str(current_temperature) +
                  "\n atmospheric pressure (in hPa unit) = " + str(current_pressure) +
                  "\n humidity (in percentage) = " + str(current_humidity) +
                  "\n description = " + str(weather_description))
        else:
            print(" City Not Found ")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
    except (KeyError, IndexError) as e:
        print(f"Error parsing weather data: {e}. The API response format might have changed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    while True:
        city = input("Enter city name (or 'exit' to quit): ")
        if city.lower() == "exit":
            break

        if not API_KEY:
            print("Error: OPENWEATHERMAP_API_KEY environment variable not set.")
            break

        get_weather(city)