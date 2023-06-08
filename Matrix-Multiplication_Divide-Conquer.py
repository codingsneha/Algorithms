def pad_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    padded_n = 1
    padded_m = 1
    while padded_n < n:
        padded_n *= 2
    while padded_m < m:
        padded_m *= 2
    padded_matrix = [[0] * padded_m for _ in range(padded_n)]
    for i in range(n):
        for j in range(m):
            padded_matrix[i][j] = matrix[i][j]
    return padded_matrix

def unpad_matrix(matrix, original_n, original_m):
    return [row[:original_m] for row in matrix[:original_n]]

def matrix_multiplication(a, b):
    n = len(a)
    m = len(b[0])
    result = [[0] * m for _ in range(n)]
    if n <= 16 and m <= 16:
        for i in range(n):
            for j in range(m):
                for k in range(len(b)):
                    result[i][j] += a[i][k] * b[k][j]
    else:
        a_padded = pad_matrix(a)
        b_padded = pad_matrix(b)
        mid = len(a_padded) // 2
        a11 = [row[:mid] for row in a_padded[:mid]]
        a12 = [row[mid:] for row in a_padded[:mid]]
        a21 = [row[:mid] for row in a_padded[mid:]]
        a22 = [row[mid:] for row in a_padded[mid:]]
        b11 = [row[:mid] for row in b_padded[:mid]]
        b12 = [row[mid:] for row in b_padded[:mid]]
        b21 = [row[:mid] for row in b_padded[mid:]]
        b22 = [row[mid:] for row in b_padded[mid:]]
        p1 = matrix_multiplication(a11, [[b11[0][0]], [b21[0][0]]])
        p2 = matrix_multiplication(a12, [[b12[0][0]], [b22[0][0]]])
        p3 = matrix_multiplication(a11, [[b11[0][1]], [b21[0][1]]])
        p4 = matrix_multiplication(a12, [[b12[0][1]], [b22[0][1]]])
        p5 = matrix_multiplication(a21, [[b11[0][0]], [b11[0][1]]])
        p6 = matrix_multiplication(a22, [[b21[0][0]], [b21[0][1]]])
        p7 = matrix_multiplication(a21, [[b12[0][0]], [b12[0][1]]])
        p8 = matrix_multiplication(a22, [[b22[0][0]], [b22[0][1]]])
        result[:mid][:mid] = [[p1[0][0] + p5[0][0] - p3[0][0] + p7[0][0]]]
        result[:mid][mid:] = [[p2[0][0] + p3[0][0]]]
        result[mid:][:mid] = [[p1[1][0] + p5[1][0] - p4[0][0] + p8]]
    return result
a = [[1, 2, 3],
     [4, 5, 6]]
b = [[1, 2],
     [3, 4],
     [5, 6]]
print(matrix_multiplication(a, b))