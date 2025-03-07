import json

def read_json(file_path):
    with open(file_path,"r") as file:
        data = json.load(file)
    for item in data:
        if not isinstance(item.get("stud_id"),int):
            print("invalid student id")
        if not isinstance(item.get("stud_name"),str):
            print("invalid student name")
        if not isinstance(item.get("stud_fees"),float):
            print("invalid fees format")
        

read_json("jsondemo.json")