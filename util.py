import json


def open_json():
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)