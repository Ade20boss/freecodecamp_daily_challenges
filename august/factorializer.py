def factorial(n):
    factorialized = 1
    for i in range(0, n + 1):
        if i == n:
            break
        factorialized *= (n - i)
    return factorialized
print(factorial(20))