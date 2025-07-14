# modules/timer.py
import time
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def set_timer(seconds):
    speak(f"Timer set for {seconds} seconds.")
    time.sleep(seconds)
    speak("Time's up! Your timer has finished.")

def set_alarm(hour, minute):
    speak(f"Alarm set for {hour}:{minute}.")
    while True:
        current_time = time.strftime('%H:%M')
        if current_time == f"{hour}:{minute}":
            speak("Wake up! Your alarm is ringing.")
            break
        time.sleep(30)  # Check every 30 seconds
