
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in range(len(matrix)):
            for j in matrix[i]:
                print("{:d}".format(j), end=" ")
            print()


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)