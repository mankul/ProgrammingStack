import MatrixOperations



def main():
    # Example usage of the C extension
    matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

    # # Add matrices
    # result_add = Matrix_Operations.add_matrices(matrix_a, matrix_b)
    # print("Result of addition:")
    # print(result_add)

    # Multiply matrices
    result_multiply = MatrixOperations.matrix_multiplication(matrix_a, matrix_b)
    print("Result of multiplication:")
    print(result_multiply)
if __name__ == "__main__":  
    main()
