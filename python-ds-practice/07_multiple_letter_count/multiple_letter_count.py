# Complete!
#
# Count frequency of letter and add to dictionary
# return output of letter
# """Return dict of {ltr: frequency} from phrase.
#
#     >>> multiple_letter_count('yay')
#     {'y': 2, 'a': 1}
#
#     >>> multiple_letter_count('Yay')
#     {'Y': 1, 'a': 1, 'y': 1}
# """
def multiple_letter_count(phrase):
    chars = list(phrase)
    freq = []
    for char in chars:
        freq.append(chars.count(char))
    letter_count = dict(zip(chars, freq))
    return letter_count



phrase = input("""
I can count how often letters are used in a phrase. 
Give me a phrase, then I'll handle the rest.
>""").replace(" ", "").casefold()
print(multiple_letter_count(phrase))
