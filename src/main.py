from fastapi import FastAPI, UploadFile
from ultralytics import YOLO
from PIL import Image
import io

app = FastAPI()

# Load the model when the application starts
model = YOLO('yolov8n.pt')

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/detect/")
async def detect(file: UploadFile):
    # Load the image from the request
    image = Image.open(io.BytesIO(await file.read()))

    # Run inference on the image
    results = model.predict(image)
    print("number of boxes: ")
    print(len(results[0].boxes))
    
    # Get the class index for 'dog'
    dog_index = [k for k, v in results[0].names.items() if v == 'dog'][0]

    # Filter the results to get only the detections of dogs
    dogs = [box for box in results[0].boxes if box.cls == dog_index]

    num_dogs = len(dogs)


    return {"num_dogs": num_dogs}
