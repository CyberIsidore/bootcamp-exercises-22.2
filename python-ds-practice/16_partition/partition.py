def is_even(lst):
    return lst % 2 == 0

def is_string(el):
    return isinstance(el, str)


def partition(lst, is_even):
    win = []
    lose = []
    return [win.append(x) if is_even(x) is True else lose.append(x) for x in lst]

lst = [1, 2, 3, 4, 5, 6, 7, 8]
print(partition(lst, is_even(lst)))
    # """Partition lst by predicate.
    #
    #  - lst: list of items
    #  - fn: function that returns True or False
    #
    #  Returns new list: [a, b], where `a` are items that passed fn test,
    #  and `b` are items that failed fn test.
    #
    #     >>> partition([1, 2, 3, 4], is_even)
    #     [[2, 4], [1, 3]]
    #
    #     >>> partition(["hi", None, 6, "bye"], is_string)
    #     [['hi', 'bye'], [None, 6]]
    # """