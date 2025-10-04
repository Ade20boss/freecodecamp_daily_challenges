def squares_with_three(n):
    count = 0
    for i in range(n+1):
        if "3" in str(i**2):
            count += 1
    return count
print(squares_with_three(10000))