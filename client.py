# CS 370 - Computer Networks
# Word Wizard Client
# Authors: Mason King, Zander Look, Sulav Ojha
# Environment: Python 3.10 or higher
# Licence: MIT License

import socket

class GameClient:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def connect_to_server(self):
        """Connect to the server"""
        self.client.connect(("127.0.0.1", 5001))
    
    def select_difficulty(self):
        """Allow user to select difficulty level"""
        print("Select difficulty level:")
        print("1. Easy (4 wrong guesses, simple word)")
        print("2. Medium (6 wrong guesses, medium word)")
        print("3. Hard (10 wrong guesses, complex word)")
        
        while True:
            choice = input("Enter your choice (1-3): ").strip()
            match choice:
                case "1":
                    return "easy"
                case "2":
                    return "medium"
                case "3":
                    return "hard"
                case _:
                    print("Invalid choice. Please enter 1, 2, or 3.")
    
    def start_game(self):
        """Start the game with difficulty selection"""
        try:
            # Connect to server
            self.connect_to_server()
            
            # Select difficulty
            difficulty = self.select_difficulty()
            
            # Send difficulty to server
            self.client.send(difficulty.encode())
            
            # Receive and display initial game state
            message = self.client.recv(1024).decode()
            print(message)
            
            # Main game loop
            while True:
                # Prompt user for a letter guess
                guess = input("Guess a letter: ").lower().strip()
                
                # Skip empty inputs
                if not guess:
                    continue
                
                # Send the first character of the guess to the server
                self.client.send(guess[0].encode())
                
                # Receive and display the game response from the server
                response = self.client.recv(1024).decode()
                print("\n" + response)
                
                # Exit loop if the game is over (win or lose condition met)
                if "You win!" in response or "You lose!" in response:
                    break
            
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            # Close the client socket when the game ends
            self.client.close()

def main():
    """Main function to start the game"""
    client = GameClient()
    client.start_game()

if __name__ == "__main__":
    main()