import requests

API_KEY = "your_api_key_here"  

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        city_name = data["name"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        
        print(f"\nWeather in {city_name}:")
        print(f"🌡 Temperature: {temperature}°C")
        print(f"💧 Humidity: {humidity}%")
        print(f"☁ Condition: {condition}")
    else:
        print("❌ City not found or API error!")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
