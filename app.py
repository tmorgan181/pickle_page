from flask import Flask, render_template
import os
import json

images_dir = os.path.join('static', 'Images')
sounds_dir = os.path.join('static', 'pickle_audio')

app = Flask(__name__)

@app.route('/')
def index() -> None:
    title = 'Pickle Page'

    pickle_files=[]
    for filename in os.listdir(images_dir):
        pickle_files.append(os.path.join(images_dir, filename))


    sound_files=[]
    for filename in os.listdir(sounds_dir):
        sound_files.append(os.path.join("..", sounds_dir, filename))
    print(sound_files)

    return render_template('index.html', title=title, pickles=pickle_files, sound_files=json.dumps(sound_files))
