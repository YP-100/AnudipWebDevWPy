

#get palindrome number or not 

def rev(num):
    rev = 0
    while(num>0):
        rem = num%10
        rev = rev*10+rem
        num = num//10
    return rev

num = int(input("Enter a number: "))
cpalin = num
if(rev(num) == cpalin):                     #checks if reverse of number = original
    print("Number is palindrome")
else:
    print(rev(num))