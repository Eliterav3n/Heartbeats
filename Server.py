# Set up the script as a Python program
# !/usr/bin/env python3

import socket, sys, threading

# Create a TCP/IP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to the port. This part will assign the socket with the server address
    # The local address is 127.0.0.1 as localhost and the local port is 8561
    s.bind(("127.0.0.1", 8561))

    # Set up to listen for incoming connections.
    s.listen()
    print('Waiting for a connection')

    # Accept an incoming connection
    conn, addr = s.accept()

    # Read and write the data
    with conn:
        print('Connected by', addr)

        while True:
            data = conn.recv(1024)

            if not data:
                    break
            conn.sendall(data)
    print('Connection terminated')