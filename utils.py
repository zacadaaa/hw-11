import json


def load_candidates_from_json() -> list[dict]:
    """Возвращает список всех кандидатов"""
    with open("candidates.json", encoding="utf-8") as f:
        return json.load(f)


def get_candidate(candidate_id: int) -> dict:
    """Возвращает одного кандидата по его id"""
    return [candidate for candidate in load_candidates_from_json() if candidate["id"] == candidate_id][0]


def get_candidates_by_name(candidate_name: str) -> list[dict]:
    """Возвращает кандидатов по имени"""
    candidate_by_name = []
    for candidate in load_candidates_from_json():
        if candidate["name"] == candidate_name:
            candidate_by_name.append(candidate)
    return candidate_by_name


def get_candidates_by_skill(skill_name: str) -> list:
    """Возвращает кандидатов по навыку"""
    candidate_by_skill = []
    for candidate in load_candidates_from_json():
        if skill_name in candidate["skills"].lower().split(', '):
            candidate_by_skill.append(candidate)
    return candidate_by_skill



