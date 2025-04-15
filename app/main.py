from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, List
from lib.json_lib import filter_json

app = FastAPI()

class FilterRequest(BaseModel):
    data: Dict[str, Any]
    filter: Dict[str, List[str]]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/filter")
async def filter_json_endpoint(request: FilterRequest):
    try:
        filtered_data = filter_json(request.data, request.filter)
        return filtered_data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
