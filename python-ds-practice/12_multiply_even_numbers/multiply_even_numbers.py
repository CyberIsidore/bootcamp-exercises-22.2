# Complete!
numbers = [1, 2, 3, 4, 5, 6]
def multiply_even_numbers(numbers):
    evens = [num for num in numbers if num % 2 == 0]
    result = 1
    for x in evens:
        result = result * x
    return result


print(multiply_even_numbers(numbers))
