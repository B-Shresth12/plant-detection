import asyncio
from fastapi import FastAPI, UploadFile, File, Form
from grpc_client import classify_disease
from PIL import Image
import io

app = FastAPI()


@app.post("/predict")
async def classify_disease_endpoint(
    crop: str = Form(...),
    image: UploadFile = File(...)
):
    image_data = await image.read()
    response = classify_disease(crop, image_data)

    return response
