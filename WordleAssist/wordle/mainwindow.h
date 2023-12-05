#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui {
class MainWindow;
}
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void selectRandomWord(bool initGameList, bool initAssistantList);
    void checkGuess();
    void updateAssistant();
    void trimGameWordList(const QString& guessedLetter, const QString& color, int index);
    void trimAssistantWordList(const QString& guessedLetter, const QString& color, int index);
    void displayInitialList(bool initGameList, bool initAssistantList);
    void displayFilteredGameList();
    void displayFilteredAssistList();
    int calculateMinimax(const QString& word);
    int calculateAssistantMinimax(const QString& word);
    void restartGame();
    void restartAssistant();

private:
    Ui::MainWindow *ui;
    QString randomlySelectedWord;
    int gameGuessCount;
    int assistantGuessCount;
    QStringList textArray;
    QStringList gameList;
    QStringList assistList;
};
#endif // MAINWINDOW_H
