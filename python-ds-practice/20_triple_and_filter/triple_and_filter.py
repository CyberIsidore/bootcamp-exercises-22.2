# Complete!
def triple_and_filter(nums):
    return [num * 3 for num in nums if num % 4 == 0]


nums = [6, 8, 10, 12]
print(triple_and_filter(nums))
