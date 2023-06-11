# Complete!
def flip_case(phrase, to_swap):
    if to_swap in phrase:
        return "".join([x.swapcase() if x == to_swap else x for x in phrase ]).strip(" ")
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
print(f'You said: "{phrase}"')
to_swap = input("What letter should we flip? ").casefold()

print(flip_case(phrase, to_swap))
