import math
n = int (input ("Enter size: "))
a = [int(input("Enter [%d]:"%i )) for i in range(n)]
def maxSumSubArray(a, n):
    e = 0
    m = float(-math.inf)
    for i in range(n):
        e += a[i]
        if (m < e):
            m = e
        if (e < 0):
            e = 0
    return m

print(maxSumSubArray(a, n))