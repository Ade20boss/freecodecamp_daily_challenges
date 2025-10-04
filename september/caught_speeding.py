def speeding(speeds, limit):
    speeding = []
    new_speeds = []
    new_speeds1 = []
    count = 0
    for speed in speeds:
        if speed > limit:
            new_speeds.append(speed)
            count += 1
    if count > 0:
        for i in new_speeds:
            i = i - limit
            new_speeds1.append(i)
        average_speed = sum(new_speeds1) / count
    else:
        return [0, 0]
    speeding.append(count)
    speeding.append(average_speed)
    return speeding

print(speeding([40, 45, 44, 50, 112, 39], 55))