def to_binary(n):
    divide = n/2
    modulo_list = []
    binary = ""
    modulo_list.append(n % 2)
    while divide >= 1:
        modulo_list.append(int(divide%2))
        divide = divide/2
    modulo_list = modulo_list[::-1]
    for i in modulo_list:
        binary += str(i)
    return binary
print(to_binary(12))