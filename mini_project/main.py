# Wordle words link: https://gist.github.com/dracos/dd0668f281e685bad51479e5acaadb93
import random

def getWordAndList():
    filename = "wordlist.txt"
    wordList = []
    wordToGuess = ""
    
    with open(filename, 'r') as file:
        wordList = file.read().splitlines()
        wordToGuess = random.choice(wordList)
        # print(f"The randomly selected word is: {wordToGuess}")  

    return wordToGuess, wordList

def containsNonLetter(userGuess):
    for char in userGuess:
        if not char.isalpha():
            return True  # Return True if a non-letter character is found
    return False  # Return False if all characters are letters
    
def main():
    # random.seed(2023)
    keepPlaying = "y"
    
    while(keepPlaying == "y"):
    
        wordToGuess, wordList = getWordAndList()
        solved = False
        
        while(not solved):
            invalidGuess = True
            userGuess = ""
            while(invalidGuess):
                userGuess = input("Please enter a guess: ").lower()
                if len(userGuess) != 5:
                    print("Invalid length")
                elif containsNonLetter(userGuess):
                    print("Invalid character(s)")
                elif userGuess not in wordList:
                    print("Not in word list")
                else:
                    invalidGuess = False
            print("Your guess is:", userGuess)
            if userGuess == wordToGuess:
                print("Congratulations, you guessed the wordle!")
                solved = True
            else:
                hint = ""
                for i in range(5):
                    if userGuess[i] == wordToGuess[i]:
                        hint = hint + userGuess[i].upper()
                    elif userGuess[i] in wordToGuess:
                        hint = hint + userGuess[i]
                    else:
                        hint = hint + "*"
                print("Hint: " + hint)
        invalidAnswer = True
        while(invalidAnswer):
            keepPlaying = input("Would you like to play again? [y/n] ").lower()
            if keepPlaying == "y" or keepPlaying == "n":
                invalidAnswer = False

if __name__ == "__main__":
    main()