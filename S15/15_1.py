import random
from string import ascii_lowercase

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

letters = list(ascii_lowercase)
answer = random.choice(words)
guess = list(len(answer)*'?')
print(answer)
i = 0
guessed_words = []
while i<7:
    print(''.join(guess))
    a = input("Enter one word: ")
    while len(a) != len(answer):
        a = input(f"Enter a word that has {len(answer)} characters.")
    if a in guessed_words:
        print("This word has been used")
        continue
    guessed_words.append(a)
    if a == answer:
        print(f"\n\n\n------ You Win ------ The answer was {answer}\n\n\n")
        break
    else:
        print(HANGMANPICS[i])
        i = i+1
if i==7:
    print(f"\n\n\n------ You lose ------ The answer was {answer}\n\n\n")