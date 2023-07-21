function playGuessingGame(numToGuess, totalGuesses=10){
    let guess = 0;
    let numOfGuesses = 0;
    while (numOfGuesses <= totalGuesses) {
        if (numOfGuesses == 0){
            guess = prompt("Enter a number between 1 and 100.");
            numOfGuesses++;
        }
        else if (isNaN(guess)){
            if (guess == "Cancel"){
                return 0;
            }
            guess = prompt("Please enter a number.");
        }
        else if (guess < numToGuess){
            guess = prompt(guess + ' is too small. Guess a larger number.');
            numOfGuesses++;
        }
        else if (guess > numToGuess){
            guess = prompt(guess + ' is too large. Guess a smaller number.');
            numOfGuesses++;
        }
        else if (guess == numToGuess){
            return numOfGuesses;
        }
    }
    return 0;
}
