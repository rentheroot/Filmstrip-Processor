# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 13:35:26 2023

@author: RENEEEEEEE

To Run: uvicorn api-interface:app --reload
"""

# imports
from fastapi import FastAPI

# init app
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}