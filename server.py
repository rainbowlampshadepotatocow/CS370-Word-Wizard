# CS 370 - Computer Networks
# Word Wizard Server
# Authors: Mason King, Zander Look, Sulav Ojha
# Environment: Python 3.10 or higher
# Licence: MIT License

import socket
import json

class Game:
    def __init__(self, difficulty="medium"):
        self.difficulties = {
            "easy": {"word": "cat", "max_wrong": 10},
            "medium": {"word": "dragon", "max_wrong": 6},
            "hard": {"word": "programming", "max_wrong": 4}
        }
        
        # Set difficulty
        self.word = self.difficulties[difficulty]["word"]
        self.max_wrong = self.difficulties[difficulty]["max_wrong"]
        
        # Game state
        self.current_wrong_guesses = 0
        self.guessed_letters = []
    
    def print_word(self):
        """Create a display string showing guessed letters"""
        display = ""
        
        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        
        return display.strip()
    
    def make_guess(self, guess):
        """Process a guess and return game status"""
        # Check if the letter has already been guessed
        if guess in self.guessed_letters:
            return "You already guessed that letter.\n"
        
        # Add new guess to the list of guessed letters
        self.guessed_letters.append(guess)
        
        # Check if the guessed letter is in the target word
        if guess in self.word:
            message = "Correct!\n"
        else:
            # Incorrect guess - increment wrong guess counter
            self.current_wrong_guesses += 1
            message = "Wrong!\n"
        
        # Get the current word display showing guessed letters
        display_word = self.print_word()
        
        # Add word display to message
        message += "Word: " + display_word + "\n"
        
        # Add wrong guesses count to message
        message += "Wrong guesses: " + str(self.current_wrong_guesses) + "/" + str(self.max_wrong)
        
        # Check win condition
        if all(letter in self.guessed_letters for letter in self.word):
            message += "\nYou win!"
            return message, True  # Game over - win
        
        # Check lose condition
        if self.current_wrong_guesses >= self.max_wrong:
            message += "\nYou lose! The word was: " + self.word
            return message, True  # Game over - lose
        
        return message, False  # Game continues

def main():
    # Create a TCP/IP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Allow the socket to be reused if the program is restarted quickly
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Bind the socket to localhost on port 5001
    server.bind(("127.0.0.1", 5001))
    
    # Listen for incoming connections (max 1 connection in queue)
    server.listen(1)
    
    print("Server is waiting for the client...")
    
    # Wait for a client connection and accept it
    conn, addr = server.accept()
    
    # Print the client address that connected
    print("Connected by", addr)
    
    #Main game loop
    while True:
        # Get difficulty from client
        data = conn.recv(1024).decode().lower().strip()

        if not data or data == quit:
            break

        # Create game instance with selected difficulty
        game = Game(data)

        # Send the initial word display (all underscores) to the client
        conn.send(game.print_word().encode())

        # Main game loop - continues until win/lose condition is met
        while True:
            # Receive guess from client (max 1024 bytes), convert to lowercase, and remove whitespace
            guess = conn.recv(1024).decode().lower().strip()
            
            # If client sends empty message, exit the loop (client disconnected)
            if not guess:
                break
            
            # Only use the first character of the input (in case client sends multiple characters)
            guess = guess[0]
            
            # Process the guess
            message, game_over = game.make_guess(guess)
            
            # Send the game status message to the client
            conn.send(message.encode())
            
            # Exit the game loop if game is over
            if game_over:
                break
        
        #Ask the client if they want to play again
        play_again = conn.recv(1024).decode().lower().strip()
        if play_again != "y":
            break

    # Close the connection with the client
    conn.close()

    # Close the server socket
    server.close()

if __name__ == "__main__":
    main()