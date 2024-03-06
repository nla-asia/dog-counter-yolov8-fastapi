import random
from fastapi import FastAPI, UploadFile


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/detect/")
async def detect(file: UploadFile):
  

    num_dogs = random.randint(0, 100)


    return {"num_dogs": num_dogs}
