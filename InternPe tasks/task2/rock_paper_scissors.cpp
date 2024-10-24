#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
    srand(time(0)); // Seed the random number generator

    int playerChoice, computerChoice;
    string choices[] = {"Rock", "Paper", "Scissors"};

    while (true) {
        cout << "Enter your choice (1 for Rock, 2 for Paper, 3 for Scissors): ";
        cin >> playerChoice;

        if (playerChoice < 1 || playerChoice > 3) {
            cout << "Invalid choice. Please enter a number between 1 and 3.\n";
            continue;
        }

        computerChoice = rand() % 3 + 1; // Generate a random number between 1 and 3

        cout << "You chose: " << choices[playerChoice - 1] << endl;
        cout << "Computer chose: " << choices[computerChoice - 1] << endl;

        if (playerChoice == computerChoice) {
            cout << "It's a tie!\n";
        } else if ((playerChoice == 1 && computerChoice == 3) ||
                   (playerChoice == 2 && computerChoice == 1) ||
                   (playerChoice == 3 && computerChoice == 2)) {
            cout << "You win!\n";
        } else {
            cout << "Computer wins!\n";
        }

        cout << "Do you want to play again? (y/n): ";
        char playAgain;
        cin >> playAgain;
        if (playAgain != 'y' && playAgain != 'Y') {
            break;
        }
    }

    return 0;
}