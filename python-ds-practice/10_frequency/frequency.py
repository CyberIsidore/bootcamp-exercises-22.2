# Return frequency of term in list
# make list
# iterate over each term
# store item and frequency in dictionary
# get search term from user
# get item from dictionary
import collections
def frequency(lst, search_term):
    x = lst.count(search_term)
    return x


lst = ["cat", "dog", "dog", "cat", "fish", "lizard", "hamster", "bird", "cat", "dog", "chimpanzee", "snake", "dog",
       "bird", "micro sheep", "cat", "cat"]
search_term = input("""
Check how many vet appointments there are for each type of animal. Enter an animal from the list to search.
cat
dog
fish
lizard
hamster
bird
chimpanzee
snake
micro sheep
>""").lower()
print(frequency(lst, search_term))
# print(f"There are {frequency(lst, search_term)}appointments today.")
