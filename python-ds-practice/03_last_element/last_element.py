# Complete!
# Make function that returns last element of a list. If list is empty, return "None"

def last_element(nums):
    if len(nums) == 0:
        return("None.")
    else:
        last = nums[-1]
        return(last)


nums = [1, 2, 3]
print(last_element(nums))
