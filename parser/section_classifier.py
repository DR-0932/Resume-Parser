import pickle

# Load trained model + vectorizer
model = pickle.load(open("ml/section_model.pkl", "rb"))
vectorizer = pickle.load(open("ml/section_vectorizer.pkl", "rb"))

def classify_sentence(sentence):
    vec = vectorizer.transform([sentence])
    return model.predict(vec)[0]
