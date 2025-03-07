
# 1. WAP to create a tuple and append another tuple to it get the count of total members & repeated members similarly print length of this new tuple

# Creating a tuple
tup1 = (1, 2, 3, 4, 5, 2, 3)
tup2 = (6, 7, 3, 2, 8)
new_tup = tup1 + tup2
total_members = len(new_tup)
checked = []
repeated_members = {}

for item in new_tup:
    if item not in checked:
        count = new_tup.count(item)
        if count > 1:
            repeated_members[item] = count
        checked.append(item)

print("New Tuple:", new_tup)
print("Total Members:", total_members)
print("Repeated Members:", repeated_members)
print("Length of New Tuple:", len(new_tup))


#  WAP to to deduce use of sorting in tuples.

tup = (9, 5, 2, 8, 3, 1)
sorted_tup = tuple(sorted(tup))

print("Original Tuple:", tup)
print("Sorted Tuple:", sorted_tup) #will sort the tuple in an order
