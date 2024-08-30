import random

import hangman_art
import hangman_words

# initialising
chosen_word = random.choice(hangman_words.word_list)
lives = 6
display = []
for letter in range(1, (len(chosen_word)) + 1):
    display.append("_")
end_of_game = False
print(hangman_art.logo)
print(f"The word has {len(chosen_word)} letters.\nYou have 6 lives left.")

while end_of_game is False:
    i = -1
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print("You already guessed this letter.")

    # checking if the guess is present in the chosen word
    for letter in chosen_word:
        i += 1
        if letter == guess:
            display[i] = letter
            print(display)
            if display.count("_") == 0:
                end_of_game = True
                print(f"{' '.join(display)}")
                print("You won!")

    # if the guess is not present in the chosen word
    if guess not in chosen_word:
        lives -= 1
        print(
            f"You guessed {guess}, that is not in the chosen word. You lose a life."
        )
        print(hangman_art.stages[lives])
        if lives == 0:
            end_of_game = True
            print(f"You lose. The word was {chosen_word}.")
        else:
            print(display)
            print(f"You have {lives} live(s) left.")
