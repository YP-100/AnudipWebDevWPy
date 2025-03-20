class Matrix:
    def __init__(self, data):
        if not all(len(row) == len(data[0]) for row in data):
            raise ValueError("All rows must have the same number of columns")
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions to be added")
        
        result = [
            [
                self.data[i][j] + other.data[i][j] 
                for j in range(self.cols)
            ] 
            for i in range(self.rows)
        ]
        
        return Matrix(result)

    def __repr__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

# Example usage:
if __name__ == "__main__":
    matrix1 = Matrix([[1, 2, 3], [4, 5, 6]])
    matrix2 = Matrix([[7, 8, 9], [10, 11, 12]])

    result_matrix = matrix1 + matrix2
    print("Result of Matrix Addition:")
    print(result_matrix)









class CustomString:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, CustomString):
            return CustomString(self.value + other.value)
        return NotImplemented

    def __mul__(self, times):
        if isinstance(times, int) and times >= 0:
            return CustomString(self.value * times)
        return NotImplemented

    def to_upper(self):
        return self.value.upper()

    def __repr__(self):
        return f'CustomString("{self.value}")'

# Example usage:
if __name__ == "__main__":
    str1 = CustomString("Hello")
    str2 = CustomString(" World")

    # Concatenation
    concatenated = str1 + str2
    print("Concatenated String:", concatenated)

    # Repeating the string
    repeated = str1 * 3
    print("Repeated String:", repeated)

    # Uppercase
    uppercase = str1.to_upper()
    print("Uppercase String:", uppercase)