from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from typing import List
from fastapi import FastAPI, Path, Query
import json


app = FastAPI()


f = open('d.json')
var =json.load(f)
@app.get("/")
def home():
    return {"Hello":"welcome"}


@app.get("/query")
def show(page_no:int = Query(None,description="Show page ",le=2,gt=0)):
    for new in var:
        if new["page"]== page_no:
          return new
    

@app.get("/queryforuser")
def id(id_value:int = Query(None,description="Show id"),le=12,gt=7):
    for new in var:
        for neww in new["data"]:
          if neww["id"]==id_value:
              return neww
              
              

   


