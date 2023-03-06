# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 13:35:26 2023

@author: RENEEEEEEE

To Run: uvicorn api-interface:app --reload
"""

# imports
from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
from contextlib import closing

# init backend db
projectDb = "project.db"

# init app
app = FastAPI()

# Define image subsection / mask area
# formatted for cv2.rectangle
class Subdivision(BaseModel):
    id: int
    start_point: tuple[int, int] = []
    end_point: tuple[int, int] = []
    
# add new segment data to image
@app.post("/api/segment-image/{image_id}")
async def add_segmentation(image_id : int, subdivision : Subdivision):
    return {"im ID": image_id, "sub" : subdivision}

# add new segment data to image
@app.put("/api/segment-image/{image_id}")
async def update_segmentation(image_id : int, subdivision : Subdivision):
    return {"im ID": image_id, "sub" : subdivision}

# initiate database with correct tables
@app.get("/api/init-db")
async def check_tables():
    with closing(sqlite3.connect(projectDb)) as connection:
        with closing(connection.cursor()) as cursor:
            
            # check if table already exists
            sql_query = "SELECT name FROM sqlite_master WHERE type='table';"
            cursor.execute(sql_query)
            res = cursor.fetchall()
            if res == []:
                cursor.execute("CREATE TABLE segments (image_id INTEGER, segment_id INTEGER, start_point BLOB, end_point BLOB)")
                return({"status": "table added"})
            else:
                return({"status": "table already exists"})