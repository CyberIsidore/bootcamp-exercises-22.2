original = [1, 2, 1, 4, 3, 12]
def find_the_duplicate(original):
    dupes = []
    x = 0
    freq = original.count(x)
    [dupes.append(n) for n in original if freq > 1]
    return(dupes)

print(find_the_duplicate(original))
    # """Find duplicate number in nums.
    #
    # Given a list of nums with, at most, one duplicate, return the duplicate.
    # If there is no duplicate, return None
    #
    #     >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
    #     1
    #
    #     >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
    #     9
    #
    #     >>> find_the_duplicate([2, 1, 3, 4]) is None
    #     True
    # """
