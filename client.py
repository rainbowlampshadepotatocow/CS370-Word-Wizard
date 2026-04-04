import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5001))

message = client.recv(1024).decode()
print(message)

while True:
    guess = input("Guess a letter: ").lower().strip()

    if not guess:
        continue

    client.send(guess[0].encode())

    response = client.recv(1024).decode()
    print("\n" + response)

    if "You win!" in response or "You lose!" in response:
        break

client.close()