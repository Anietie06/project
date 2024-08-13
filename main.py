from fastapi import FastAPI, Depends, HTTPException, status, File, UploadFile
from database import get_db
from sqlalchemy import Session
from file_models import File
from mongo import connect_to_mongo

app = FastAPI()

# Establish connection
client = connect_to_mongo()

# Access database and collection
db = client['project']
collection = db['models']


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/models")
async def add_models(
    filename: str,
    file: UploadFile,
    description: str = None,
    db: Session = Depends(get_db)
):
    
    document = {'name': 'Alice', 'age': 30}
    collection.insert_one(document)
    
    return file