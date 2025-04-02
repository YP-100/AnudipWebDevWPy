# WAP to remove repeated members from a string and print original and resultant string.


input_str = "string and string function"
result_str = ""

print("original string = ", input_str)

for i in input_str.split(" "):
    if i not in result_str:
        result_str += i+" "

print("unique characters = ", result_str)

# WAP deducing multiple string methods.

str1 = "App Dev Using Python @4544"

rstr1 =str1.replace("App","WEB")  #will change the first member of string with the second will change app with web
print(rstr1)

rsstr1 = str1.rstrip("4") #will remove the members of string which are to the right of the first appearing given argument from the right i.e behind
print(rsstr1)

fstr1 = str1.format() #will capatalise all first characters of all members in string
print(fstr1)

cstr = str1.count("4") #will count no of apperance of the argument in the string
print(cstr)