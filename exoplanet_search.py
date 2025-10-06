stuff = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
def readings(read):
    readings_list = []
    for i in read:
        readings_list.append(stuff.index(i))
    return sum(readings_list)/len(readings_list)

def list1(read):
    readings_list = []
    for i in read:
        readings_list.append(stuff.index(i))
    return readings_list

def has_exoplanet(read1):
    average = readings(read1)
    readings_list = list1(read1)
    for i in readings_list:
        if i <= ((80/100) * average):
            return True
    return False

print(has_exoplanet("ZXXWYZXYWYXZEGZXWYZXYGEE"))


