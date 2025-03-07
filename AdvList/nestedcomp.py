pairs = [(x,x**2) for x in range(1,4)]
print(pairs)

matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(matrix)

flattened = [element for row in matrix for element in row]

print(flattened)