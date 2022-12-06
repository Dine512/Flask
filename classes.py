from util import open_json


class GetCandidates:
    def __init__(self, list_candidates):
        self.list_candidates = list_candidates

    def get_all(self):
        mas = []
        for candidate in self.list_candidates:
            mas.append(f'{candidate["name"]}\n{candidate["position"]}\n{candidate["skills"]}')
        return '\n\n'.join(mas)

    def get_x_candidat(self, x):
        for candidate in self.list_candidates:
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

