

#electricity bill:


# Household = 2
# Smallbusiness = 5
# Industrialpurpose = 10


total = 0
print("Enter 1 Household")
print("Enter 2 for SmallBusiness")
print("Enter 3 for IndustrialPurpose")
type = int(input("Enter the type of user : "))

rate = float(input("Enter rate of electricity consumption per month : "))

if(type == 1):
    total = rate * 2
elif(type ==2 ):
    total = rate * 5
elif(type == 3):
    total = rate * 10
else:
    print("Enter Valid Number")

print("Your Total Rate = ",total)