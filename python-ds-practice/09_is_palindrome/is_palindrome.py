# Complete!
def is_palindrome(x):
    return x[::-1]


phrase = input("""
I can check for a palindrome!
Enter your phrase: """).lower().replace(" ", "")
if phrase == is_palindrome(phrase):
    print("Yep, it's a palindrome.")
else:
    print("No, that's not a palindrome.")
