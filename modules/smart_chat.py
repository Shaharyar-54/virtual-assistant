
import requests
import pyttsx3
import os
from dotenv import load_dotenv


load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Speaks the given text aloud."""
    engine.say(text)
    engine.runAndWait()

def chat_with_ai(prompt):
    """Sends the prompt to Gemini API and returns spoken response."""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        print("Status Code:", response.status_code)
        response_data = response.json()
        print("Response Data:", response_data)

        # Extract AI's reply
        reply = response_data['candidates'][0]['content']['parts'][0]['text']
        speak(reply)
        return reply

    except Exception as e:
        error_msg = f"Error talking to Gemini AI: {str(e)}"
        print(error_msg)
        speak("Sorry, I couldn't process your request.")
        return error_msg
