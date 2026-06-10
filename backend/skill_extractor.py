import re

# Predefined skill list (you can expand later)
SKILL_DB = [
    "python", "java", "c++", "sql", "machine learning",
    "deep learning", "nlp", "flask", "fastapi",
    "django", "aws", "azure", "docker",
    "git", "pandas", "numpy", "tensorflow", "pytorch"
]

def extract_skills(resume_text):
    resume_text = resume_text.lower()
    found_skills = []

    for skill in SKILL_DB:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, resume_text):
            found_skills.append(skill)

    return list(set(found_skills))
