

# string demo 1

str = "App Dev Web Using Python @4544"
print("My string : " ,  str)

upr,lwr,num,spl = 0,0,0,0
for i in str:
    if(i.isupper()):
        upr+=1
    elif(i.islower()):
        lwr+=1
    elif(i.isdigit()):
        num+=1
    else:
        spl+=1
print("Uppercase : ",upr)
print("Lowercase : ",lwr)   
print("Numbers : ",num)
print("Special characters : ",spl)


# string demo 2

dempstr = "Welcome to Topic on Strings"

count = 0
for i in dempstr:
    if(i == "A" or i == "E" or i == "I" or i == "O" or i == "U" or i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):   
        count += 1

print("Number of Vowels : ",count)


# string demo 3

input_str = "string and string function"
result_str = ""

print("original string = ", input_str)

for i in input_str.split(" "):
    if i not in result_str:
        result_str += i+" "

print("unique characters = ", result_str)