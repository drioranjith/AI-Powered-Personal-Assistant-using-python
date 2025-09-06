import requests
from dotenv import load_dotenv
import os

load_dotenv()
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

def get_weather(city):
    """
    Fetch current weather data for a given city (optionally with country).
    :param city: string like "London" or "New York,US"
    :return: formatted weather string or error message
    """
    # Replace spaces with + for URL encoding
    city_query = city.replace(" ", "+")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_query}&appid={OPENWEATHER_API_KEY}&units=metric"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        
        if data.get("cod") == 200:
            weather_desc = data["weather"][0]["description"].capitalize()
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            
            return (f"The weather in {city} is {weather_desc} with temperature {temp}°C, "
                    f"humidity {humidity}%, and wind speed {wind_speed} m/s.")
        else:
            message = data.get("message", "")
            return f"Couldn't find weather for {city}. {message}"
    except requests.RequestException as e:
        return f"Error retrieving weather data: {e}"

def google_search(query):
    """
    Launch a web browser to perform Google search for query.
    :param query: search query string
    :return: confirmation string
    """
    import webbrowser
    try:
        webbrowser.open(f"https://www.google.com/search?q={query.replace(' ', '+')}")
        return f"Here are results for {query}."
    except Exception as e:
        return f"Failed to open web browser: {e}"

def get_news(country='us', category=None):
    url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}"
    if category:
        url += f"&category={category}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        articles = data.get('articles', [])
        if not articles:
            return "Sorry, no news found."
        headlines = [article['title'] for article in articles[:3]]
        return "Here are the top news headlines: " + "; ".join(headlines)
    except requests.RequestException as e:
        return f"Error fetching news: {e}"

