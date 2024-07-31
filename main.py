from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os
app = FastAPI()

def content(color:str):
    return f"<body style=\"background-color:{color};\"></body>"

@app.get("/")
async def root():
    color = os.environ["COLOR"] 
    return HTMLResponse(content=content(color),status_code = 200)#HTML Code that means success.