from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index() -> None:
    title = 'Pickle Page'
    return render_template('index.html', title=title)
