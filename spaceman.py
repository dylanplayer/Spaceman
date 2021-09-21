import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def spaceman(secret_word):
    
    gameIsOver = False
    gameIsWin = False
    
    guessedLetters = ''
    for i in range(len(secret_word)):
        guessedLetters += "_"

    print(guessedLetters)
    # while(not gameIsOver):



#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
