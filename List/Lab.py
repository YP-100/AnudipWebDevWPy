# Write a Python program to get the largest and smallest number from a list without built-in functions. 

numbers = [3, 1, 8, 2, 9, 4, 5, 7]
smallest = numbers[0]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
    elif num < smallest:
        smallest = num

print("Smallest:", smallest)
print("Largest:", largest)

# Write a Python program to find duplicate values from a list and display those.


list = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 3, 9, 1]

duplicates = []
seen = []

for item in list:
    if item in seen and item not in duplicates:
        duplicates.append(item)
    else:
        seen.append(item)

print("Duplicate values:", duplicates)
