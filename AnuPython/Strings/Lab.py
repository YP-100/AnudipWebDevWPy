
# WAP to print count of uppercase, lowercase, numbers and special characters in a string print count seperately.


str = "Web Dev Using Python @4544"
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



#functions on string
str1 = "Web Dev Using Python @4544"
ustr1 = str1.upper()                       #an string function upper is used to change the string to upper case
print(ustr1)

lstr1 = str1.lower()                       #an string function lower is used to change the string to lower case
print(lstr1)

cstr1 = str1.capitalize()                   #an string function that will capatilise the first character of the string
print(cstr1)

castr1 = str.casefold()                      #an string function that will decapatilise all the characters of the string
print(castr1)