#include "mainwindow.h"
#include "./ui_mainwindow.h"
#include <fstream>
#include <string>
#include <QDebug>
#include <random> // for random number generation
#include <set>

// Inputs: QWidget *parent - Pointer to the parent widget
// Description: Initializes the main window, connects buttons to respective methods, initializes variables, and selects a random word for the game.
MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    this->setWindowTitle("WordleAssist");
	
	// Connect Buttons to Methods
    connect(ui->guessButton, &QPushButton::clicked, this, &MainWindow::checkGuess);
    connect(ui->updateButton, &QPushButton::clicked, this, &MainWindow::updateAssistant);
    connect(ui->restartGameButton, &QPushButton::clicked, this, &MainWindow::restartGame);
    connect(ui->restartAssistButton, &QPushButton::clicked, this, &MainWindow::restartAssistant);
	
	// Initialize Variables
    gameGuessCount = 0;
    assistantGuessCount = 0;
    selectRandomWord(true, true);
}

// Destructor for the MainWindow class
// Description: Performs cleanup and deallocates resources when the MainWindow object is destroyed.
MainWindow::~MainWindow()
{
    delete ui;
}

// Inputs: bool initGameList - Flag indicating whether to initialize the game word list
//         bool initAssistantList - Flag indicating whether to initialize the assistant word list
// Description: Loads words from a file, selects a random word, and initializes word lists based on input flags.
void MainWindow::selectRandomWord(bool initGameList, bool initAssistantList) {
    // Load word list
    std::ifstream file("wordlist.txt");

    if (file.is_open()) {
		
		// Store each word into QStringList
        std::string line;
        while (std::getline(file, line)) {
            textArray.append(QString::fromStdString(line)); 
        }

        file.close();

        if (!textArray.empty()) {
			
			// Randomly select word
            std::random_device rd;
            std::mt19937 gen(rd());
            std::uniform_int_distribution<> dist(0, textArray.size() - 1);
            int randomIndex = dist(gen);
            randomlySelectedWord = textArray[randomIndex];

			// Initialize word lists for each tab
            if (initGameList) {
                gameList = textArray;
            }
            if (initAssistantList) {
                assistList = textArray;
            }
			
			// Display Initial Word Lists
            displayInitialList(initGameList, initAssistantList);

            qDebug() << "Randomly selected word:" << randomlySelectedWord;
        } else {
            qDebug() << "The file is empty.";
        }
    } else {
        qDebug() << "Unable to open the file.";
    }
}

// Description: Processes the user's guess, updates the game interface, and handles game logic.
void MainWindow::checkGuess() {

	// Loads guessed word from QLineEdits
    QString guessedWord = ui->lineEdit_1->text().toLower() +
                              ui->lineEdit_2->text().toLower() +
                              ui->lineEdit_3->text().toLower() +
                              ui->lineEdit_4->text().toLower() +
                              ui->lineEdit_5->text().toLower();


    // Check if the guessed word matches the randomly selected word
    if (guessedWord != "" && guessedWord.size() == 5 && textArray.contains(guessedWord)) {
		
		// Increment guess count
        gameGuessCount = gameGuessCount + 1;

		// Iterate through each letter in guessed word
        for (int i = 0; i < 5; ++i) {
			
            // Initialize variable labels
            QString labelObjectName = QString("label_%1_%2").arg(gameGuessCount).arg(i + 1);
            QLabel* currentLabel = this->findChild<QLabel*>(labelObjectName);
            QString labelLetterName = QString("label_%1").arg(guessedWord[i]);
            QLabel* letterLabel = this->findChild<QLabel*>(labelLetterName);

            if (currentLabel) {
                QString color = "";

                // Change label values and colors
                currentLabel->setText(QString(guessedWord[i]).toUpper());
                if (guessedWord[i] == randomlySelectedWord[i]) {
                    currentLabel->setStyleSheet("color: green;");
                    letterLabel->setStyleSheet("color: green;");
                    color = "green";
                }
                else if (randomlySelectedWord.contains(guessedWord[i])) {
                    currentLabel->setStyleSheet("color: orange;");
                    QString styleSheet = letterLabel->styleSheet().toLower();
                    if (!styleSheet.contains("color: green") and !styleSheet.contains("color: #008000")) {
                        letterLabel->setStyleSheet("color: orange;");
                    }
                    color = "orange";
                }
                else {
                    currentLabel->setStyleSheet("color: red;");
                    letterLabel->setStyleSheet("color: red;");
                    color = "red";
                }

                // Trim word list based on result and current index
                trimGameWordList(guessedWord[i], color, i);
            }
        }

        // Update and display current word list
        displayFilteredGameList();

        // Update UI
        ui->remainingWordsLabel->setText("Words Remaining: " + QString::number(gameList.size()));
        ui->guessCountLabel->setText("Guesses: " + QString::number(gameGuessCount));
        ui->lineEdit_1->setText("");
        ui->lineEdit_2->setText("");
        ui->lineEdit_3->setText("");
        ui->lineEdit_4->setText("");
        ui->lineEdit_5->setText("");
        ui->gameFeedbackLabel->setText("");

    } else {
        // Handle invalid input length (not exactly 5 characters)
        ui->gameFeedbackLabel->setText("Please enter a valid five-letter word.");
        qDebug() << "Please enter a valid five-letter word.";
    }

    // Handle end of game text
    if (gameGuessCount == 6 || guessedWord == randomlySelectedWord) {
        ui->guessButton->setEnabled(false);
        if (gameGuessCount == 6 && guessedWord != randomlySelectedWord) {
            ui->gameFeedbackLabel->setText("Out of guesses!  Random word was: " + randomlySelectedWord);
        }
        if (guessedWord == randomlySelectedWord) {
            ui->gameFeedbackLabel->setText("You guessed the correct word, " + randomlySelectedWord + "!");
        }
    }
}

// Description: Processes the assistant's guess, updates its display, and handles assistant's logic.
void MainWindow::updateAssistant(){

    // Loads guessed word from QLineEdits
    QString guessedWord = ui->lineEdit_1_assist->text().toLower() +
                          ui->lineEdit_2_assist->text().toLower() +
                          ui->lineEdit_3_assist->text().toLower() +
                          ui->lineEdit_4_assist->text().toLower() +
                          ui->lineEdit_5_assist->text().toLower();


    // Check if the guessed word matches the randomly selected word
    if (guessedWord != "" && guessedWord.size() == 5 && textArray.contains(guessedWord)) {
        assistantGuessCount = assistantGuessCount + 1;

        // Iterate through each letter in guessed word
        for (int i = 0; i < 5; ++i) {

            // Initialize variable labels and combo boxes
            QString labelObjectName = QString("label_%1_%2_assist").arg(assistantGuessCount).arg(i + 1);
            QLabel* currentLabel = this->findChild<QLabel*>(labelObjectName);
            QString labelLetterName = QString("label_%1_2").arg(guessedWord[i]);
            QLabel* letterLabel = this->findChild<QLabel*>(labelLetterName);
            QString colorComboName = QString("colorCombo_%1").arg(i + 1);
            QComboBox* colorComboBox = this->findChild<QComboBox*>(colorComboName);

            if (currentLabel) {

                // Change label values and colors
                QString color = colorComboBox->currentText().toLower();
                currentLabel->setText(QString(guessedWord[i]).toUpper());
                QString labelStyleSheet = "color: " + color + ";";
                currentLabel->setStyleSheet(labelStyleSheet);
                letterLabel->setStyleSheet(labelStyleSheet);

                // Trim word list based on result and current index
                trimAssistantWordList(guessedWord[i], color, i);
            }
        }

        // Update and display current word list
        displayFilteredAssistList();

        // Update UI
        ui->remainingWordsLabel_assist->setText("Words Remaining: " + QString::number(assistList.size()));
        ui->guessCountLabel_assist->setText("Guesses: " + QString::number(assistantGuessCount));
        ui->lineEdit_1_assist->setText("");
        ui->lineEdit_2_assist->setText("");
        ui->lineEdit_3_assist->setText("");
        ui->lineEdit_4_assist->setText("");
        ui->lineEdit_5_assist->setText("");
        ui->assistantFeedbackLabel->setText("");

    } else {
        // Handle invalid input length (not exactly 5 characters)
        ui->assistantFeedbackLabel->setText("Please enter a valid five-letter word.");
    }

    // Handle end of game text
    if (assistantGuessCount == 6) {
        ui->updateButton->setEnabled(false);
        ui->assistantFeedbackLabel->setText("Out of guesses!");
    }
}

// Inputs: const QString& guessedLetter - Guessed letter
//         const QString& color - Color of the guessed letter (green, orange, red)
//         int i - Index of the guessed letter in the word
// Description: Eliminates words from the game word list based on guessed letters and colors.
void MainWindow::trimGameWordList(const QString& guessedLetter, const QString& color, int i) {

    // Eliminate words without correct letter in current index
    if (color == "green") {
        for (int j = 0; j < gameList.size(); ++j) {
            if  (guessedLetter != gameList[j][i]) {
                gameList.removeAt(j);
                --j;
            }
        }

    }
    // Eliminate words not containing correct letter or correct letter in wrong position
    else if (color == "orange") {
        for (int j = 0; j < gameList.size(); ++j) {
            if  (!gameList[j].contains(guessedLetter) || guessedLetter == gameList[j][i]) {
                gameList.removeAt(j);
                --j;
            }
        }
    }
    // Eliminate words containing incorrect letter
    else if (color == "red") {
        for (int j = 0; j < gameList.size(); ++j) {
            if  (gameList[j].contains(guessedLetter)) {
                gameList.removeAt(j);
                --j;
            }
        }
    }
}

// Inputs: const QString& guessedLetter - Guessed letter
//         const QString& color - Color of the guessed letter (green, orange, red)
//         int i - Index of the guessed letter in the word
// Description: Eliminates words from the assistant word list based on guessed letters and colors.
void MainWindow::trimAssistantWordList(const QString& guessedLetter, const QString& color, int i) {
    // Eliminate words without correct letter in current index
    if (color == "green") {
        for (int j = 0; j < assistList.size(); ++j) {
            if  (guessedLetter != assistList[j][i]) {
                assistList.removeAt(j);
                --j;
            }
        }

    }
    // Eliminate words not containing correct letter or correct letter in wrong position
    else if (color == "orange") {
        for (int j = 0; j < assistList.size(); ++j) {
            if  (!assistList[j].contains(guessedLetter) || guessedLetter == assistList[j][i]) {
                assistList.removeAt(j);
                --j;
            }
        }
    }
    // Eliminate words containing incorrect letter
    else if (color == "red") {
        for (int j = 0; j < assistList.size(); ++j) {
            if  (assistList[j].contains(guessedLetter)) {
                assistList.removeAt(j);
                --j;
            }
        }
    }
}

// Inputs: bool initGameList - Flag indicating whether to display the game word list
//         bool initAssistantList - Flag indicating whether to display the assistant word list
// Description: Loads initial filtered lists from a file and displays them in the UI based on input flags.
void MainWindow::displayInitialList(bool initGameList, bool initAssistantList) {
    // Display initial guess list from .txt file to save computational time
    std::ifstream file("initialFilteredList.txt");
    if (file.is_open()) {
        QString textToDisplay;
        std::string line;

        // Add each line and a newline character
        while (std::getline(file, line)) {
            textToDisplay += QString::fromStdString(line) + "\n";
        }

        file.close();

        // Set the text of the QTextEdit to the accumulated text
        if (initGameList) {
            ui->textEdit->setText(textToDisplay);
            ui->remainingWordsLabel->setText("Words Remaining: " + QString::number(gameList.size()));
            ui->guessCountLabel->setText("Guesses: " + QString::number(gameGuessCount));
        }
        if (initAssistantList) {
            ui->textEdit_assist->setText(textToDisplay);
            ui->remainingWordsLabel_assist->setText("Words Remaining: " + QString::number(gameList.size()));
            ui->guessCountLabel_assist->setText("Guesses: " + QString::number(gameGuessCount));
        }

    } else {
        qDebug() << "Unable to open the initial filtered list file.";
    }
}

// Inputs: const QString& word - Word for which unique letters need to be counted
// Outputs: int - Count of unique letters in the word
// Description: Calculates and returns the count of unique letters in a word.
int countUniqueLetters(const QString& word) {
    // Find unique letter count in word
    std::set<QChar> uniqueChars;
    for (const QChar& ch : word) {
        uniqueChars.insert(ch);
    }
    return uniqueChars.size();
}

// Description: Calculates and displays the filtered game word list in the UI.
void MainWindow::displayFilteredGameList() {
    QMap<QString, int> wordEliminationCounts;

    // Calculate elimination counts for each word in filteredList
    for (const QString& currentWord : gameList) {
        int currentWordElimination = calculateMinimax(currentWord);
        wordEliminationCounts.insert(currentWord, currentWordElimination);
    }

    // Sort the filteredList based on the wordEliminationCounts and unique letter count using a lambda function
    std::sort(gameList.begin(), gameList.end(), [&wordEliminationCounts](const QString& wordA, const QString& wordB) {
        if (wordEliminationCounts[wordA] == wordEliminationCounts[wordB]) {
            int uniqueLettersCountA = countUniqueLetters(wordA);
            int uniqueLettersCountB = countUniqueLetters(wordB);
            return uniqueLettersCountA > uniqueLettersCountB;
        }
        return wordEliminationCounts[wordA] > wordEliminationCounts[wordB];
    });

    QString textToDisplay;

    // Iterate through sorted filteredList and append each word with its index and guess impact to textToDisplay
    for (int index = 0; index < gameList.size(); ++index) {
        QString currentWord = gameList[index];
        int currentGuessImpact = wordEliminationCounts[currentWord];
        textToDisplay += QString("%1. %2 (Guess Impact: %3)\n").arg(index + 1).arg(currentWord).arg(currentGuessImpact);
    }

    // Set the text of the QTextEdit to the accumulated text
    ui->textEdit->setText(textToDisplay);
}

// Description: Calculates and displays the filtered assistant word list in the UI.
void MainWindow::displayFilteredAssistList() {
    QMap<QString, int> wordEliminationCounts;

    // Calculate elimination counts for each word in filteredList
    for (const QString& currentWord : assistList) {
        int currentWordElimination = calculateAssistantMinimax(currentWord);
        wordEliminationCounts.insert(currentWord, currentWordElimination);
    }
    // Sort the filteredList based on the wordEliminationCounts and unique letter count using a lambda function
    std::sort(assistList.begin(), assistList.end(), [&wordEliminationCounts](const QString& wordA, const QString& wordB) {
        if (wordEliminationCounts[wordA] == wordEliminationCounts[wordB]) {
            int uniqueLettersCountA = countUniqueLetters(wordA);
            int uniqueLettersCountB = countUniqueLetters(wordB);
            return uniqueLettersCountA > uniqueLettersCountB;
        }
        return wordEliminationCounts[wordA] > wordEliminationCounts[wordB];
    });
    QString textToDisplay;

    // Iterate through sorted filteredList and append each word with its index and guess impact to textToDisplay
    for (int index = 0; index < assistList.size(); ++index) {
        QString currentWord = assistList[index];
        int currentGuessImpact = wordEliminationCounts[currentWord];
        textToDisplay += QString("%1. %2 (Guess Impact: %3)\n").arg(index + 1).arg(currentWord).arg(currentGuessImpact);
    }
    // Set the text of the QTextEdit to the accumulated text
    ui->textEdit_assist->setText(textToDisplay);
}

// Inputs: const QString& word - Word for which the minimax value needs to be calculated
// Outputs: int - Minimax value for the word in the game
// Description: Calculates and returns the minimax value for a word in the game.
int MainWindow::calculateMinimax(const QString& word) {
    // Initialize with a high value to find the minimum impact
    int minMaxImpact = INT_MAX;

    for (int letterIndex = 0; letterIndex < word.size(); ++letterIndex) {
        QString guessedLetter = word[letterIndex];

        // Calculate the elimination count for this guessed letter
        int maxLetterElimination = 0;

        // Simulate guessing this word and count how many words it eliminates
        for (const QString& candidateWord : gameList) {
            int currentWordElimination = 0;

            for (int candidateLetterIndex = 0; candidateLetterIndex < candidateWord.size(); ++candidateLetterIndex) {
                if ((candidateLetterIndex == letterIndex && candidateWord[candidateLetterIndex] != guessedLetter) ||
                    (candidateLetterIndex != letterIndex && candidateWord[candidateLetterIndex] == guessedLetter)) {
                    currentWordElimination++;
                }
            }

            if (currentWordElimination > maxLetterElimination) {
                maxLetterElimination = currentWordElimination;
            }
        }

        // Update the minMaxImpact (minimum of maximum elimination counts)
        if (maxLetterElimination < minMaxImpact) {
            minMaxImpact = maxLetterElimination;
        }
    }

    return minMaxImpact;
}

// Inputs: const QString& word - Word for which the minimax value needs to be calculated
// Outputs: int - Minimax value for the word in the assistant's guesses
// Description: Calculates and returns the minimax value for a word in the assistant's guesses.
int MainWindow::calculateAssistantMinimax(const QString& word) {
    // Initialize with a high value to find the minimum impact
    int minMaxImpact = INT_MAX;

    for (int letterIndex = 0; letterIndex < word.size(); ++letterIndex) {
        QString guessedLetter = word[letterIndex];

        // Calculate the elimination count for this guessed letter
        int maxLetterElimination = 0;

        // Simulate guessing this word and count how many words it eliminates
        for (const QString& candidateWord : assistList) {
            int currentWordElimination = 0;

            for (int candidateLetterIndex = 0; candidateLetterIndex < candidateWord.size(); ++candidateLetterIndex) {
                if ((candidateLetterIndex == letterIndex && candidateWord[candidateLetterIndex] != guessedLetter) ||
                    (candidateLetterIndex != letterIndex && candidateWord[candidateLetterIndex] == guessedLetter)) {
                    currentWordElimination++;
                }
            }

            if (currentWordElimination > maxLetterElimination) {
                maxLetterElimination = currentWordElimination;
            }
        }

        // Update the minMaxImpact (minimum of maximum elimination counts)
        if (maxLetterElimination < minMaxImpact) {
            minMaxImpact = maxLetterElimination;
        }
    }

    return minMaxImpact;
}

// Description: Resets game-related variables and elements in the UI to restart the game.
void MainWindow::restartGame() {
    // Reset Feedback Text
    ui->gameFeedbackLabel->setText("");

    // Reset guessCount
    gameGuessCount = 0;
    ui->guessCountLabel->setText("Guesses: " + QString::number(gameGuessCount));

    // Delete previous guesses
    for (int i = 1; i <= 6; ++i){
        for (int j = 1; j <= 5; ++j) {
            QString labelObjectName = QString("label_%1_%2").arg(i).arg(j);
            QLabel* currentLabel = this->findChild<QLabel*>(labelObjectName);
            currentLabel->setText("");
        }
    }

    // Remove colors from letter labels
    QStringList alphabetList = QStringList() << "a" << "b" << "c" << "d" << "e" << "f" << "g" << "h" << "i" << "j" << "k"
                                             << "l" << "m" << "n" << "o" << "p" << "q" << "r" << "s" << "t" << "u" << "v"
                                             << "w" << "x" << "y" << "z";
    for (QString letter : alphabetList) {
        QString labelLetterName = QString("label_%1").arg(letter);
        QLabel* letterLabel = this->findChild<QLabel*>(labelLetterName);
        letterLabel->setStyleSheet("color: black;");
    }

    // Reenable guess button
    if (!ui->guessButton->isEnabled()) {
        ui->guessButton->setEnabled(true);
    }

    // Reset word list
    textArray.clear();
    gameList.clear();
    selectRandomWord(true, false);

}

// Description: Resets assistant-related variables and elements in the UI to restart its guessing process.
void MainWindow::restartAssistant() {
    // Reset Feedback Text
    ui->assistantFeedbackLabel->setText("");

    // Reset guessCount
    assistantGuessCount = 0;
    ui->guessCountLabel_assist->setText("Guesses: " + QString::number(assistantGuessCount));

    // Delete previous guesses
    for (int i = 1; i <= 6; ++i){
        for (int j = 1; j <= 5; ++j) {
            QString labelObjectName = QString("label_%1_%2_assist").arg(i).arg(j);
            QLabel* currentLabel = this->findChild<QLabel*>(labelObjectName);
            currentLabel->setText("");
        }
    }

    // Remove colors from letter labels
    QStringList alphabetList = QStringList() << "a" << "b" << "c" << "d" << "e" << "f" << "g" << "h" << "i" << "j" << "k"
                                             << "l" << "m" << "n" << "o" << "p" << "q" << "r" << "s" << "t" << "u" << "v"
                                             << "w" << "x" << "y" << "z";
    for (QString letter : alphabetList) {
        QString labelLetterName = QString("label_%1_2").arg(letter);
        QLabel* letterLabel = this->findChild<QLabel*>(labelLetterName);
        letterLabel->setStyleSheet("color: black;");
    }

    // Reenable guess button
    if (!ui->updateButton->isEnabled()) {
        ui->updateButton->setEnabled(true);
    }

    // Reset word list
    textArray.clear();
    assistList.clear();
    selectRandomWord(false, true);
}
