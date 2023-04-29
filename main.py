# import
import random
import hangman_words
import hangman_art
import os

repeat = False
while not repeat:
    os.system('cls')
    # Update the word list to use the 'word_list' from hangman_words.py
    chosen_word = random.choice(hangman_words.word_list).lower()
    word_length = len(chosen_word)

    end_of_game = False
    lives = 6

    # TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
    print(hangman_art.logo)

    # Testing code
    # print(f'Pssst, the solution is {chosen_word}.')

    # Create blanks
    display = []
    for _ in range(word_length):
        display += "_"

    print(f"The word length is {word_length}: {display}")

    h = input("Do you want hints? type y ")
    if (h == 'y' or h == 'Y') and word_length > 3:
        display[word_length - 1] = chosen_word[word_length - 1]
        display[0] = chosen_word[0]
        display[2] = chosen_word[2]
        print(display)
    else:
        print("The word is not more than 3 character or you don't need hints. Best of luck!")

    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        # If the user has entered a letter they've already guessed, print the letter and let them know.
        if guess in display:
            print(guess + " the letter might be guessed, try other letter.")

        # Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
            if letter == guess:
                display[position] = letter

        # Check if user is wrong.
        if guess not in chosen_word:
            # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
            print(guess + " is not exist in the word")
            lives -= 1
            if not lives:
                end_of_game = True
                print(f"You lose. The word was {chosen_word}")

        # Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")

        # Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("You win.")

        # Import the stages from hangman_art.py and make this error go away.
        print(hangman_art.stages[lives])

    r = input("Do you want to continue the game? type y ")
    if (r != 'y'):
        repeat = True


