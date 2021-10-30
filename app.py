from flask import Flask, render_template
import os

images_dir = os.path.join('static', 'Images')

app = Flask(__name__)

@app.route('/')
def index() -> None:
    title = 'Pickle Page'

    pickle_files=[]
    for filename in os.listdir(images_dir):
        pickle_files.append(os.path.join(images_dir, filename))

    return render_template('index.html', title=title, pickles=pickle_files, len=len(pickle_files))
