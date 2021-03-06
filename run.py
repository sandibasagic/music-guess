"""
It's a guess game where users can guess a secret word.
The game has secret words of musical instruments
"""
import random
from words import word_list


def get_word():
    """
    Function used to get words from random words list.
    """
    word = random.choice(word_list)
    return word.upper()


def play(word):
    """
    The list of variables used in game and the main function to run the game
    """
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Welcome to guess game of musical instruments!")
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Great!,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                sign = [i for i, letter in enumerate(word) if letter == guess]
                for index in sign:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word)


def main():
    """
    Function if the user wants to play the game again.
    """
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)
    print("Thank you for playing Can You Guess?")


if __name__ == "__main__":
    main()
