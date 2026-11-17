from fastapi import FastAPI

app = FastAPI()


@app.get("/students/{name}")
def get_student(name):

    data = [
                {
                    "Name":"Meet",
                    "Age":21,
                    "City":"vadodara"
                },
                {
                    "Name":"Raj",
                    "Age":22,
                    "City":"Navsari"
                },
                {
                    "Name":"Jay",
                    "Age":21,
                    "City":"Surat"
                },
                {
                    "Name":"Jainil",
                    "Age":22,
                    "City":"Ankleshwer"
                },
                {
                    "Name":"Rahul",
                    "Age":30,
                    "City":"Ahmedabad"
                }            
    ]

    for i in data:
        if i['Name'] == name:
            return i
    else:
        return "Student Not Found"