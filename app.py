from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__, static_folder='static')

MUSIC_DIR = '/app/music'
ALARM_DIR = '/app/alarms'

@app.route('/')
def index():
    # Sirve el archivo HTML directamente
    return app.send_static_file('index.html')

@app.route('/api/music')
def get_music():
    # Lista los archivos de música disponibles
    files = [f for f in os.listdir(MUSIC_DIR) if f.endswith(('.mp3', '.wav', '.ogg'))]
    return jsonify(files)

@app.route('/api/alarms')
def get_alarms():
    # Lista los archivos de alarma disponibles
    files = [f for f in os.listdir(ALARM_DIR) if f.endswith(('.mp3', '.wav', '.ogg'))]
    return jsonify(files)

@app.route('/music/<path:filename>')
def serve_music(filename):
    return send_from_directory(MUSIC_DIR, filename)

@app.route('/alarms/<path:filename>')
def serve_alarms(filename):
    return send_from_directory(ALARM_DIR, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)