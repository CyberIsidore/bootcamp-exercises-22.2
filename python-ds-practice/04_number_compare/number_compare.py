# Complete!
def number_compare(a, b):
    if a == b:
        return "The numbers are equal."
    elif a > b:
        return "The first number is greater."
    else:
        return "The second number is greater."


a = int(input("""
Let's compare numbers. 
Please give me two integers!
>"""))
b = int(input("""
One more, please!
>"""))
print(number_compare(a, b))
