from fastapi import FastAPI, Depends, HTTPException, status, File, UploadFile, Form
from database import get_db
from sqlalchemy.orm import Session
from mongo import connect_to_mongo
import gridfs
from typing import Annotated

app = FastAPI()

# Establish connection
client = connect_to_mongo()

# Access database and collection
db = client['project']
collection = db['models']
fs= gridfs.GridFS(db)


import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url

# Configuration       
cloudinary.config( 
    cloud_name = "djxq0ohdx", 
    api_key = "986771533288669", 
    api_secret = "9A5ngvyOq8urOsm-2Y_4upBB8xY", # Click 'View API Keys' above to copy your API secret
    secure=True
)



@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/models")
async def add_models(
):
    upload_result = cloudinary.uploader.upload("Projectile-project.mp4", public_id="projectile")
    print(upload_result["secure_url"])
    
    
    return file
    

