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

def isInWord(secret_word, guess):
    for letter in secret_word:
        if letter == guess:
            return True
    return False

def getIndexsOf(secret_word, letter):
    indexes = []
    for i in range(len(secret_word)):
        if letter == secret_word[i]:
            indexes.append(i)
    return indexes

def toString(guessedLetters):
    str = ''
    for letter in guessedLetters:
        str += letter
    return str

def spaceman(secret_word):
    
    gameIsOver = False
    gameIsWin = False
    incorrectGuesses = 0
    guessedLetters = []
    for i in range(len(secret_word)):
        guessedLetters.append("_")

    while(not gameIsOver):
        guess = input("Guess a letter: ")
        if isInWord(secret_word, guess):
            indexesOfLetter = getIndexsOf(secret_word, guess)
            for i in indexesOfLetter:
                guessedLetters[i] = guess
            if toString(guessedLetters) == secret_word:
                gameIsOver = True
                gameIsWin = True
        else:
            incorrectGuesses += 1
            if incorrectGuesses == 7:
                gameIsOver = True
        print(f"Guess: {toString(guessedLetters)}\n{7 - incorrectGuesses} guesses left")

    if gameIsWin:
        print("You Win")
    else:
        print("You Lose")


#These function calls that will start the game
secret_word = load_word()
print(secret_word)
spaceman(secret_word)
