from fastapi import FastAPI

app = FastAPI()

#http://127.0.0.1:8000/students?city=vadodara
# @app.get("/students")
# def get_students(city: str):
#     return {"City": city}


#http://127.0.0.1:8000/students/search?City=Surat
@app.get("/students/search")
def get_Students(City:str):
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
    result = []
    for i in data:
        if i["City"] == City:
           result.append(i)
    

    return result


