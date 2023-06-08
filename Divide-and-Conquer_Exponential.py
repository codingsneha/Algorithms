def power(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        result = power(x, n//2)
        if n % 2 == 0:
            return result * result
        else:
            return x * result * result
print(power(2, 5)) # Output: 32
