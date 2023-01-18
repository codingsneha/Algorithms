def merge(a, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]
    
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        k = k + 1
        i = i + 1

    
    while j < n2:
        arr[k] = R[j]
        k = k + 1
        j = j + 1

def mergeSort(a, l, r):
    if l < r:
        m = l + (r - l) // 2

        mergeSort(a, l, m)
        mergeSort(a, m + 1, r)
        merge(a, l, m, r)
    
arr = [12, 11, 13, 27, 19, 2, 1]
n = len(arr)
print("\nArray: ")
for i in range(n):
    print("%d" % arr[i], end = " ")

mergeSort(arr, 0, n - 1)
print("\n\nSorted array: ")
for i in range(n):
    print("%d" % arr[i], end = " ")
