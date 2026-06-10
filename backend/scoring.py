from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_match_score(resume_text, job_description):
    """
    Returns similarity score between resume and job description
    """

    documents = [resume_text, job_description]

    # Convert text to numerical vectors
    tfidf = TfidfVectorizer(stop_words='english')
    matrix = tfidf.fit_transform(documents)

    # Compute similarity
    score = cosine_similarity(matrix[0:1], matrix[1:2])[0][0]

    return round(score * 100, 2)
