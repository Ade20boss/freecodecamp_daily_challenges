letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
digits = list("0123456789")
def battle(my_army, opposing_army):
    my_army_list = []
    opposing_army_list = []
    my_army_score = 0
    opposing_army_score = 0
    if len(my_army) > len(opposing_army):
        return "Opponent retreated"
    elif len(my_army) < len(opposing_army):
        return "We retreated"
    else:
        for i in my_army:
            if i in letters:
                my_army_list.append(int(letters.index(i)) + 1)
            elif i in digits:
                my_army_list.append(int(i))
            else:
                my_army_list.append(0)
        for j in opposing_army:
            if j in letters:
                opposing_army_list.append(int(letters.index(j)) + 1)
            elif j in digits:
                opposing_army_list.append(int(j))
            else:
                opposing_army_list.append(0)
        for k in range(len(my_army_list)):
            if my_army_list[k] > opposing_army_list[k]:
                my_army_score += 1
            elif my_army_list[k] < opposing_army_list[k]:
                opposing_army_score += 1
            else:
                continue
        if my_army_score > opposing_army_score:
            return "We won"
        elif my_army_score < opposing_army_score:
            return "We lost"
        else:
            return "It was a tie"

print(battle("Mr. Smith", "Dr. Jones"))



