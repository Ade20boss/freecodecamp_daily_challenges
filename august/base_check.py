import string
alphabets_upper = list(string.ascii_uppercase)
def is_valid_number(n, base):
    base_index = []
    track = 0
    for i in range(base):
        if i > 9:
            i = alphabets_upper[track]
            track += 1
        base_index.append(i)
    print(base_index)
    for j in n:
        try:
            j = int(j)
        except ValueError:
            j = j.upper()
        if j not in base_index:
            return False
    return True



print(is_valid_number("4B4BA9", 16))
