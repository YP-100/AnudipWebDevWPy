# You have a list of strings, and you want to extract all digits from these strings and combine them into a single list.
# strings = [
# "abc123",
# "hello456world",
# "789",
# "test"
# ]

strings = ["abc123","hello456world","789","test"]

digits = [int(char) for s in strings for char in s if char.isdigit()]

print(digits)

