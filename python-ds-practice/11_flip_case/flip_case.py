def flip_case(phrase, to_swap):
    letters = list(phrase)
    for char in letters:
        if char == to_swap:
            return char.swapcase(char)
        elif char != to_swap:
            return char
        else:
            return "That character isn't in your phrase!"


    # """Flip [to_swap] case each time it appears in phrase.
    #
    #     >>> flip_case('Aaaahhh', 'a')
    #     'aAAAhhh'
    #
    #     >>> flip_case('Aaaahhh', 'A')
    #     'aAAAhhh'
    #
    #     >>> flip_case('Aaaahhh', 'h')
    #     'AaaaHHH'
    #
    # """
phrase = input("Say something! ")
print(f'You said: "{phrase}."')
to_swap = input("What letter should we switch? ")

print(flip_case(phrase, to_swap).swapcase())
