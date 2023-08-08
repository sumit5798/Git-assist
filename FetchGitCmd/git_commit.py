import subprocess
import spacy

def perform_git_commit(commit_message):
    print(" git commit msg:", commit_message)
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        print("Git commit successful.")
    except subprocess.CalledProcessError as e:
        print("Error during Git commit:", e)

def extract_commit_message(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    
    noun_chunks = [chunk for chunk in doc.noun_chunks]
    commit_message = " ".join(chunk.text for chunk in noun_chunks)
    return commit_message