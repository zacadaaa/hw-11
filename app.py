from flask import Flask, render_template
from utils import *

app = Flask(__name__)


@app.route("/")
def page_main():
    candidates: list[dict] = load_candidates_from_json()
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:idx>")
def candidate_page(idx):
    candidate: dict = get_candidate(idx)
    return render_template("card.html", candidate=candidate)


@app.route("/search/<candidate_name>")
def search_candidate_by_name_page(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    return render_template("search.html", candidates=candidates)


@app.route("/skill/<skill_name>")
def search_candidate_by_skill_page(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    return render_template("skill.html", skill=skill_name, candidates=candidates)


app.run()
