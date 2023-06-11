# Complete!
def capitalize(phrase):
    return phrase.capitalize()
    # """Capitalize first letter of first word of phrase.
    #
    #     >>> capitalize('python')
    #     'Python'
    #
    #     >>> capitalize('only first word')
    #     'Only first word'
    # """
phrase = input("Phrase please! ")
print(f'I think you meant: "{capitalize(phrase)}."')