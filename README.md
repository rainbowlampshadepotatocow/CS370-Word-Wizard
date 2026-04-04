# CS370-Word-Wizard

Authors: Mason King, Zander Look, Sulav Ojha

We will build a game in Python that will be called "Word Wizard".
It will be a knockoff of the game "Hangman" where you play as a wizard 'battling' a dragon. Each correct guess deals damage to the dragon. Incorrect guesses deal damage to the player's wizard character.
* The health bar for the dragon is calculated by the number of characters in the word to be guessed.
* The health bar for the wizard is calculated by a static number of allowed incorrect guesses (traditionally 6, but we can add multiple difficulty options).
We can also implement a rolling leaderboard (acts more like a live-updating log of recently completed games) that tracks time taken to finish and number of failed guesses to satisfy project requirements if necessary.

CS370
Spring 2026
Term Project

## Project Summary
For the term project, you will be reinforcing the concepts covered throughout the course by creating a client-server socket application. You decide what the end user application does. Some example applications are file servers, instant message apps, media streaming apps, and so on.

## Requirements
* You must use a basic socket package in whichever programming language you choose.
* You must work in a group of 2-3 people. You must form your group in Canvas under the People → Team. Failure to do so may result in delay or not receiving proper credit for your entire group.
* **Due Date: April 7, 2026, 6:00 pm**

## Items to Turn In
* Description of how each group member participated in the project.
* Meeting and participation logs.
* Copies of all code and documentation for the project.
* Video presentation of your project.
  * Give a presentation describing your project.
    * How does the client/server application work?
    * What language did you use? Did you use any other tools?
    * What does your application do?
    * Who are the group members? If can't include a video stream from all members, please include a photo in the presentation.
  * Demo your application.
* Copy of the presentation.

## Game Features
This implementation now supports three difficulty levels:
- Easy: 4 wrong guesses allowed with simple words
- Medium: 6 wrong guesses allowed with medium complexity words
- Hard: 10 wrong guesses allowed with complex words

The game is now modularized with separate classes for game logic and client-server communication.