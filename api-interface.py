# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 13:35:26 2023

@author: RENEEEEEEE

To Run: uvicorn api-interface:app --reload
"""

# imports
from fastapi import FastAPI
from pydantic import BaseModel

# init app
app = FastAPI()

# Define image subsection / mask area
# formatted for cv2.rectangle
class Subdivision(BaseModel):
    id: int
    start_point: tuple[int] = []
    end_point: tuple[int] = []

@app.get("/")
async def root():
    return {"message": "Hello World"}