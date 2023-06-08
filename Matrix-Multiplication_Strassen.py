import numpy as np

def pad_matrix(matrix):
    rows, cols = matrix.shape
    max_dim = max(rows, cols)
    next_power_of_two = int(2 ** np.ceil(np.log2(max_dim)))
    padded_matrix = np.zeros((next_power_of_two, next_power_of_two))
    padded_matrix[:rows, :cols] = matrix
    return padded_matrix

def strassen(matrix1, matrix2):
    # Pad matrices if necessary
    matrix1 = pad_matrix(matrix1)
    matrix2 = pad_matrix(matrix2)

    # Base case
    if matrix1.shape == (1, 1):
        return matrix1 * matrix2

    # Recursive case
    else:
        # Split matrices into quadrants
        a, b = np.hsplit(matrix1, 2)
        c, d = np.hsplit(matrix2, 2)

        # Compute intermediate matrices
        p1 = strassen(a, c)
        p2 = strassen(b, d)
        p3 = strassen(a + b, c + d)
        p4 = strassen(a - b, c + d)
        p5 = strassen(a + b, c - d)
        p6 = strassen(a - d, c - d)
        p7 = strassen(b - d, c + d)

        # Compute submatrices of the result
        top_left = p3 + p4 - p6 - p2
        top_right = p1 + p2
        bottom_left = p5 + p6
        bottom_right = p1 - p3 - p5 + p7

        # Combine submatrices into the final result
        result = np.vstack((np.hstack((top_left, top_right)), np.hstack((bottom_left, bottom_right))))
        return result

A = [[1, 2, 3], [1, 2, 3], [0, 0, 2]]
B = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
strassen(A, B) # A[][],B[][],R1,C1,R2,C2