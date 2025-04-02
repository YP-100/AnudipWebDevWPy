# 1. Write a function in Python to count and display the total number of words in a text file “ABC.txt”
# also count uppercase / lowercase character in same  text file

def countw():
    file = open("ABC.txt","r")
    fdata = file.read()
    split = fdata.split()
    count = 0
    for words in split:
        # print(words.__len__())
        count += 1
    print("Total no of words in ABC.txt = ",count)

def upplow():
    file = open("ABC.txt","r")
    data = file.read()
    count = 0
    count2 = 0
    for words in data:
        if words.isupper():
            count += 1
        elif words.islower():
            count2 += 1
    print("The no of upper cased letters in ABC.txt = ",count)
    print("The no of lower cased letters in ABC.txt = ",count2)
countw()
upplow()

# 2. Write a function display_words() in python to read lines from a text file "story.txt", and display those words, which are less than 4 characters.

def display_words():
    file = open("story.txt","r")
    data = file.read()
    split = data.split()
    for words in split:
        if words.__len__() < 4:
            print(words)
display_words()