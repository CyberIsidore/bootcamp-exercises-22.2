def multiply_even_numbers(numbers):
    nums = numbers.split(" ")
    evens = []
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
    if any in nums % 2 == 0:
        for x in evens:
            result = result * x
        return result
    else:
        return "You didn't give me any even numbers..."


    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
numbers = input("""
I only multiply even numbers...
>""")
print(f"Mmmmm delicious. The product is {multiply_even_numbers(numbers)}")