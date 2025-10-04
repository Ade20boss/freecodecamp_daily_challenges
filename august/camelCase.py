def to_camel_case(s):
    separator_set = [" ", "_", "-"]
    s = s.lower()
    for i in separator_set:
        s = s.replace(i, " ")
    s_list = s.split()
    s = ""
    for i in s_list:
        if i == s_list[0]:
            s += i
            continue
        s += i.capitalize()
    return s

print(to_camel_case("ye old-_-sea  faring_buccaneer_-_with a - peg__leg----and a_parrot_ _named- _squawk"))