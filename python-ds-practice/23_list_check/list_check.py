def list_check(lst_lite):
    result = ""
    for x in lst_lite:
        if isinstance(x, list) is True:
            result = "True"
        else:
            result = "False"
    return result


lst = ([[1], [2, 3]])
lst_lite = ([[1], "nope"])
print(list_check(lst))
