import spacy

def process_command(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    
    for token in doc:
        if token.pos_ == "VERB":
            verb = token.text
            return verb
    return None
