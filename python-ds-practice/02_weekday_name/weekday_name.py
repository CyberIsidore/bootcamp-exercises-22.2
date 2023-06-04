# Complete!
# Make a dictionary for days of the week and corresponding numbers
# Return Weekday name if 1-7 is entered
# Else, return "None"
def weekday_name(day_of_week):
    numbers = {
        "1": "Sunday",
        "2": "Monday",
        "3": "Tuesday",
        "4": "Wednesday",
        "5": "Thursday",
        "6": "Friday",
        "7": "Saturday",
    }
    output = ""
    good_nums = ["1", "2", "3", "4", "5", "6", "7"]
    for num in day_of_week:
        if day_of_week in good_nums:
            output += f"It's {numbers.get(num, num)}!"
            return output
        else:
            return "That's not right!"


day_of_week = input("""
Which day of the week is it?
(Enter 1-7)
>""")
print(weekday_name(day_of_week))
