import socket

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the address and port to receive the data
address = 'localhost'
port = 12345

# Bind the socket to the address and port
sock.bind((address, port))

# Listen for incoming connections
sock.listen(1)

# Accept the connection from the sender script
conn, addr = sock.accept()

while True:
    # Receive the variable
    data = conn.recv(1024).decode()

    if not data:
        break

    # Print the received variable
    print("Received:", data)

# Close the connection and socket
conn.close()
sock.close()
