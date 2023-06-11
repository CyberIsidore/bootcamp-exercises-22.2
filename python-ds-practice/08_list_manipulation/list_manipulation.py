#Complete!!
def list_manipulation(lst, command, location, value):
    if location == "b":
        loc = 0
    elif location == "e":
        loc = -1
    else:
        return "None"
    if command == "a":
        lst.insert(loc, value)
        return f"Okay. Here's the new list:{lst}."
    elif command == "r":
        i = lst.index(value)
        lst.pop(i)
        return f"Cool. We got rid of '{value}.' The new list is: {lst}."
    else:
        return "None"


lst = [1, 2, 3]
print(lst)
command = input("""
Would you like to add to or remove something from the list?
(A)dd or (R)emove
>""").lower()
location = input("""
Would you like to do that at the beginning or end of the list?
(B)eginning or (E)nd
>""").lower()
value = int(input("What number would you like to add or remove?"))

print(list_manipulation(lst, command, location, value))
