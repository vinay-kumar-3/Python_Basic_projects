

import random

from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)


# Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo
print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

dead=6
count = 0
#Create blanks
display = ["_"] * word_length

while count<word_length and dead>0:
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")
    elif guess in chosen_word:
        for i in range(word_length):
            if guess == chosen_word[i]:
                display[i] = guess
                count+=1
    else:
        dead-=1
    for i in display:
        print(i,end=" ")
    
    from hangman_art import stages
    print(stages[dead])

if count == word_length:
    print("you saved the Hangman")
else:
    print("Hangman is dead")