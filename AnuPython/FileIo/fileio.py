# fileio demo 1 **********************

def studemo():
    file = open("txtfi.txt", "r")
    for line in file:
        print(line)
    file.close()

studemo()


# fileio demo 2 **********************

def count_words():
    file1 = open("D:\\anudip\\AnuPython\\LecMar3\\txtfi.txt", "r")
    count = 0
    data = file1.read()
    words = data.split()

    for word in words:
        count +=1
    print("total words = ",count)
    file1.close()

count_words()


#f ileio demo 3 ************************

def count_upper():
    file2 = open("txtfi.txt", "r")
    data2 = file2.read()
    count2 = 0
    count3 = 0
    for letter in data2:
        # if upp.isupper():               #for upper case
        if letter.isupper():                 #for lower case
            count2 +=1
        elif letter.islower():
            count3 +=1                    #for lower in same
    print("upper case letters",count2)
    print("lower case letters",count3)
    file2.close

count_upper()