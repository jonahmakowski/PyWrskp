# Server-side script

import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the hostname and port as inputs from the user
host = input("Enter hostname: ")
port = int(input("Enter port: "))

# Bind the socket to the host and port
server_socket.bind((host, port))

# Start listening for incoming connections
server_socket.listen(1)

# Accept the incoming connection
connection, address = server_socket.accept()

print("Connected to:", address)

while True:
    # Receieve data from the client
    data = connection.recv(1024).decode()
    if not data:
        # If no data is received, the connection is probably closed
        break
    print("Received message:", data)

    # Send a message back to the client
    message = input("Enter message to send: ")
    connection.send(message.encode())

# Close the connection
connection.close()

