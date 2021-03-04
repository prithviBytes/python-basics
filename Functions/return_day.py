def return_day(num):
    days = {
        1 : "Sunday",
        2 : "Monday",
        3 : "Tuesday",
        4 : "Wednesday",
        5 : "Thursday",
        6 : "Friday",
        7 : "Saturday"
    }
    if num in days:
        return days[num]
    else:
        return None

print(return_day(10))
