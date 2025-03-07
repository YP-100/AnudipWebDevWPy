
# tuple demo 1***********************************************

first_tup = (1,2,3,4)                                    #tuple creation
print("Tuple : ",first_tup)

list1 = [11,12,13,14]

secound_tup = tuple(list1)                               #converting list to tuple
print("Tuple 2: ",secound_tup)

str1 = "my python programming"
third_tuple = tuple(str1)                                #converting string to tuple
print("Tuple 3: ",third_tuple)

fourth_tuple = ()                                        #empty tuple
print("Tuple 4: ",fourth_tuple)

# tuple demo 2***********************************************

tup1 = (1,2,3,4,5)
first_mem = tup1[0]                                        #tuple indexing
secound_mem = tup1[1]
last_mem = tup1[-1]                                        #negative indexing
slast_mem = tup1[-2]

print("First member : ",first_mem)
print("Secound member : ",secound_mem)
print("Last member : ",last_mem)
print("Secound last member : ",slast_mem)


slice_tup = tup1[1:3]                                      #tuple slicing
print("Slice tup : ",slice_tup)

# tuple demo 3***********************************************

new_tup = (11,"python",22.88,"script",7)

print("First member : ",new_tup[0])
print("Secound member : ",new_tup[1])
print("Third member : ",new_tup[2])
print("Fourth member : ",new_tup[3])
print("Fifth member : ",new_tup[4])

for i in new_tup:
    print(i)

# tuple demo 4***********************************************

tuple1 = (1,2,3,4,5)
tuple2 = (100,200,300,400,500)

add_tuple = tuple1 + tuple2                               #tuple concatenation
print(add_tuple)

length = len(add_tuple)                                      #tuple length
print(length)

minimum = min(add_tuple)                                     #tuple minimum
print(minimum)

maximum = max(add_tuple)                                     #tuple maximum
print(maximum)

# tuple demo 5***********************************************

count_tuple = (1,22,1,44,22,1,66)

count = count_tuple.count(1)                                 #tuple count
print(count)

my_tuple = (88,66,44,22,88,44)
sortedtuple = tuple(sorted(my_tuple))                        #tuple sorted
print(sortedtuple)

