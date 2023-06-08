def matrix_multiplication(a, b):
    n = len(a)
    m = len(b[0])
    result = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result
a = [[1, 2, 3],
     [4, 5, 6]]
b = [[1, 2],
     [3, 4],
     [5, 6]]
print(matrix_multiplication(a, b))