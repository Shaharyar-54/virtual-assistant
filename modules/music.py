# modules/music.py
import os
import random
import webbrowser

def play_local_music(music_folder="music/"):
    try:
        songs = os.listdir(music_folder)
        if songs:
            song = random.choice(songs)
            song_path = os.path.join(music_folder, song)
            os.startfile(song_path)
            return "Playing music from your local folder."
        else:
            return "No songs found in your music folder."
    except Exception as e:
        return f"Failed to play music: {str(e)}"

def play_youtube_music(song_name="lofi chill beats"):
    webbrowser.open(f"https://www.youtube.com/results?search_query={song_name}")
    return f"Playing {song_name} on YouTube."
