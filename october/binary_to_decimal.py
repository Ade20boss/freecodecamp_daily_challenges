def to_decimal(binary):
    binary_list = []
    new_binary = []
    count = 0
    for i in binary:
        binary_list.append(int(i))
    for i in range(len(binary_list)-1, -1, -1):
        new_binary.append(binary_list[count] * 2**i)
        count += 1
    return sum(new_binary)

print(to_decimal("100000000111"))