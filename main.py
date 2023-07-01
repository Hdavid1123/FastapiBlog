from fastapi import FastAPI
from os import environ as env

app = FastAPI()

@app.get("/")
def root():
    return {"details":f"Hello, secret sentence = {env['MY_ENV_VARIABLE']}."}
