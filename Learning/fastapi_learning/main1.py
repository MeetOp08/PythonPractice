from fastapi import FastAPI

app = FastAPI()

@app.get("/students")
def get_Students():
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
    return data


@app.get("/students/jay")
def get_Students():
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
       if i["Name"] == "Jay":
           return i

@app.get("/students/rahul")
def get_Students():
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
        if i["Name"] == "Rahul":
           return i
    else:
        return "Not Exists Data"




    
@app.get("/student/search")
def get_student():

    data = [

        {"Name":"Meet","Age":21,"City":"Vadodara"},
        {"Name":"Raj","Age":22,"City":"Navsari"}

    ]
    for i in data:
        if i["Name"] =="Meet":
            return i
    else:
        return "Student Not Found"
    