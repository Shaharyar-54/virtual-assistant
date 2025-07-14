# # assistant.py
# import speech_recognition as sr
# import pyttsx3
# import datetime
# import webbrowser
# import os
# import wikipedia
# import requests

# engine = pyttsx3.init()

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# def listen():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         audio = r.listen(source)
#     try:
#         command = r.recognize_google(audio)
#         print(f"User said: {command}")
#     except:
#         speak("Sorry, I did not understand.")
#         return ""
#     return command.lower()

# def handle_command(command):
#     if 'open google' in command:
#         webbrowser.open("https://www.google.com")
#         speak("Opening Google.")
#     elif 'open youtube' in command:
#         webbrowser.open("https://www.youtube.com")
#         speak("Opening YouTube.")
#     elif 'time' in command:
#         now = datetime.datetime.now().strftime('%I:%M %p')
#         speak(f"Current time is {now}")
#     elif 'date' in command:
#         today = datetime.datetime.now().strftime('%B %d, %Y')
#         speak(f"Today's date is {today}")
#     elif 'wikipedia' in command:
#         topic = command.replace('wikipedia', '').strip()
#         result = wikipedia.summary(topic, sentences=2)
#         speak(result)
#     elif 'play music' in command or 'play songs' in command:
#         response = play_local_music()
#         speak(response)
#     elif 'play' in command and 'on youtube' in command:
#         song_name = command.replace('play', '').replace('on youtube', '').strip()
#         response = play_youtube_music(song_name)
#         speak(response)
#     elif 'weather' in command:
#         speak("Which city?")
#         city = listen()
#         weather_info = get_weather(city)
#         speak(weather_info)
#     elif 'news' in command:
#         news_info = get_news()
#         speak(news_info)
#     elif 'set reminder' in command:
#         speak("What should I remind you about?")
#         task = listen()
#         speak("In how many minutes?")
#         minutes_input = listen()
#         try:
#             minutes = int(minutes_input)
#             set_reminder(task, minutes)
#             speak(f"Reminder set for {task} in {minutes} minutes.")
#         except ValueError:
#             speak("Sorry, I could not understand the time.")
#     elif 'chat' in command or 'talk' in command:
#         speak("Sure, what would you like to talk about?")
#         prompt = listen()
#         if prompt:
#             reply = chat_with_ai(prompt)
#             if reply:
#                 print(f"AI: {reply}")
#     else:
#         webbrowser.open(f"https://www.google.com/search?q={command}")
#         speak(f"Here’s what I found for {command}")

# # assistant.py (update)
# from modules.music import play_local_music, play_youtube_music

# def handle_command(command):
#     if 'play music' in command or 'play songs' in command:
#         response = play_local_music()
#         speak(response)

#     elif 'play' in command and 'on youtube' in command:
#         song_name = command.replace('play', '').replace('on youtube', '').strip()
#         response = play_youtube_music(song_name)
#         speak(response)

#     # (baaki commands as it is)
# # assistant.py (update)
# from modules.weather import get_weather
# from modules.news import get_news

# def handle_command(command):
#     if 'weather' in command:
#         speak("Which city?")
#         city = listen()
#         weather_info = get_weather(city)
#         speak(weather_info)

#     elif 'news' in command:
#         news_info = get_news()
#         speak(news_info)

#     # (baaki commands music, search, etc.)

# from modules.reminder import set_reminder

# def handle_command(command):
  

#     if 'set reminder' in command:
#         speak("What should I remind you about?")
#         task = listen()
#         speak("In how many minutes?")
#         minutes_input = listen()
#         try:
#             minutes = int(minutes_input)
#             set_reminder(task, minutes)
#             speak(f"Reminder set for {task} in {minutes} minutes.")
#         except ValueError:
#             speak("Sorry, I could not understand the time.")



#            # assistant.py (updated)
# from modules.smart_chat import chat_with_ai

# def handle_command(command):
#     # Handle various command cases
#     if 'chat' in command or 'talk' in command:
#         speak("Sure, what would you like to talk about?")
#         prompt = listen()
#         if prompt:
#             reply = chat_with_ai(prompt)
#             if reply:
#                 print(f"AI: {reply}")
#     # Add other command handling logic as needed
#     else:
#         # Handle other types of commands
#         pass



# # assistant.py (updated)
# from modules.timer import set_timer, set_alarm

# def handle_command(command):
#     # Handle existing features

#     if 'chat' in command or 'talk' in command:
#         speak("Sure, what would you like to talk about?")
#         prompt = listen()
#         if prompt:
#             reply = chat_with_ai(prompt)
#             if reply:
#                 print(f"AI: {reply}")
    
#     elif 'set timer' in command:
#         speak("For how many seconds?")
#         seconds_text = listen()
#         if seconds_text.isdigit():
#             seconds = int(seconds_text)
#             set_timer(seconds)
#         else:
#             speak("Please say a number.")
    
#     elif 'set alarm' in command:
#         speak("At what time? Please say in hour and minute format like '15 30' for 3:30 PM.")
#         time_text = listen()
#         try:
#             hour, minute = map(int, time_text.split())
#             set_alarm(hour, minute)
#         except:
#             speak("Sorry, I didn't understand the time format.")



# assistant.py
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import wikipedia
from modules.weather import get_weather
from modules.news import get_news
from modules.music import play_local_music, play_youtube_music
from modules.reminder import set_reminder
from modules.smart_chat import chat_with_ai
from modules.timer import set_timer, set_alarm

# Initialize the assistant
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source)  # optional but helps in noise
            audio = r.listen(source)
    except Exception as e:
        print(f"Microphone error: {e}")
        speak("Sorry, I am unable to access the microphone.")
        return ""

    try:
        command = r.recognize_google(audio)
        print(f"User said: {command}")
    except sr.UnknownValueError:
        speak("Sorry, I did not understand.")
        return ""
    except sr.RequestError:
        speak("Sorry, I could not reach the recognition service.")
        return ""

    return command.lower()
def handle_command(command):
    if 'open google' in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")

    elif 'open youtube' in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")

    elif 'time' in command:
        now = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"Current time is {now}")

    elif 'date' in command:
        today = datetime.datetime.now().strftime('%B %d, %Y')
        speak(f"Today's date is {today}")

    elif 'wikipedia' in command:
        topic = command.replace('wikipedia', '').strip()
        result = wikipedia.summary(topic, sentences=2)
        speak(result)

    elif 'play music' in command or 'play songs' in command:
        response = play_local_music()
        speak(response)

    elif 'play' in command and 'on youtube' in command:
        song_name = command.replace('play', '').replace('on youtube', '').strip()
        response = play_youtube_music(song_name)
        speak(response)

    elif 'weather' in command:
        speak("Which city?")
        city = listen()
        weather_info = get_weather(city)
        speak(weather_info)

    elif 'news' in command:
        news_info = get_news()
        speak(news_info)

    elif 'set reminder' in command:
        speak("What should I remind you about?")
        task = listen()
        speak("In how many minutes?")
        minutes_input = listen()
        try:
            minutes = int(minutes_input)
            set_reminder(task, minutes)
            speak(f"Reminder set for {task} in {minutes} minutes.")
        except ValueError:
            speak("Sorry, I could not understand the time.")



 

    elif 'chat' in command or 'talk' in command:
        speak("Sure, what would you like to talk about?")
        prompt = listen()
        if prompt:
            reply = chat_with_ai(prompt)
            if reply:
                speak(reply)


    
                

    elif 'set timer' in command:
        speak("For how many seconds?")
        seconds_text = listen()
        if seconds_text.isdigit():
            seconds = int(seconds_text)
            set_timer(seconds)
            speak(f"Timer set for {seconds} seconds.")
        else:
            speak("Please say a number.")

    elif 'set alarm' in command:
        speak("At what time? Please say in hour and minute format like '15 30' for 3:30 PM.")
        time_text = listen()
        try:
            hour, minute = map(int, time_text.split())
            set_alarm(hour, minute)
            speak(f"Alarm set for {hour}:{minute}.")
        except:
            speak("Sorry, I didn't understand the time format.")

    else:
        webbrowser.open(f"https://www.google.com/search?q={command}")
        speak(f"Here’s what I found for {command}")

# Main loop to run the assistant
def run_assistant():
    speak("Hello, I am your virtual assistant. How may I help you?")
    while True:
        command = listen()
        if 'exit' in command or 'stop' in command:
            speak("Goodbye, have a nice day!")
            break
        handle_command(command)

if __name__ == "__main__":
    run_assistant()
