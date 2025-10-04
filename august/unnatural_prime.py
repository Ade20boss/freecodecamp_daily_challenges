import math
def unnatural_prime(prime):
    if prime < 0:
        prime = prime * -1
    count = 0
    if prime == 1 or prime == 0:
        return False
    elif prime % 2 == 0 and prime > 2:
        return False
    for j in range(2,  round(math.sqrt(prime))+1):
        if prime % j == 0 and prime != j:
            count += 1
            break
    if count > 0:
        return False
    else:
        return True

print(unnatural_prime(-23))