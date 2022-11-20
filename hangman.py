################################################################################
## HANGMAN GAME                                                               ##
## © Jon Landaburu November 2022                                              ##
## CODE FOR Python3                                                           ##
## THE FILE "words.txt" CONATINS ALL THE POSSIBLE WORDS                       ##
################################################################################

################################################################################
## IMPORTS                                                                    ##
################################################################################
import random
import os

################################################################################
## ASCII PICTURE FOR THE HANGMAN                                              ##
################################################################################
HANGMAN_PICTURES = [
"""
   ╔══════════╗
   ╚═╦══════╗ ║
     ║      ║ ║
     ║      ║ ║
            ║ ║
            ║ ║
            ║ ║
            ║ ║
            ║ ║
            ║ ║
            ║ ║
            ║ ║
            ║ ║
            ║ ║
╔═══════════╝ ║
╚═════════════╝""",
"""
   ╔══════════╗
   ╚═╦══════╗ ║
     ║      ║ ║
     ║      ║ ║
   ╔═╩═╗    ║ ║
   ║▘▄▝║    ║ ║
   ╚═══╝    ║ ║
            ║ ║
            ║ ║
            ║ ║
            ║ ║
            ║ ║
            ║ ║
            ║ ║
╔═══════════╝ ║
╚═════════════╝""",
"""
   ╔══════════╗
   ╚═╦══════╗ ║
     ║      ║ ║
     ║      ║ ║
   ╔═╩═╗    ║ ║
   ║▘▄▝║    ║ ║
   ╚═╦═╝    ║ ║
   ╔═╩═╗    ║ ║
   ║   ║    ║ ║
   ║   ║    ║ ║
   ╚═══╝    ║ ║
            ║ ║
            ║ ║
            ║ ║
╔═══════════╝ ║
╚═════════════╝""",
"""
   ╔══════════╗
   ╚═╦══════╗ ║
     ║      ║ ║
     ║      ║ ║
   ╔═╩═╗    ║ ║
   ║▘▄▝║    ║ ║
   ╚═╦═╝    ║ ║
 ╔═╦═╩═╗    ║ ║
 ║ ║   ║    ║ ║
 ║ ║   ║    ║ ║
 ╝ ╚═══╝    ║ ║
            ║ ║
            ║ ║
            ║ ║
╔═══════════╝ ║
╚═════════════╝""",
"""
   ╔══════════╗
   ╚═╦══════╗ ║
     ║      ║ ║
     ║      ║ ║
   ╔═╩═╗    ║ ║
   ║▘▄▝║    ║ ║
   ╚═╦═╝    ║ ║
 ╔═╦═╩═╦═╗  ║ ║
 ║ ║   ║ ║  ║ ║
 ║ ║   ║ ║  ║ ║
 ╝ ╚═══╝ ╚  ║ ║
            ║ ║
            ║ ║
            ║ ║
╔═══════════╝ ║
╚═════════════╝""",
"""
   ╔══════════╗
   ╚═╦══════╗ ║
     ║      ║ ║
     ║      ║ ║
   ╔═╩═╗    ║ ║
   ║▘▄▝║    ║ ║
   ╚═╦═╝    ║ ║
 ╔═╦═╩═╦═╗  ║ ║
 ║ ║   ║ ║  ║ ║
 ║ ║   ║ ║  ║ ║
 ╝ ╠═══╝ ╚  ║ ║
   ║        ║ ║
   ║        ║ ║
  ═╝        ║ ║
╔═══════════╝ ║
╚═════════════╝""",
"""
   ╔══════════╗
   ╚═╦══════╗ ║
     ║      ║ ║
     ║      ║ ║
   ╔═╩═╗    ║ ║
   ║▘▄▝║    ║ ║
   ╚═╦═╝    ║ ║
 ╔═╦═╩═╦═╗  ║ ║
 ║ ║   ║ ║  ║ ║
 ║ ║   ║ ║  ║ ║
 ╝ ╠═══╣ ╚  ║ ║
   ║   ║    ║ ║
   ║   ║    ║ ║
  ═╝   ╚═   ║ ║
╔═══════════╝ ║
╚═════════════╝"""]

################################################################################
## CONSTANTS                                                                  ##
################################################################################
MAX_NUMBER_OF_GUESSES = len(HANGMAN_PICTURES) - 1
STRING_ALPHABET = " a b c d e f g h i j k l m n ñ o p q r s t u v w x  y z"
ALPHABET =STRING_ALPHABET.upper().split()

################################################################################
## chooseRandomWord()                                                         ##
################################################################################
def chooseRandomWord():
    my_file = open("words.txt", "r")
    data = my_file.read()
    data_into_list = data.replace('\n', ' ').split()
    my_file.close()
    return random.choice(data_into_list).upper()

################################################################################
## getWordWithGuessedLetters(guessedLetters, secretWord)                      ##
################################################################################
def getWordWithGuessedLetters(guessedLetters, secretWord):
    text = ""
    for i in range(len(secretWord)):
        if secretWord[i] in guessedLetters:
            text += secretWord[i]
        else:
            text += "-"
    return text

################################################################################
## getGuess(guessedLetters)                                                   ##
################################################################################
def getGuess(guessedLetters):
    while True:
        guessIsValid = True
        guess = input("Type your guess: ")
        guess = guess.upper()
        if len(guess) != 1:
            print("Please try again (type only one letter).")
            guessIsValid = False
        if guess not in ALPHABET:
            print("Please try again (type only one letter).")
            guessIsValid = False
        if guess in guessedLetters:
            print("Please try again (you already guesses the letter " + guess + ").")
            guessIsValid = False

        if guessIsValid == True:
            break
    return guess

################################################################################
## getNumberOfGuessedLetters(guessedLetters, secretWord)                      ##
################################################################################
def getNumberOfGuessedLetters(guessedLetters, secretWord):
    count = 0
    for letter in secretWord:
        if letter in guessedLetters:
            count += 1
    return count

################################################################################
## showBoard(numberOfGuesses, guessedLetters, secretWord)                     ##
################################################################################
def showBoard(numberOfGuesses, guessedLetters, secretWord):
    wordWithGuessedLetters = getWordWithGuessedLetters(guessedLetters, secretWord)
    indexForPicture = numberOfGuesses - getNumberOfGuessedLetters(guessedLetters, secretWord)
    os.system('clear')
    print("The Hangman game")
    print("© Jon Landaburu November 2022")
    print(HANGMAN_PICTURES[indexForPicture])
    print()
    print("Leters already guessed: " + guessedLetters)
    print("Secret word: "+ getWordWithGuessedLetters(guessedLetters, secretWord))
    print()

################################################################################
## def showWinMessage()                                                       ##
################################################################################
def showWinMessage():
    print()
    print("C O N G R A T U L A T I O N S !")
    print("-------------------------------")
    print("You won the game.")

################################################################################
## def showlOSTMessage()                                                      ##
################################################################################
def showLostMessage():
    print()
    print("S O R R Y   Y O U   L O S T !")
    print("-----------------------------")
    print("The word was: " + secretWord)

def askIfPlayAgain():
    while True:
        print()
        text = input("Do you want to play again [y or n] ? ").upper()
        if text == 'Y':
            return True
        elif text == 'N':
            return False

################################################################################
## MAIN                                                                       ##
################################################################################
while True:
    numberOfGuesses = 0
    guessedLetters = ""
    secretWord = chooseRandomWord()

    isGameOver = False
    playerWins = False
    while isGameOver == False:
        showBoard(numberOfGuesses, guessedLetters, secretWord)
        guess = getGuess(guessedLetters)
        guessedLetters += guess
        numberOfGuesses += 1
        numberOfFaults = numberOfGuesses - getNumberOfGuessedLetters(guessedLetters, secretWord)
        allLetterAreGuessed = "-" not in getWordWithGuessedLetters(guessedLetters, secretWord)
        if numberOfFaults >= MAX_NUMBER_OF_GUESSES:
            isGameOver = True
        if allLetterAreGuessed:
            isGameOver = True
            playerWins = True

    showBoard(numberOfGuesses, guessedLetters, secretWord)
    if playerWins == True:
        showWinMessage()
    else:
        showLostMessage()

    if askIfPlayAgain() == False:
        break

print()
print("Goodbye!")
