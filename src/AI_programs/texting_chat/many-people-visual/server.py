import socket
import threading

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the hostname and port as inputs from the user
host = input("Enter hostname: ")
port = int(input("Enter port: "))

# Bind the socket to the host and port
server_socket.bind((host, port))

# Start listening for incoming connections
server_socket.listen(5)

# Create a list to store the connections to all the clients
connections = []


# Create a function to handle a new client
def handle_client(connection, address):
    # Print a message to the server console
    print("Connected to:", address)

    # Add the connection to the list of connections
    connections.append(connection)

    # Create a loop to receive messages from the client
    while True:
        data = connection.recv(1024).decode()
        if not data:
            # If no data is received, the connection is probably closed
            break

        # Print the message to the server console
        print("Received message from", address, ":", data)

        # Send the message to all the other clients
        for conn in connections:
            if conn != connection:
                conn.send(data.encode())

    # Remove the connection from the list of connections
    connections.remove(connection)

    # Close the connection
    connection.close()


# Create a loop to accept new connections
while True:
    # Accept a new connection
    connection, address = server_socket.accept()

    # Start a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(connection, address))
    client_thread.start()

# Close the server socket
server_socket.close()
