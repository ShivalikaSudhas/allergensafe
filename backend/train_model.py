import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Load data
df = pd.read_csv("allergen_dataset.csv")

# Vectorize ingredients
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["ingredients"])
y = df["contains_allergen"]

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model and vectorizer
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Model trained and saved!")
