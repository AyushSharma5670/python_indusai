import urllib.request
import json

# Function to fetch weather data
def fetch_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    query = f"?q={urllib.parse.quote(location)}&appid={api_key}&units=metric"
    url = base_url + query
    
    try:
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                data = response.read()
                return json.loads(data)
            else:
                return None
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None

# Function to display weather data
def display_weather(data):
    if data:
        location = data['name']
        temp = data['main']['temp']
        weather = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        
        print(f"Weather in {location}:")
        print(f"Temperature: {temp}°C")
        print(f"Description: {weather}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("Sorry, could not fetch the weather data. Please check the location and try again.")

def main():
    api_key = "c2eca50f8d1e8563ce52567e9477ca97"  # API key from open weather maps
    print("Welcome to the Weather API Fetcher!")
    
    while True:
        location = input("Enter the location to get the current weather (or 'exit' to quit): ")
        
        if location.lower() == 'exit':
            print("Goodbye!")
            break
        
        weather_data = fetch_weather(api_key, location)
        display_weather(weather_data)

# Start the Weather API Fetcher
if _name_ == "_main_":
    main()
