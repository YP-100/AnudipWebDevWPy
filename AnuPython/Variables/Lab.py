# python program to convert Celsius to Fahrenheit

degree = float(input("Enter temperature in Celsius: "))  
fahrenheit = (degree * 9/5) + 32  
print(fahrenheit)


# area of triangle only using sides
side1 = 5
side2 = 12
side3 = 13
s = (side1+side2+side3) / 2
area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
print(area)
