import streamlit as st
import requests

st.title("🧠 Autonomous Resume Screening Agent")

job_description = st.text_area("Enter Job Description")

resumes_input = st.text_area("Enter Resumes (format: Name:Text per line)")

if st.button("Rank Candidates"):

    resumes = []

    lines = resumes_input.split("\n")

    for line in lines:
        if ":" in line:
            name, text = line.split(":", 1)
            resumes.append({"name": name.strip(), "text": text.strip()})

    response = requests.post(
        "http://127.0.0.1:8000/rank",
        json={
            "job_description": job_description,
            "resumes": resumes
        }
    )

    if response.status_code == 200:
        results = response.json()["ranked_candidates"]

        st.subheader("🏆 Ranked Candidates")

        for i, r in enumerate(results, 1):
            st.write(f"{i}. {r['name']} - {r['score']}%")
            st.write(f"Skills: {', '.join(r['skills'])}")
            st.write("---")
