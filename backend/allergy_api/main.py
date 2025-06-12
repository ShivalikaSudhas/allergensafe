from fastapi import FastAPI
from .schemas.allergen_schema import TextInput
from .utils.check_allergen import check_for_allergens

app = FastAPI()

@app.get("/")
def read_root():
    return {"MESSAGE": "ALLERGY DETECTION API IS RUNNING 🚀"}

@app.post("/predict")
def predict_ingredients(data: TextInput):
    results = check_for_allergens(data.text)
    return {"input": data.text, "allergens_detected": results}
