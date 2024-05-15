import uvicorn
import requests
import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from typing import Dict


DJANGO_API_BASE_URL = "http://localhost:8001/"


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def hello():
    return {
        "hello": "world"
    }


@app.get("/items/{key}")
def get_key(key):
    try:
        res = requests.get(DJANGO_API_BASE_URL + f'/dictionaries/{key}/')
    except:
        return Response(status_code=500, content={"message": "something went wrong"})
    if res.status_code == 200:
        return res.json()
    elif res.status_code == 404:
        return Response(
            status_code=404,
            content=json.dumps({"message": "Item not found"})
        )


@app.post('/items')
def set_key(data: Dict[str, str]):
    try:
        res = requests.post(DJANGO_API_BASE_URL + '/dictionaries/', json=data)
    except:
        return Response(
            status_code=500,
            content=json.dumps({"message": "something went wrong"})
        )
    return res.json()


@app.put("/items/{key}")
def update_key(key, data: Dict[str, str]):
    try:
        res = requests.put(DJANGO_API_BASE_URL +
                           f'/dictionaries/{key}/', json=data)
    except:
        return Response(status_code=500, content={"message": "something went wrong"})
    if res.status_code == 200:
        return res.json()
    elif res.status_code == 404:
        return Response(
            status_code=404,
            content=json.dumps({"message": "Item not found"})
        )


@app.delete("/items/{key}")
def delete_key(key):
    try:
        res = requests.delete(DJANGO_API_BASE_URL + f'/dictionaries/{key}/')
    except:
        return Response(status_code=500, content="something went wrong")
    return res.json()


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
