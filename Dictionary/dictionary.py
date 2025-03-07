employee = {
    "employee_id": 111,
    "name": "shivam",
    "salary": 50000
}

first_dict = dict(name = "akbar", age = 20 , gender = "male")           #dictionary using dict function

print(first_dict)

# dictionary demo                                                     **********************************************

num = {1:19,2:22,3:83,4:44,5:5,6:64,7:64,8:55,9:69,10:1055}
print("key, values :")
for key,value in num.items():
    print(key,",",value)

#dictionary demo2                                                       **********************************************

first = {1:96,2:69}
second = {3:44,4:55}
third = {5:66,6:77}

fourth = {}

for i in (first,second,third):
    fourth.update(i)

print(fourth)

#dictionary demo3                                                       **********************************************

test = {"A":6, "B":9, "C":5, "D":7, "E":4}
res = 0

for val in test.values():
    res += val
Avg = res/len(test)
print("sum of values : ", res)
print("Average of values : ", Avg)

#dictionary demo4                                                       **********************************************
new_dict = {5: 67,6: 55,7: None,8: None,9: None, 10: 87}
print(new_dict)


for key,value in list(new_dict.items()):
    del new_dict[key]

print("Empty dictionary : ")
print(new_dict)