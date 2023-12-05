# Wordle words link: https://gist.github.com/dracos/dd0668f281e685bad51479e5acaadb93
import random
import tkinter as tk

def getWordAndList():
    filename = "wordlist.txt"
    wordList = []
    wordToGuess = ""
    
    with open(filename, 'r') as file:
        wordList = file.read().splitlines()
        wordToGuess = random.choice(wordList)
        print(f"The randomly selected word is: {wordToGuess}")  

    return wordToGuess, wordList

def game(wordToGuess):

    def validate_input(new_value):
        return len(new_value) <= 1  # Allow only one character

    def submit():
        guessed_word = [entry.get() for entry in entry_fields]  # Get values from entry fields
        for i in range(5):
            guessed_letter = guessed_word[i]
            actual_letter = wordToGuess[i]

            labels[i].config(text=guessed_letter)  # Update corresponding label text with guessed word
            
            if guessed_letter == actual_letter:
                labels[i].config(fg='green')  # Change text color to green if guessed correctly
            elif guessed_letter in wordToGuess and guessed_letter != actual_letter:
                labels[i].config(fg='yellow')  # Change text color to yellow if guessed letter exists in wordToGuess but doesn't match at this position
            else:
                labels[i].config(fg='black')  # Reset text color to black if guessed incorrectly
             
    
    # Create the main Tkinter window
    root = tk.Tk()
    root.title("Wordle Bot")
    #root.geometry("1280x720")

    # Labels in a row
    guess_labels = []
    for guess in range(6):
        guess_frame = tk.Frame(root)
        guess_frame.pack()

        labels = []
        for i in range(5):
            label = tk.Label(guess_frame, text=" ", font=('Arial', 24))
            label.grid(row=guess, column=i, padx=5)
            labels.append(label)
        
        guess_labels.append(labels)

    # Frame to contain the input fields
    input_frame = tk.Frame(root)
    input_frame.pack()

    entry_fields = []
    vcmd = root.register(validate_input)  # Register the validation function

    for i in range(5):
        entry = tk.Entry(input_frame, width=2, font=('Arial', 24), validate="key", validatecommand=(vcmd, '%P'))
        entry.grid(row=0, column=i, padx=5)
        entry_fields.append(entry)

    # Submit button placed after the entry fields
    submit_button = tk.Button(input_frame, text="Submit", command=submit)
    submit_button.grid(row=0, column=5, padx=5)

    root.mainloop()
    
def main():
    random.seed(2023)
    
    wordToGuess, wordList = getWordAndList()
    game(wordToGuess)
    

if __name__ == "__main__":
    main()