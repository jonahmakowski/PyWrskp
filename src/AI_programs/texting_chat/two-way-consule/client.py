# Client-side script

import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the hostname and port as inputs from the user
host = input("Enter hostname: ")
port = int(input("Enter port: "))

# Connect to the server
client_socket.connect((host, port))

while True:
    # Send a message to the server
    message = input("Enter message to send: ")
    client_socket.send(message.encode())

    # Receive a message from the server
    data = client_socket.recv(1024).decode()
    if not data:
        # If no data is received, the connection is probably closed
        break
    print("Received message:", data)

# Close the connection
client_socket.close()

