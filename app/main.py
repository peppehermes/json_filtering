from fastapi import FastAPI, HTTPException
from lib.json_lib import filter_json

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/filter")
def filter_json():
    return HTTPException(status_code=405, detail="not implemented")
