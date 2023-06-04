# Complete!
def single_letter_count(string, letter):
    chars = list(string)
    return chars.count(letter)


string = input("""
I can check how many times a letter appears in a string. 
Give me a string to check!
>""")
letter = input("""
Okay, got it. 
What letter should I count?
>""")
print(f'The letter "{letter}" appears in "{string}" {single_letter_count(string, letter)} time(s).')
