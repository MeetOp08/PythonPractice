
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"Message":"FastAPI is working"}


@app.get("/students")
def get_student():
    data = {
        "Name":["Meet","Raj","Jay","Jainil"],
        "Marks":[24,28,25,29]
    }
    return data

@app.get("/details")
def get_details():
    data = {
        "City":["Vadodara","Navsari","Surat","Ankleshwer"],
    }
    return data