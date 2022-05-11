import json
from flask import Flask

app = Flask(__name__)

with open('candidates.json', encoding='utf-8') as file:
    file = json.load(file)


@app.route("/")
def page_index():
    person = """"""
    for i in file:
        name = (i['name'])
        position = (i['position'])
        skills = (i['skills'])
        person += f"""
Имя кандидата - {name}
Позиция кандидата - {position}
Навыки через запятую - {skills}
"""
    return f'<pre>{person}</pre>'


@app.route("/candidates/<x>")
def candidate_img(x):
    for i in file:
        if i['id'] == int(x):
            name = (i['name'])
            position = (i['position'])
            skills = (i['skills'])
            candidate = f"""
Имя кандидата - {name}
Позиция кандидата - {position}
Навыки через запятую - {skills}
"""

    return f'<img src = "https://picsum.photos/200"> <br /><pre> {candidate}</pre>'


@app.route("/skills/<x>")
def candidate_skills(x):
    candidate = """"""
    for i in file:
        if x in i['skills'].lower().split(', '):
            name = (i['name'])
            position = (i['position'])
            skills = (i['skills'])
            candidate += f"""
Имя кандидата - {name}
Позиция кандидата - {position}
Навыки через запятую - {skills}
"""
    return f'<pre>{candidate}</pre>'

app.run()
