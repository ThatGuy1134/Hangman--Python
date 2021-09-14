# Jesse Hauck
# 9/5/21 Hangman
import random


def word_printer():
    for j in dashes:
        print(j, end="")


def letter_checker(a_letter):
    letter_index = guess_word.index(a_letter)
    guess_word[letter_index] = "*"
    dashes[letter_index] = a_letter


def input_checker():
    an_input = input("\nInput a letter: ")
    if len(an_input) != 1:
        return an_input, 2
    if an_input.isalpha() and an_input.islower():
        good_guess = 0
    else:
        good_guess = 1

    return an_input, good_guess


print("H A N G M A N")

game_start = ""
while game_start not in ("play", "exit"):
    game_start = input('Type "play" to play the game, "exit" to quit: ')

while game_start != "exit":
    guess_words = ["python", "java", "kotlin", "javascript"]
    guess_index = random.randint(0, 3)
    guess_word = list(guess_words[guess_index])
    dashes = [i for i in "-" * len(guess_word)]
    guessed_letters = set()
    wrong_guesses = 0

    while wrong_guesses < 8:
        print()
        word_printer()
        a_guess, good_guess = input_checker()
        if good_guess == 1:
            print("Please enter a lowercase English letter")
        elif good_guess == 2:
            print("You should input a single letter")
        else:
            if a_guess in guess_word:
                while a_guess in guess_word:
                    letter_checker(a_guess)
            elif a_guess in guessed_letters:
                print("You've already guessed this letter")
            else:
                print("That letter doesn't appear in the word")
                wrong_guesses += 1
            guessed_letters.add(a_guess)

        is_correct = "".join(dashes) == guess_words[guess_index]

        if is_correct:
            wrong_guesses = 8
            print("You guessed the word {0}!".format(guess_words[guess_index]))
            print("You survived!")

    if not is_correct:
        print("You lost!")

    game_start = ""
    print()
    while game_start not in ("play", "exit"):
        game_start = input('\nType "play" to play the game, "exit" to quit: ')
