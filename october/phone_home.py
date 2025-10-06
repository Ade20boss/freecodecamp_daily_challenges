def send_message(route):
    times = []
    for i in route:
        times.append(((i/300000) + 0.5))
    return round(((sum(times))-0.5), 4)
print(send_message([802101, 725994, 112808, 3625770, 481239]))

