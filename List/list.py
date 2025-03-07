first_list = [11,12,13,14,15,16]

print(first_list[0])
print(first_list[1])
print(first_list[2])
print(first_list[3])
print(first_list[4])
print(first_list[5])

sub_list = first_list[1:3]
print(sub_list)
sub_list2 = first_list[2:]
print(sub_list2)
sub_list3 = first_list[::2]          #adds gap between elements
print(sub_list3)

first_list[0] = 100
print(first_list)