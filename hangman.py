import urllib.request
import random
import os
import hangman_art

# create a variable to hole the remote word list url
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

# open the url, read/decode it, and split the string into a list of words
response = urllib.request.urlopen(word_site)
text = response.read().decode()
# words = text.splitlines()
words = ['aardvark', 'bison', 'cat']

# choose a word from the list at random and create a list of blanks of the same length
word = random.choice(words)
print(f"Psst, the chosen word is {word}")
word_length = len(word)
blanks = ['_'] * word_length

win = False
lives = 6
count = 1

while not win:
    # prompt player to guess a letter and display current stats
    if count != 1:
        os.system('cls' if os.name == 'nt' else 'clear')
    count -= 1
    print(hangman_art.logo)
    print(hangman_art.stages[lives])
    for blank in blanks:
        print(blank + " ", end="")
    print("")
    player_letter = input("\nGuess a letter: ").lower()
    # loop through the letters in the word creating an index (i) with enumerate function
    for i, letter in enumerate(word):
        # if letter at current position is same as players, access blanks at current index and replace with letter
        if letter == player_letter:
            blanks[i] = player_letter
    # if players guess is not in the word, lose a life and print ASCII art for hanging man
    if player_letter not in word:
        lives -= 1
        input(f"The letter '{player_letter}' is not in the word, press ENTER try again...")

    # if blanks array has no more blanks, set win to True
    if '_' not in blanks:
        win = True
        print("You win!")
    # if player has had 6 wrong guesses, break and end game
    if lives == 0:
        print("You lose")
        break
