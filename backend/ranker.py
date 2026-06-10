from scoring import calculate_match_score
from skill_extractor import extract_skills


def rank_candidates(resume_list, job_description):
    """
    resume_list = list of dicts:
    [
        {"name": "A", "text": "..."},
        {"name": "B", "text": "..."}
    ]
    """

    ranked_list = []

    for resume in resume_list:
        name = resume["name"]
        text = resume["text"]

        score = calculate_match_score(text, job_description)
        skills = extract_skills(text)

        ranked_list.append({
            "name": name,
            "score": score,
            "skills": skills
        })

    # Sort by score (highest first)
    ranked_list = sorted(ranked_list, key=lambda x: x["score"], reverse=True)

    return ranked_list
