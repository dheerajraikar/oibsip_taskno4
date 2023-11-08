import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("400x300")

        self.location_label = ttk.Label(root, text="Enter Location:")
        self.location_label.pack(pady=10)

        self.location_entry = ttk.Entry(root)
        self.location_entry.pack()

        self.get_weather_button = ttk.Button(root, text="Get Weather", command=self.get_weather)
        self.get_weather_button.pack(pady=10)

        self.weather_data_label = ttk.Label(root, text="")
        self.weather_data_label.pack()

    def get_weather(self):
        location = self.location_entry.get()
        weather_data = self.fetch_weather_data(location)

        if weather_data:
            self.display_weather_data(weather_data)
        else:
            messagebox.showerror("Error", "Unable to fetch weather data.")
    def fetch_weather_data(self, location):
        return {
            "location": location,
            "current_conditions": "Partly Cloudy",
            "temperature": f"{random.randint(60, 90)}°F",
            "hourly_forecast": ["2 PM: Sunny", "3 PM: Cloudy", "4 PM: Rain"],
            "daily_forecast": ["Monday: 70°F/50°F, Rain", "Tuesday: 75°F/55°F, Sunny"],
            "wind_speed": f"{random.randint(1, 10)} mph",
        }

    def display_weather_data(self, data):
        weather_info = f"Weather for {data['location']}:\n"
        weather_info += f"Current Conditions: {data['current_conditions']}\n"
        weather_info += f"Temperature: {data['temperature']}\n"
        weather_info += "Hourly Forecast:\n"
        for forecast in data['hourly_forecast']:
            weather_info += f"- {forecast}\n"
        weather_info += "Daily Forecast:\n"
        for forecast in data['daily_forecast']:
            weather_info += f"- {forecast}\n"
        weather_info += f"Wind Speed: {data['wind_speed']}\n"

        self.weather_data_label.config(text=weather_info)

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()



