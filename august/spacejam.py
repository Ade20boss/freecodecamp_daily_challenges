def space_jam(s):
    word = []
    for i in s:
        if i != ' ':
            if i.isalpha():
                i = i.upper()
            word.append(i)
            word.append('  ')
    s = (''.join(word)).rstrip()
    return s

print(space_jam("C@t$ & D0g$"))


