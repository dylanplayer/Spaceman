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
    """
    Returns boolean based on if the guessed letter is in the secret word
        Parameters:
            a(str): secret word
            b(guess): guessed letter
        Returns:
            a(boolean): if guessed letter is in secret word
    """
    for letter in secret_word:
        if letter == guess:
            return True
    return False

def getIndexsOf(secret_word, letter):
    """
    Returns a list of indexs with a specific letter
        Parameters:
            a(str): secret word
            b(list): letter you want to find
        Returns:
            a(list): list of indexes where a specific letter exists
    """
    indexes = []
    for i in range(len(secret_word)):
        if letter == secret_word[i]:
            indexes.append(i)
    return indexes

def toString(guessedLetters):
    """
    Returns the contents of an array as a string
        Parameters:
            a(list): list of characters
        Returns:
            a(str): string with list of e
    """
    str = ''
    for letter in guessedLetters:
        str += letter
    return str

def spaceman(secret_word):
    """
    Controls Game and Game State
        Parameters:
            a(string): secret word game
        Returns:
            None
    """
    gameIsOver = False
    gameIsWin = False
    incorrectGuesses = 0
    guessedLetters = []
    allGuessed = []
    for i in range(len(secret_word)):
        guessedLetters.append("_")

    while(not gameIsOver):
        print("----------------")
        guess = input("Guess a letter: ")
        if isInWord(toString(allGuessed), guess):
            print(f"Already guessed: {guess}")
        elif isInWord(secret_word, guess):
            indexesOfLetter = getIndexsOf(secret_word, guess)
            for i in indexesOfLetter:
                guessedLetters[i] = guess
            if toString(guessedLetters) == secret_word:
                gameIsOver = True
                gameIsWin = True
            print(f"Guess: {toString(guessedLetters)}\n{7 - incorrectGuesses} guesses left")
        else:
            print("Guess Incorrect")
            incorrectGuesses += 1
            print(f"Guess: {toString(guessedLetters)}\n{7 - incorrectGuesses} guesses left")
            if incorrectGuesses == 7:
                gameIsOver = True
        allGuessed.append(guess)

    if gameIsWin:
        print("You Win")
    else:
        print(f"You Lose the word was {secret_word}")

asciiFile = open('ascii.txt', 'r')
asciiArray = asciiFile.readlines()
for line in asciiArray:
    print(line, end="")
asciiFile.close()
print()

secret_word = load_word()
spaceman(secret_word)

