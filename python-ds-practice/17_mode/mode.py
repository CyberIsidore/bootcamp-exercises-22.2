# Complete!
def mode(nums):
    counter = 0
    num = nums[0]
    for i in nums:
        freq = nums.count(i)
        if(freq > counter):
            counter = freq
            num = i
    return num
    # return [x for x in nums if max(nums.count(x))]


nums = [1, 2, 4, 5, 2, 6, 7, 8, 2, 3, 4, 2]
print(mode(nums))
