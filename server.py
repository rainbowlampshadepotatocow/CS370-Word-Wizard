import socket

word = "dragon"

current_wrong_guesses = 0
max_wrong = 6

guessed_letters = []

def print_word():
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("127.0.0.1", 5001))
server.listen(1)

print("Server is waiting for the client...")

conn, addr = server.accept()
print("Connected by", addr)

conn.send(print_word().encode())

while True:
    guess = conn.recv(1024).decode().lower().strip()

    if not guess:
        break

    guess = guess[0]

    if guess in guessed_letters:
        message = "You already guessed that letter.\n"
    else:
        guessed_letters.append(guess)

        if guess in word:
            message = "Correct!\n"
        else:
            current_wrong_guesses += 1
            message = "Wrong!\n"

    display_word = print_word()
    message += "Word: " + display_word + "\n"
    message += "Wrong guesses: " + str(current_wrong_guesses) + "/" + str(max_wrong)

    if all(letter in guessed_letters for letter in word):
        message += "\nYou win!"
        conn.send(message.encode())
        break

    if current_wrong_guesses >= max_wrong:
        message += "\nYou lose! The word was: " + word
        conn.send(message.encode())
        break

    conn.send(message.encode())

conn.close()
server.close()