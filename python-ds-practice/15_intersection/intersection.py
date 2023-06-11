# Complete!
def intersection(nums, numbers):
    return [num for num in nums if num in numbers]


nums = [1, 2, 3]
numbers = [2, 3, 4]
print(intersection(nums, numbers))
    # """Return intersection of two lists as a new list::
    #
    #     >>> intersection([1, 2, 3], [2, 3, 4])
    #     [2, 3]
    #
    #     >>> intersection([1, 2, 3], [1, 2, 3, 4])
    #     [1, 2, 3]
    #
    #     >>> intersection([1, 2, 3], [3, 4])
    #     [3]
    #
    #     >>> intersection([1, 2, 3], [4, 5, 6])
    #     []
    # """