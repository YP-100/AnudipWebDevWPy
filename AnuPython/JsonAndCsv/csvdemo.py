import csv

def handlevalues(input_file,default_value):
    with open(input_file,mode="r") as infile:
        reader = csv.reader(infile)
        rows=[row for  row in reader]
    updated_rows=[]
    for row in rows:
        updated_row=[value if value !=" " else default_value for value in row]       #type ignore
        updated_rows.append(updated_row)
        print(updated_row)

handlevalues("csvdemo.csv","unknown")
