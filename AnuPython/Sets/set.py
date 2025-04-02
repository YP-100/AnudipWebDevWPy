
first_set = {1,54,39,2,74}                  #set creation
print(first_set)

demo = [1,2,3,4,5]
second_set = set(demo)                      #set using constructor
print(second_set)

empty_set = {}                              #empty set
print(empty_set)

empty_set2 = set()                          #empty set using constructor
print(empty_set2)

str = "python programming"
str_set = set(str)                          #converting string to set
print(str_set)


#set demo 2**********************************************

demo_set = {4,7,8,33,99,23}
print("original set : ",demo_set)
demo_set2 = {4,6,8,9}
print("second set : ",demo_set2)
resultant_set = demo_set.union(demo_set2)       #union function
print("union set : ",resultant_set)

intersect_set = demo_set.intersection(demo_set2) #intersection function
print("intersection set : ",intersect_set)

diff_set = demo_set.difference(demo_set2)       #difference function
print("difference set : ",diff_set)

symetric_set = demo_set.symmetric_difference(demo_set2) #symmetric difference
print("symmetric difference set : ",symetric_set)

sub = demo_set2.issubset(demo_set)              #issubset function
print("set2 is subset of set1 : ",sub)

sup = demo_set.issuperset(demo_set2)            #issuperset function
print("set1 is superset of set2 : ",sup)

demo_set.add(88)                                #add function
print("set1 after add : ",demo_set)

demo_set.remove(4)                             #remove function
print("set1 after remove : ",demo_set)
