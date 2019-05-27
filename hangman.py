#!/usr/bin/env python
''' Hangman game. '''
from random import randint, choice

WORDS = ['apple', 'orange', 'monkey', 'hallucination', 'hangman']

WORDS_DICT = {'apple': 'A fruit that keeps the doctor away.',
              'orange': 'an orange fruit.',
              'monkey': 'A mischevious animal.',
              'hallucination': 'What you get when you eat shrooms.',
              'hangman': 'The antagonist of this game.'}

CHOSEN_WORD = list(choice(WORDS))  # Chosing a word from the list at random.
# Making another list for adding BLANKS.
BLANKED_WORD = [l for l in CHOSEN_WORD]
BLANKS = set()  # Creating a set called BLANKS to get unique elements.
# Collecting the HINT just in case the user needs it.
HINT = WORDS_DICT["".join(CHOSEN_WORD)]

'''
Selecting the positions to add the BLANKS/underscores.
Writing to a set to prevent selecting the same position again.
This loop also replaces selected letters with underscore.
'''
while len(BLANKS) <= ((len(CHOSEN_WORD) // 2) - 1):
    A = randint(0, len(CHOSEN_WORD) - 1)
    BLANKS.add(A)
    BLANKED_WORD[A] = "_"


# making it a set makes it much easier for iterating through it.
BLANKS = list(BLANKS)
RIGHT_COUNTER = 0

for _ in range(len(BLANKS) + 5):
    print("".join(BLANKED_WORD))
    USER_CHOICE = input("\nMake a choice! \n")
    if USER_CHOICE.isalpha() and (len(USER_CHOICE) == 1):  # Filtering user input.
        for index in BLANKS:
            if USER_CHOICE == str(CHOSEN_WORD[index]):
                # Adds the underscore with the corresponding letter.
                BLANKED_WORD[index] = USER_CHOICE.lower()
                RIGHT_COUNTER += 1

    else:
        print(f"\n'{USER_CHOICE}' is not a supported choice. Try again")

    if RIGHT_COUNTER == len(BLANKS):
        print("\nYou won!")
        break
    elif (len(BLANKS) + 5) - _ == 3:
        print(f" You have 2 chances left.\n The hint is: {HINT}")
