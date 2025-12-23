import pandas as pd
from sklearn.feature_extraction.text  import TfidfVectorizer
from sklearn.linear_model import LogisticRegression 
import pickle
df = pd.read_csv("ml/dataset.csv")

x=df["sentence"]
y= df["label"]

vectorizer =TfidfVectorizer(stop_words="english")
x_vector = vectorizer.fit_transform(x)

model =LogisticRegression(max_iter =300)
model.fit(x_vector,y)

pickle.dump(model, open("ml/model.pkl","wb"))
pickle.dump(vectorizer, open("ml/vectorizer.pkl","wb"))

print("training complete ")