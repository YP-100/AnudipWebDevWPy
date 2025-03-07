def count_letters(str):
    count = {}
    for char in str:
        if char.isalpha():
            count[char] = count.get(char, 0) + 1
    return count

text = "THis is my self study on demo on strings"
result = count_letters(text)
print(result)
