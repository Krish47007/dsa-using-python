def fast_pow(a,n):
    if n == 0:
        return 1
    res = fast_pow(a,n//2)

    if n % 2 == 0:
        return res * res
    else:
        return a * res * res

print(fast_pow(2,7))
print(fast_pow(3,4))