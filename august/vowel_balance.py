def vowel_balance(s):
    mid = int(len(s) / 2)
    count = 0
    count2 = 0
    first_half = s[:mid]
    second_half = s[mid:]
    if len(s) % 2 != 0:
        second_half = s[mid+1:]
    for i in first_half:
        if i in "aeiouAEIOU":
            count += 1
    for j in second_half:
        if j in "aeiouAEIOU":
            count2 += 1
    if count == count2:
        return True
    else:
        return False

print(vowel_balance("123A#b!E&*456-o.U"))

