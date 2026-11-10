from fastapi import FastAPI
import joblib
import uvicorn

# Trained in Untitled.ipynb. requirements.txt pins scikit-learn==1.2.2,
# the version that wrote final_model.pkl.
model_name = "final_model.pkl"
model = joblib.load(model_name)

app = FastAPI()

# path
# POST, PUT, DELETE, GET
@app.get("/")  # path operation decorator
async def root():
    return {"message": "Hello from FASTAPI - IRIS Model"}


@app.get("/predict")  # path operation decorator
def predict(feat1: float, feat2: float, feat3: float, feat4: float):
    data = [[feat1, feat2, feat3, feat4]]
    result = model.predict(data)
    # predict() returns a numpy array, which JSON cannot encode directly.
    return {"prediction": result.tolist()}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


# POST: to create data.
# GET: to read data.
# PUT: to update data.
# DELETE: to delete data.
