# Complete!
def remove_every_other(lst):
    new_lst = [x for x in lst if lst.index(x) % 2 == 0]
    return new_lst


lst = [1, 2, 3, 4, 5]
print(remove_every_other(lst))
