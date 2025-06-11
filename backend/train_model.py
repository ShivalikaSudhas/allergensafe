import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

df = pd.read_csv("allergen_dataset.csv")

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["ingredients"])
y = df["contains_allergen"]

model = LogisticRegression()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("✅ Model trained and saved!")
