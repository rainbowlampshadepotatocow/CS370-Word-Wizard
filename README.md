# CS370-Word-Wizard

Authors: Mason King, Zander Look, Sulav Ojha

A client-server implementation of a Hangman-style word guessing game where you play as a wizard battling a dragon. Each correct guess deals damage to the dragon, while incorrect guesses deal damage to your wizard character.

## Overview

**Word Wizard** is a networked game that demonstrates client-server communication using Python sockets. The game features:
- Three difficulty levels with different word complexities and allowed wrong guesses
- Real-time game state updates between client and server
- Modular architecture separating game logic from networking code

## Game Mechanics

- **Dragon Health**: Calculated by the number of characters in the target word
- **Wizard Health**: Based on the number of allowed incorrect guesses (difficulty-dependent)
- **Gameplay**: Guess letters to reveal the hidden word before running out of wrong guesses

## Installation & Setup

### Prerequisites
- Python 3.10 or higher

### Running the Game

#### Starting the Server
```bash
python server.py
```

The server will:
1. Bind to `127.0.0.1:5001`
2. Wait for a client connection
3. Accept difficulty selection from the client
4. Manage game state and process guesses

#### Starting the Client
```bash
python client.py
```

The client will:
1. Connect to the server at `127.0.0.1:5001`
2. Present difficulty selection menu
3. Send user guesses to the server
4. Display game state updates from the server

### Running Both Components

Open two terminal windows:
- **Terminal 1**: Start the server (`python server.py`)
- **Terminal 2**: Start the client (`python client.py`)

## Architecture

### File Structure
```
CS370-Word-Wizard/
├── .gitignore          # Git ignore rules
├── client.py           # Client application with game UI
├── LICENSE             # MIT License
├── README.md           # This file - project documentation
└── server.py           # Server application with game logic
```

### Class Diagram

#### `Game` (in server.py)
- **Purpose**: Contains core game logic and state management
- **Methods**:
  - [`__init__(self, difficulty="medium")`](server.py:10) - Initialize game with selected difficulty
  - [`print_word(self)`](server.py:26) - Create display string showing guessed letters
  - [`make_guess(self, guess)`](server.py:38) - Process a letter guess and return game status
- **Attributes**:
  - `word`: The target word to guess
  - `max_wrong`: Maximum allowed wrong guesses (difficulty-dependent)
  - `current_wrong_guesses`: Count of incorrect guesses made
  - `guessed_letters`: List of letters already guessed

#### `GameClient` (in client.py)
- **Purpose**: Handles client-side networking and user interaction
- **Methods**:
  - [`__init__(self)`](client.py:9) - Initialize TCP socket
  - [`connect_to_server(self)`](client.py:13) - Connect to server at `127.0.0.1:5001`
  - [`select_difficulty(self)`](client.py:17) - Present difficulty menu and get user choice
  - [`start_game(self)`](client.py:36) - Main game loop with networking
- **Attributes**:
  - `client`: TCP socket for server communication

## Difficulty Levels

| Level   | Word          | Max Wrong Guesses |
|---------|---------------|-------------------|
| Easy    | "cat"        | 10                |
| Medium  | "dragon"     | 6                 |
| Hard    | "programming"| 4                 |

## Network Protocol

### Message Format
All messages are UTF-8 encoded strings with a maximum size of 1024 bytes.

### Communication Flow

1. **Client → Server**: Difficulty selection (e.g., "easy", "medium", "hard")
2. **Server → Client**: Initial word display (underscores for each letter)
3. **Client → Server**: Letter guesses (single character)
4. **Server → Client**: Game state updates with:
   - Correct/Wrong feedback
   - Current word display
   - Wrong guesses count
   - Win/Lose condition if applicable

### Port Configuration
- **Server Port**: 5001
- **Protocol**: TCP (SOCK_STREAM)
- **Address**: localhost (`127.0.0.1`)

## Development Notes

### Key Design Decisions

1. **Separation of Concerns**: Game logic is separated from networking code for better maintainability
2. **Modular Difficulty System**: Easy to add new difficulty levels by extending the `difficulties` dictionary
3. **Error Handling**: Graceful handling of network errors and invalid inputs
4. **State Management**: Server maintains all game state, client only displays information

### Extensibility Ideas

1. **Word Database**: Replace hardcoded words with a word list file or API
2. **Additional Difficulties**: Add more levels by extending the `difficulties` dictionary
3. **Multiplayer Support**: Extend to support multiple clients simultaneously
4. **Leaderboard**: Implement a scoring system based on time and wrong guesses
5. **Persistent Storage**: Save game statistics or high scores to a file

### Testing Recommendations

1. Test each difficulty level separately
2. Verify edge cases:
   - Repeated guesses of the same letter
   - Non-alphabetic character inputs
   - Network disconnections
3. Check that win/lose conditions are properly detected

## License

This project is licensed under the MIT License - see the [`LICENSE`](LICENSE) file for details.

## Course Information

**Course**: CS 370 - Computer Networks
**Term**: Spring 2026
**Project Type**: Term Project - Client-Server Socket Application
