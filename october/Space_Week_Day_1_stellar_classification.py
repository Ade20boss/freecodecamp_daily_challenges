def classification(temp):
    if 0 <= temp <= 3699:
        return "M"
    elif 3700 <= temp <= 5199:
        return "K"
    elif 5200 <= temp <= 5999:
        return "G"
    elif 6000 <= temp <= 7499:
        return "F"
    elif 7500 <= temp <= 9999:
        return "A"
    elif 10000 <= temp <= 29999:
        return "B"
    elif temp >= 30000:
        return "O"

