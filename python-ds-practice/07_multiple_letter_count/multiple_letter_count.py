# get phrase from user
# turn phrase into a list of characters (dictionary = "characters")
# count frequency (variable = freq) of each letter (keyword = "ltr")
#
# Count frequency of letter and add to dictionary
# return output of letter
#"""Return dict of {ltr: frequency} from phrase.
    #
    #     >>> multiple_letter_count('yay')
    #     {'y': 2, 'a': 1}
    #
    #     >>> multiple_letter_count('Yay')
    #     {'Y': 1, 'a': 1, 'y': 1}
    # """
def multiple_letter_count(phrase):
    letters = {}
    x = list(phrase)
# lists aren't hashable! turn x into a tuple
    ltr = tuple(x)
    freq = x.count(x)
    letters[ltr] = freq
    print(freq)
    return letters

phrase = input("""
I can count how often letters are used in a phrase. 
Give me a phrase, then I'll handle the rest.
>""")
print(multiple_letter_count(phrase))
