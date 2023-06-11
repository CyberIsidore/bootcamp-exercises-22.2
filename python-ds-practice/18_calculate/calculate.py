def calculate(operation, a, b, message='The result is'):
    if operation == "a":
        x = ""
        return f"{message}: {x}"
    elif operation == "s":
        x = a - b
        return f"{message}: {x}"
    elif operation == "m":
        x = a * b
        return f"{message}: {x}"
    elif operation == "d":
        x = a % b
        return f"{message}: {x}"
    else:
        return "That's not a valid operator."

operation = "a"
a = 2.4
b = 4
message = "Result"


print(calculate(operation, a, b, message))
    # """Perform operation on a + b, ()possibly truncating) & returning w/msg.
    #
    # - operation: 'add', 'subtract', 'multiply', or 'divide'
    # - a and b: values to operate on
    # - make_int: (optional, defaults to False) if True, truncates to integer
    # - message: (optional) message to use (if not provided, use 'The result is')
    #
    # Performs math operation (truncating if make_int), then returns as
    # "[message] [result]"
    #
    #     >>> calculate('add', 2.5, 4)
    #     'The result is 6.5'
    #
    #     >>> calculate('subtract', 4, 1.5, make_int=True)
    #     'The result is 2'
    #
    #     >>> calculate('multiply', 1.5, 2)
    #     'The result is 3.0'
    #
    #     >>> calculate('divide', 10, 4, message='I got')
    #     'I got 2.5'
    #
    # If a valid operation isn't provided, return None.
    #
    #     >>> calculate('foo', 2, 3)
    #
    # """
