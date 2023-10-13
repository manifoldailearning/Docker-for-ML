from fastapi import FastAPI 
import joblib
import uvicorn


model_name = 'final_model.pkl'
model = joblib.load(model_name)

app = FastAPI() 
# my_first_api = FastAPI() 
# path
# POST, PUT, DELETE, GET
# @my_first_api.get("/")
@app.get("/") # path operation decorator
async def root():
    return {"message":"Hello from FASTAPI - IRIS Model"}

@app.get("/predict") # path operation decorator
def predict(feat1:float ,feat2:float, feat3:float,feat4:float):
    data = [[feat1,feat2,feat3,feat4]]
    result = model.predict(data)
    return {"prediction":result}

if __name__== "__main__":
    uvicorn.run(app, host="0.0.0.0",port=8000)


# POST: to create data.
# GET: to read data.
# PUT: to update data.
# DELETE: to delete data.

# @app.post()
# @app.put()
# @app.delete()