import string
def jbelmu(text):
    new_text = []
    temp_list = []
    for i in text:
        i = i.lower()
        if i in string.punctuation:
            i = ''
        new_text.append(i)
    text = "".join(new_text)
    new_list = text.split()
    for j in new_list:
        if len(j) < 4:
            temp_list.append(j)
            continue
        first, middle, last = j[0], j[1:-1], j[-1]
        sorted_middle = ''.join(sorted(middle))
        new_s = first + sorted_middle + last
        temp_list.append(new_s)
    result = ' '.join(temp_list)
    return result


jbelmu("the quick brown fox jumps over the lazy dog")


