import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Load our converted Kaggle dataset
df = pd.read_csv("ml/kaggle_converted_dataset.csv")

# Drop missing rows (important)
df = df.dropna()

X = df["sentence"]
y = df["label"]

print("Dataset loaded. Samples:", len(df))

# Convert text → vectors
vectorizer = TfidfVectorizer(stop_words="english")
X_vectors = vectorizer.fit_transform(X)

# Train classifier
model = LogisticRegression(max_iter=300)
model.fit(X_vectors, y)

# Save model + vectorizer
pickle.dump(model, open("ml/section_model.pkl", "wb"))
pickle.dump(vectorizer, open("ml/section_vectorizer.pkl", "wb"))

print("Section classifier trained ✔")
print("Saved as section_model.pkl and section_vectorizer.pkl")
