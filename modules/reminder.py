# modules/reminder.py
import time
import threading
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def set_reminder(task, minutes):
    def reminder_thread():
        time.sleep(minutes * 60)  # minutes -> seconds
        speak(f"Reminder: {task}")

    threading.Thread(target=reminder_thread).start()
