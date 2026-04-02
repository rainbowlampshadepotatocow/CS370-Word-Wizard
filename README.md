# CS370-Word-Wizard

We will build a game in Python that will be called "Word Wizard".
It will be a knockoff of the game "Hangman" where you play as a wizard 'battling' a dragon. Each correct guess deals damage to the dragon. Incorrect guesses deal damage to the player's wizard character.
* The health bar for the dragon is calculated by the number of characters in the word to be guessed.
* The health bar for the wizard is calculated by a static number of allowed incorrect guesses (traditionally 6, but we can add multiple difficulty options).
We can also implement a rolling leaderboard (acts more like a live-updating log of recently completed games) that tracks time taken to finish and number of failed guesses to satisfy project requirements if necessary.
