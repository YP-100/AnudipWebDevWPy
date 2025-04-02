def fact(num):
    result = 1
    while(num>1):
        result = result * num
        num -= 1
    return result

numm = int(input("Enter a number: "))
print(fact(numm))