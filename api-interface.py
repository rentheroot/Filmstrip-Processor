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
    start_point: tuple[int, int] = []
    end_point: tuple[int, int] = []

# add new segment data to image
@app.put("/api/segment-image/{image_id}")
async def add_segmentation(image_id : int, subdivision : Subdivision):
    return {"im ID": image_id, "sub" : subdivision}