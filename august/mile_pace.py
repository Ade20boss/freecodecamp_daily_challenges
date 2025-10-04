def mile_pace(miles, duration):
    minutes, seconds = duration.split(":")
    minutes, seconds = int(minutes), int(seconds)
    total_time_in_seconds = (minutes * 60) + seconds
    seconds_per_miles = total_time_in_seconds / miles
    total_minutes = int(seconds_per_miles//60)
    if len(str(total_minutes)) == 1:
        total_minutes = "0" + str(total_minutes)
    original_total = int(seconds_per_miles % 60)
    if len(str(original_total)) == 1:
        original_total = "0" + str(original_total)
    return f"\"{total_minutes}:{original_total}\""


print(mile_pace(3, "24:00"))