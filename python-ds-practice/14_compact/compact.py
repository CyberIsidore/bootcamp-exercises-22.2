# Complete!
def compact(lst):
    return list(filter(bool,lst))


lst = [0, 1, 2, '', [], False, (), None, 'All done']
print(compact(lst))
