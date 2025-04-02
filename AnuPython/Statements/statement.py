

student_id = 1002               #assignment statement
print(student_id)

sub1 = 88
sub2 = 78
sub3 = 90
sub4 = 77
sub5 = 88

TotalMks = sub1 + sub2 + sub3 + sub4 + sub5         #expression statement
print(TotalMks)

print("web development using python by anudip foundation")          #print statement


student_name = input("Enter student name: ")        #input statement

print("Hello " + student_name)

dataMember = 88

if dataMember == 100:                                 #conditional statement
    print("data member is greater than 99")
elif dataMember > 99:
    print("data member is equal to 100")
else:
    print("data member is less than 99")

loop_var = 1                                      #loop statement
while loop_var <10:
    if loop_var%2 == 0:
        print("even number : ")
        print(loop_var)
    else: 
        print("odd number : ")
        print(loop_var)
    loop_var += 1

counter = 1                                      #for loop
for counter in range(1, 10):
    if counter%2 == 0:
        print("even number : ")
        print(counter)
    else: 
        print("odd number : ")
        print(counter)
    counter += 1

loop_var2 = 1                                      #while loop
while loop_var2 <10:
    if loop_var2%2 == 0:
        print("even number : ")
        print(loop_var2)
    else: 
        print("odd number : ")
        print(loop_var2)
    loop_var2 += 1

def two_numbers(first, second):                    #function def
    return first + second
result = two_numbers(11, 22)
print(result)

try:                                               #exception handling
    error_log = 10/0
except ZeroDivisionError as e:
    print("cannot divide by zero : " ,e)

for count in range(10):
    if count == 9:
        break
    if count == 3:
        continue
    print(count)