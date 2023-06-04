def multiply_even_numbers(numbers):
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
        return evens
    if evens.index(0) is True:
        for x in evens:
            i = 1
            product = i * x
        return product
    else:
        return "....wait, you didn't give me any even numbers..."


    # """Multiply the even numbers.
    #
    #     >>> multiply_even_numbers([2, 3, 4, 5, 6])
    #     48
    #
    #     >>> multiply_even_numbers([3, 4, 5])
    #     4
    #
    # If there are no even numbers, return 1.
    #
    #     >>> multiply_even_numbers([1, 3, 5])
    #     1
    # """
numbers = input("Numbers, please!: ").replace(" ", "")
print(f"Mmmmm delicious. The product is {multiply_even_numbers(numbers)}")
