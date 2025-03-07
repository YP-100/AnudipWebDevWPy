import csv
import json


#first question solution:


def handlevalues(input_file,default_value):
    with open(input_file,mode="r") as infile:
        reader = csv.reader(infile)
        rows=[row for  row in reader]
    updated_rows=[]
    for row in rows:
        updated_row = [value if value.strip() else default_value for value in row]
        updated_rows.append(updated_row)
        print(updated_row)

handlevalues("missing_data.csv","unknown")

#secound quesion solution:

def read_json(file_path):
    with open(file_path,"r") as file:
        data = json.load(file)
    for item in data:
        if not isinstance(item.get("Product ID"),int):
            print("invalid Product id")
        if not isinstance(item.get("Name"),str):
            print("invalid Name")
        if not isinstance(item.get("Price"),float):
            print("invalid Price")
        

read_json("data.json")

