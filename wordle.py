import random
import sys
from termcolor import colored

def print_menu():
    print("Let's play a wordle game:")
    print("type a five letter word and hit enter!\n")

def read_random_word():
    with open("words.txt") as reader:
        words = reader.read().splitlines()
        return random.choice(words)



print_menu()
play_again = '' 
while play_again != 'n':
    word = read_random_word()
    for attempt in range(1, 6):
        guess = input().lower()

        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')

        for i in range(min(len(guess), 5)):
            if guess[i] == word[i]:
                print(colored(guess[i], 'green'), end='')
            elif guess[i] in word:
                print(colored(guess[i], 'yellow'), end='')
            else:
                print(guess[i], end='')
        print()

        if guess == word:
            print(colored(f'Congratulations! You got the wordle in {attempt}', 'red'))
            break
    play_again = input('Do you want to play again? click enter for yes, hit n and enter for no 😁 ')
