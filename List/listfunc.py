demo = [1,2,3,4,5,6,7,8,9]
print("demo list : ",demo)
lengthoflist = len(demo)
print("length of list : ",lengthoflist)         #length function

demo.append(10)
print("demo list after append : ",demo)         #append function

demo.extend([15,16])                            #extend function
print("demo list after extend: ",demo)

demo.insert(2,20)                               #insert function
print("demo list after insert: ",demo)

demo.remove(20)                                 #remove function

demo.insert(5,55)
print("demo list before pop: ",demo)
demo.pop(5)                                     #pop function
print("demo list after pop: ",demo)

demo.sort()                                     #sort function
print("demo list after sort: ",demo)

demo.reverse()                                  #reverse function
print("demo list after reverse: ",demo)

blank_list = []
print("blank list: ",blank_list)
blank_list = demo.copy()                        #copy function
print("blank list after copying: ",blank_list)

for member in demo:                             #list traversing
    print(member)