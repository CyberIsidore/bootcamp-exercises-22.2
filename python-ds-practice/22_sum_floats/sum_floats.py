# Complete
def sum_floats(nums):
    i = 0
    for x in nums:
        if isinstance(x, float) is True:
            i += x
    return i


nums = [1.5, 2.4, "awesome", [], 1]
print(sum_floats(nums))

