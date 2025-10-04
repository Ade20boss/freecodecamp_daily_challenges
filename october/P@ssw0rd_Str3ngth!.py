def minimum_length(password):
    if len(password) >= 8:
        return True
    else:
        return False
def has_lowercase_letters(password):
    check = []
    for i in password:
        if i.islower():
            check.append(i)
        else:
            continue
    if len(check) >= 1:
        return True
    else:
        return False


def has_numbers(password):
    check = []
    for i in password:
        if i.isdigit():
            check.append(i)
        else:
            continue
    if len(check) >= 1:
        return True
    else:
        return False

def has_uppercase_letters(password):
    check = []
    for i in password:
        if i.isupper():
            check.append(i)
        else:
            continue
    if len(check) >= 1:
        return True
    else:
        return False
def has_special_characters(password):
    special_characters = "!@#$%^&*"
    check = []
    for i in password:
        if i in special_characters:
            check.append(i)
        else:
            continue
    if len(check) >= 1:
        return True
    else:
        return False

def counter(password):
    count = 0
    if minimum_length(password):
        count += 1
    if has_numbers(password):
        count += 1
    if has_uppercase_letters(password) and has_lowercase_letters(password):
        count += 1
    if has_special_characters(password):
        count += 1
    return count
def password_validation(password):
    count = counter(password)
    if count == 4:
        return "strong"
    elif count == 2 or count == 3:
        return "medium"
    else:
        return "weak"


print(password_validation("C0d3&Fun!"))