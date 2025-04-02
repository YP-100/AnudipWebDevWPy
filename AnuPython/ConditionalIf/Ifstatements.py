
# if demo1                                      **********************************************

num1 = float(input("Enter first number: "))

if num1 > 0:
    print("Positive number")
elif num1 == 0:
    print("Zero")
else:
    print("Negative number")

# if demo2                                      **********************************************

num11 = 22
num22 = 44
num33 = 51
if(num11 > num22) and (num11 > num33):
    greatest = num11
elif(num22 > num11) and (num22 > num33):
    greatest = num22
else:
    greatest = num33
print("The greatest number is", greatest)

#secound solution 

if(num11>num22>num33):
    greatest = num11
elif(num22>num11>num33):
    greatest = num22
else:
    greatest = num33
print("The greatest number is", greatest)

#greatest out of 4 without and             ***********************************************

num111 = 224
num222 = 44
num333 = 514
num444 = 88

if num111 > num222:
    if num111 > num333:
        if num111 > num444:
            greatest = num111
        else:
            greatest = num444
    else:
        if num333 > num444:
            greatest = num333
        else:
            greatest = num444
else:
    if num222 > num333:
        if num222 > num444:
            greatest = num222
        else:
            greatest = num444
    else:
        if num333 > num444:
            greatest = num333
        else:
            greatest = num444

print("The greatest number is", greatest)


#finding out leap year                            **********************************************

year = int(input("Enter year: "))
if(year > 0):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")
else:
    print("Invalid year")
