#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
    // Initialize random seed
    srand(static_cast<unsigned int>(time(0)));

    // Generate a random number between 1 and 100
    int randomNumber = rand() % 100 + 1;
    int userGuess = 0;
    int numberOfTries = 0;

    cout << "Welcome to the Guess the Number Game!" << endl;
    cout << "I have picked a number between 1 and 100. Can you guess it?" << endl;

    // Main game loop
    do {
        cout << "Enter your guess: ";
        cin >> userGuess;
        numberOfTries++;

        if (userGuess > randomNumber) {
            cout << "Too high! Try again." << endl;
        } else if (userGuess < randomNumber) {
            cout << "Too low! Try again." << endl;
        } else {
            cout << "Congratulations! You guessed the correct number in " << numberOfTries << " tries." << endl;
        }
    } while (userGuess != randomNumber);

    return 0;
}