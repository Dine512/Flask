import json

from flask import Flask
app = Flask(__name__)

def open_json():
    with open('candidates.json', 'r', encoding='utf-8') as file:
        candidates = json.load(file)
    return candidates

@app.route('/')
def page_index():
    mas =[]
    for candidate in open_json():
        mas.append(f'{candidate["name"]}\n{candidate["position"]}\n{candidate["skills"]}')
    str_ = '\n\n'.join(mas)
    return f'<pre>{str_}<pre>'



@app.route('/candidate/<int:x>')
def profile(x):

    for candidate in open_json():
        if candidate["id"] == x:
            name = candidate["name"]
            position = candidate["position"]
            skills = candidate["skills"]
            picture = candidate["picture"]

            return f'<img src={picture}>' \
                   f'\n\n' \
                   f'<pre>' \
                   f'{name}\n' \
                   f'{position}\n' \
                   f'{skills}' \
                   f'<pre>'


app.run()