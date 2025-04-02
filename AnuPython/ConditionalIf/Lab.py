

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


# price for distance

#  WAP to find out fare  for a user 
#   Take KM wise  distance travelled as input
#  Rate per KM : (0 to 10 ): 10 rs / (10-20 ): 5 rs / (above 20 ) : 4 rs.

fare = 0
km = int(input("Enter distance traveled in KM: "))

if(km <= 10):
    fare = km * 10
elif(km <= 20):
    fare = (10 * 10) + (km - 10) * 5
elif(km > 20):
    fare = (10 * 10) + (10 * 5) + (km - 20) * 4
else:
    print("Enter Valid Number")

print("Total Fare: RS - ", fare)