def flip_case(phrase, to_swap):
    if to_swap in phrase:
        for char in phrase:
            flip_phrase = ""
            if char == to_swap:
                char.swapcase()
                flip_phrase += char
            else:
                flip_phrase += char
        return flip_phrase
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
to_swap = input("What letter should we flip? ")

print(flip_case(phrase, to_swap))
