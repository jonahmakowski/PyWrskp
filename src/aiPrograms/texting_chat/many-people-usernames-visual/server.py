import socket
import threading
import tkinter as tk

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the hostname and port as inputs from the user
host = input("Enter hostname: ")
port = int(input("Enter port: "))

# Bind the socket to the host and port
server_socket.bind((host, port))

# Start listening for incoming connections
server_socket.listen(5)

# Create a dictionary to store the connections and usernames of all the clients
clients = {}

# Create a Tkinter window
window = tk.Tk()
window.title("Server")

# Create a function to send a message to all the clients
def send():
    message_text = message.get()
    for conn, name in clients.items():
        conn.send((username + ": " + message_text).encode())

# Create a variable to store the message
message = tk.StringVar()

# Create an input field for the user to type their message
message_entry = tk.Entry(window, textvariable=message)
message_entry.pack()

# Create a send button
send_button = tk.Button(window, text="Send", command=send)
send_button.pack()

# Enter the username
username = input("Enter your username: ")

# Run the Tkinter event loop
window.mainloop()

# Create a function to handle a new client
def handle_client(connection, address):
    # Receive the username from the client
    username = connection.recv(1024).decode()

    # Print a message to the server console
    print("Connected to", username, "at", address)

    # Add the connection and username to the dictionary of clients
    clients[connection] = username

    # Create a loop to receive messages from the client
    while True:
        data = connection.recv(1024).decode()
        if not data:
            # If no data is received, the connection is probably closed
            break

        # Print the message to the server console
        print(username, ":", data)

        # Send the message to all the other clients
        for conn, name in clients.items():
            if conn != connection:
                conn.send((username + ": " + data).encode())

    # Remove the connection and username from the dictionary of clients
    del clients[connection]

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
