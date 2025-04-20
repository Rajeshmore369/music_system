from flask import Flask, render_template, request, jsonify
import pygame
import os

app = Flask(__name__)

# Initialize mixer
pygame.mixer.init()

# List all mp3 files from 'music' folder
music_folder = os.path.join(os.getcwd(), 'music')
songs = [f for f in os.listdir(music_folder) if f.endswith('.mp3')]

# Keep track of current song index
current_index = 0

@app.route("/")
def index():
    return render_template("index.html", songs=songs)

@app.route("/play", methods=["POST"])
def play_song():
    global current_index
    song_path = os.path.join(music_folder, songs[current_index])
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()
    return jsonify({"status": "playing", "song": songs[current_index]})

@app.route("/pause", methods=["POST"])
def pause_song():
    pygame.mixer.music.pause()
    return jsonify({"status": "paused"})

@app.route("/unpause", methods=["POST"])
def unpause_song():
    pygame.mixer.music.unpause()
    return jsonify({"status": "unpaused"})

@app.route("/next", methods=["POST"])
def next_song():
    global current_index
    current_index = (current_index + 1) % len(songs)
    song_path = os.path.join(music_folder, songs[current_index])
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()
    return jsonify({"status": "playing", "song": songs[current_index]})

@app.route("/previous", methods=["POST"])
def previous_song():
    global current_index
    current_index = (current_index - 1) % len(songs)
    song_path = os.path.join(music_folder, songs[current_index])
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()
    return jsonify({"status": "playing", "song": songs[current_index]})

if __name__ == "__main__":
    app.run(debug=True)
