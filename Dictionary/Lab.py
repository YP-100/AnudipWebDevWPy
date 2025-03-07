# Write a Python program to get the key, value and item in a dictionary.
#  input:dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print(dict_num.keys())             #key function
print(dict_num.values())           #value function
print(dict_num.items())            #item function

# OR

dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("With For Loop : ")
print("key, value :")
for key, value in dict_num.items():
    print(key, value)
print(dict_num.items())

# Write a Python program to deduce use of multiple dictionary functions.

dict_num1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("ORIGINAL :",dict_num1)

dict_num1.update({7: 70, 8: 80, 9: 90, 10: 100})      #update function will update dictionary values
print("after update: ",dict_num1)

new_dict = dict_num1.copy() 
print("copied dictionary : ",new_dict)                #copy function will copy dictionary values

print(new_dict.__contains__(1))                       #contains function will check whether key is present or not if yes returns true

dict_num1.pop(10)                                      #pop function will remove key value pair
print("after pop: ",dict_num1)

dict_num1.clear()                                     #clear function will clear dictionary values
print("after clear: ",dict_num1)