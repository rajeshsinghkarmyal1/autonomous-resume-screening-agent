from fastapi import FastAPI
from ranker import rank_candidates

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Autonomous Resume Screening Agent is Running"}

@app.post("/rank")
def rank_resumes(data: dict):
    """
    Expected input format:
    {
        "job_description": "...",
        "resumes": [
            {"name": "A", "text": "..."},
            {"name": "B", "text": "..."}
        ]
    }
    """

    job_description = data["job_description"]
    resumes = data["resumes"]

    result = rank_candidates(resumes, job_description)

    return {"ranked_candidates": result}
