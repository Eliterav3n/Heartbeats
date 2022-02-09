# Set up the script as a Python program
# !/usr/bin/env python3

import socket
import sys

# Create a TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

# Connect to the server.
# The local address is 127.0.0.1 as localhost and the local port is 8561
# The local address is used because the server is running on the same computer.
    s.connect(("127.0.0.1", 8561))
    print('Connected to the server successfully!')

    # Write and read the data as test
    s.sendall(b'Hello, world')
    data = s.recv(1024)

    # Provide results by received data from the server
    print('Received', repr(data))
    print('Connection terminated')