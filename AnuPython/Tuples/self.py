#calculate sum of numbers in given tuple


demo = [(1,2),(3,5),(5,6)]

sum = 0
for i in demo:
    sum = sum+i[0]+i[1]
    # for j in i:
    #     sum = sum + j

print(sum)

#iterate through given tuple

student = (111,"Akash",88.0,"ak@gmail.com","Delhi")

for i in student:
    print(i)

# repeat

example = (1,2)

#result should be (1,2,1,2,1,2,1,2,1,2) -> by using repeat

result = example * 5
print(result)