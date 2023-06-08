def binarySearch(L, key):
    low, high = 0, len(L)
    while(low < high):
        mid = int((low + high - 1) / 2)
        if (key < L[mid]):
            high = mid - 1
        elif (key > L[mid]):
            low = mid + 1
        else:
            return mid
    return -1

#Recursive binary search
def rbinarySearch(a, key, low, high):
    while(low <= high):
        mid = (high + low)//2
        if (a[mid] == key):
            return mid
        elif (a[mid] < key):
            return rbinarySearch(a, key, mid+1, high)
        else:
            return rbinarySearch(a, key, low, mid-1)
    return -1

L = [4, 5, 6,7, 8, 33]
key = 3
k = 6
print(binarySearch(L, key))
print(binarySearch(L, k))