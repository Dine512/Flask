from flask import Flask
from classes import GetCandidates
from util import open_json

app = Flask(__name__)

f = GetCandidates(open_json())


@app.route('/')
def page_index():
    return f'<pre>{f.get_all()}<pre>'


@app.route('/candidate/<int:x>')
def profile(x):
    return f.get_x_candidat(x)


app.run()
