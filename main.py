from random_words import RandomWords

hangman = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']




logo = '''

  _    _                                               
 | |  | |                                              
 | |__| |  __ _  _ __    __ _  _ __ ___    __ _  _ __  
 |  __  | / _` || '_ \  / _` || '_ ` _ \  / _` || '_ \ 
 | |  | || (_| || | | || (_| || | | | | || (_| || | | |
 |_|  |_| \__,_||_| |_| \__, ||_| |_| |_| \__,_||_| |_|
                         __/ |                         
                        |___/                          

'''

print(logo)
rw = RandomWords()
chosen_word = rw.random_word()



length = len(chosen_word)

display = []
for x in range(length):
    display += '_'

print(display)

end = False
chances = 6
while not end:
    guessed_letter = input("Guess a letter: ").lower()
    for pos in range(length):
        letter = chosen_word[pos]
        if letter == guessed_letter:
            display[pos] = letter

    print(display)

    if guessed_letter not in chosen_word:
        chances -= 1
        if chances == 0:
            end = True
            print("Game Over. You LOSE!")

    if "_" not in display:
        end = True
        print("You win!")
    print(hangman[chances])
