import socket
import threading
import tkinter as tk

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the hostname and port as inputs from the user
host = input("Enter hostname: ")
port = int(input("Enter port: "))

# Connect to the server
client_socket.connect((host, port))

# Create a Tkinter window
window = tk.Tk()
window.title("Texting Program")

# Create a scrolling text box to display the conversation
conversation = tk.Text(window, state='disabled', height=20, width=50)
conversation.pack()

# Create an input field for the user to type their message
message = tk.StringVar()
message_entry = tk.Entry(window, textvariable=message)
message_entry.pack()

# Create a send button
def send():
    message_text = message.get()
    client_socket.send(message_text.encode())
    conversation['state'] = 'normal'
    conversation.insert('end', 'You: ' + message_text + '\n')
    conversation['state'] = 'disabled'
    message_entry.delete(0, 'end')
send_button = tk.Button(window, text="Send", command=send)
send_button.pack()

# Create a function to receive messages in a separate thread
def receive():
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        conversation['state'] = 'normal'
        conversation.insert('end', 'Other: ' + data + '\n')
        conversation['state'] = 'disabled'

# Create a thread to run the receive function
receive_thread = threading.Thread(target=receive)
receive_thread.start()

# Run the Tkinter event loop
window.mainloop()

# Close the connection
client_socket.close()
