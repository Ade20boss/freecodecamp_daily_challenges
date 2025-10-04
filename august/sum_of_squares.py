def sum_of_squares(n):
    total = 0
    for i in range(n+1):
        total += i**2
    return total
print(sum_of_squares(1000))