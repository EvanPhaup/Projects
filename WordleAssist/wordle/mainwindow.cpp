#include "mainwindow.h"
#include "./ui_mainwindow.h"
#include <fstream>
#include <string>
#include <QDebug>
#include <random> // for random number generation
#include <set>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    this->setWindowTitle("WordleAssist");
    connect(ui->guessButton, &QPushButton::clicked, this, &MainWindow::checkGuess);
    connect(ui->updateButton, &QPushButton::clicked, this, &MainWindow::updateAssistant);
    connect(ui->restartGameButton, &QPushButton::clicked, this, &MainWindow::restartGame);
    connect(ui->restartAssistButton, &QPushButton::clicked, this, &MainWindow::restartAssistant);
    gameGuessCount = 0;
    assistantGuessCount = 0;
    selectRandomWord(true, true);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::selectRandomWord(bool initGameList, bool initAssistantList) {
    // Load text from a .txt file into an array when MainWindow is created
    std::ifstream file("wordlist.txt"); // Replace "../wordlist.txt" with your file's path

    if (file.is_open()) {
        std::string line;
        while (std::getline(file, line)) {
            textArray.append(QString::fromStdString(line)); // Store each line from the file in the vector
        }

        file.close(); // Close the file after reading

        if (!textArray.empty()) {
            std::random_device rd;
            std::mt19937 gen(rd()); // Initialize the random number generator without a fixed seed

            // Generate a random index within the range of textArray size
            std::uniform_int_distribution<> dist(0, textArray.size() - 1);
            int randomIndex = dist(gen);

            // Get the randomly selected word from textArray and store it in the QString variable
            randomlySelectedWord = textArray[randomIndex];

            if (initGameList) {
                gameList = textArray;
            }
            if (initAssistantList) {
                assistList = textArray;
            }

            displayInitialList(initGameList, initAssistantList);
            //displayFilteredList();

            // For demonstration, output the selected word to qDebug
            qDebug() << "Randomly selected word:" << randomlySelectedWord;
        } else {
            qDebug() << "The file is empty.";
        }
    } else {
        qDebug() << "Unable to open the file.";
    }
}


void MainWindow::checkGuess() {

    QString guessedWord = ui->lineEdit_1->text().toLower() +
                              ui->lineEdit_2->text().toLower() +
                              ui->lineEdit_3->text().toLower() +
                              ui->lineEdit_4->text().toLower() +
                              ui->lineEdit_5->text().toLower();


    // Check if the guessed word matches the randomly selected word
    if (guessedWord != "" && guessedWord.size() == 5 && textArray.contains(guessedWord)) {
        gameGuessCount = gameGuessCount + 1;

        for (int i = 0; i < 5; ++i) {
            QString labelObjectName = QString("label_%1_%2").arg(gameGuessCount).arg(i + 1);
            QLabel* currentLabel = this->findChild<QLabel*>(labelObjectName);
            QString labelLetterName = QString("label_%1").arg(guessedWord[i]);
            QLabel* letterLabel = this->findChild<QLabel*>(labelLetterName);

            if (currentLabel) {
                QString color = "";
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
                trimGameWordList(guessedWord[i], color, i);
            }
        }

        displayFilteredGameList();
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

void MainWindow::updateAssistant(){
    QString guessedWord = ui->lineEdit_1_assist->text().toLower() +
                          ui->lineEdit_2_assist->text().toLower() +
                          ui->lineEdit_3_assist->text().toLower() +
                          ui->lineEdit_4_assist->text().toLower() +
                          ui->lineEdit_5_assist->text().toLower();


    // Check if the guessed word matches the randomly selected word
    if (guessedWord != "" && guessedWord.size() == 5 && textArray.contains(guessedWord)) {
        assistantGuessCount = assistantGuessCount + 1;

        for (int i = 0; i < 5; ++i) {
            QString labelObjectName = QString("label_%1_%2_assist").arg(assistantGuessCount).arg(i + 1);
            QLabel* currentLabel = this->findChild<QLabel*>(labelObjectName);
            QString labelLetterName = QString("label_%1_2").arg(guessedWord[i]);
            QLabel* letterLabel = this->findChild<QLabel*>(labelLetterName);
            QString colorComboName = QString("colorCombo_%1").arg(i + 1);
            QComboBox* colorComboBox = this->findChild<QComboBox*>(colorComboName);

            if (currentLabel) {
                QString color = colorComboBox->currentText().toLower();
                currentLabel->setText(QString(guessedWord[i]).toUpper());
                QString labelStyleSheet = "color: " + color + ";";
                currentLabel->setStyleSheet(labelStyleSheet);
                letterLabel->setStyleSheet(labelStyleSheet);

                trimAssistantWordList(guessedWord[i], color, i);
            }
        }

        displayFilteredAssistList();
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

    if (assistantGuessCount == 6) {
        ui->updateButton->setEnabled(false);
        ui->assistantFeedbackLabel->setText("Out of guesses!");
    }
}

void MainWindow::trimGameWordList(const QString& guessedLetter, const QString& color, int i) {
    if (color == "green") {
        for (int j = 0; j < gameList.size(); ++j) {
            if  (guessedLetter != gameList[j][i]) {
                gameList.removeAt(j);
                --j;
            }
        }

    }
    else if (color == "orange") {
        for (int j = 0; j < gameList.size(); ++j) {
            if  (!gameList[j].contains(guessedLetter) || guessedLetter == gameList[j][i]) {
                gameList.removeAt(j);
                --j;
            }
        }
    }
    else if (color == "red") {
        for (int j = 0; j < gameList.size(); ++j) {
            if  (gameList[j].contains(guessedLetter)) {
                gameList.removeAt(j);
                --j;
            }
        }
    }
}

void MainWindow::trimAssistantWordList(const QString& guessedLetter, const QString& color, int i) {
    if (color == "green") {
        for (int j = 0; j < assistList.size(); ++j) {
            if  (guessedLetter != assistList[j][i]) {
                assistList.removeAt(j);
                --j;
            }
        }

    }
    else if (color == "orange") {
        for (int j = 0; j < assistList.size(); ++j) {
            if  (!assistList[j].contains(guessedLetter) || guessedLetter == assistList[j][i]) {
                assistList.removeAt(j);
                --j;
            }
        }
    }
    else if (color == "red") {
        for (int j = 0; j < assistList.size(); ++j) {
            if  (assistList[j].contains(guessedLetter)) {
                assistList.removeAt(j);
                --j;
            }
        }
    }
}


void MainWindow::displayInitialList(bool initGameList, bool initAssistantList) {
    std::ifstream file("initialFilteredList.txt"); // Replace "../initialFilteredList.txt" with your file's path

    if (file.is_open()) {
        QString textToDisplay;
        std::string line;

        while (std::getline(file, line)) {
            textToDisplay += QString::fromStdString(line) + "\n"; // Add each line and a newline character
        }

        file.close(); // Close the file after reading

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

int countUniqueLetters(const QString& word) {
    std::set<QChar> uniqueChars;
    for (const QChar& ch : word) {
        uniqueChars.insert(ch);
    }
    return uniqueChars.size();
}

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

int MainWindow::calculateMinimax(const QString& word) {
    int minMaxImpact = INT_MAX; // Initialize with a high value to find the minimum impact

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

int MainWindow::calculateAssistantMinimax(const QString& word) {
    int minMaxImpact = INT_MAX; // Initialize with a high value to find the minimum impact

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
