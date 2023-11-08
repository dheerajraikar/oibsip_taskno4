import requests


def fetch_weather_data(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)
        return None


def display_weather_data(data):
    if data is None:
        return

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather_description = data["weather"][0]["description"]

    print(f"Weather in {data['name']}, {data['sys']['country']}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Conditions: {weather_description.capitalize()}")


def main():
    api_key = "b0a5b574ad87fd3468a1a087f13eb324"  # Replace with your OpenWeatherMap API key
    location = input("Enter a city or ZIP code: ")

    data = fetch_weather_data(api_key, location)
    display_weather_data(data)


if __name__ == "__main__":
    main()
