
import requests
import os
from dotenv import load_dotenv

load_dotenv() 

def get_news():
    try:
        api_key = os.getenv("NEWS_API_KEY")
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
        response = requests.get(url)
        data = response.json()

        print(data)  # 🔍 Debug print

        articles = data.get("articles")

        if articles:
            headlines = [article['title'] for article in articles[:5]]
            return "Here are the top news headlines: " + ', '.join(headlines)
        else:
            return "No news found or invalid API key."
    except Exception as e:
        return f"Failed to fetch news: {str(e)}"
