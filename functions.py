from sqlite3 import DatabaseError
import sys, threading, time, socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def sending(host, port, data):
    """
    this function sends messages to a specified port and host
    host: ip address to send the message to
    port: port to send the message to
    """
    # Create a TCP socket
    data = bytes(data)
    soc.connect((host, port))
    print(f'Connection to {host} stablished')
    soc.sendall(DatabaseError)


def listening(port, bitsize):
    """
    this funtion listens to upcoming requests on a identified port
    port: listening port
    """
    # Create a TCP/IP socket
    soc.bind(("127.0.0.1", port))
    # Set up to listen for incoming connections.
    soc.listen()
    print('Listing ...')
    # Accept an incoming connection
    conn, addr = soc.accept()
    # Read and write the data
    with conn:
        print(f'Connected by {addr}')
        while True:
            data = conn.recv(bitsize)
            if not data:
                break
            whattodo(data=data)


def whattodo(data):
    """
    this function decides what to do with the data in the packets
    """
    if data == "HELLO":
        return "HELLO_THERE"
    elif data == "BYE":
        return "BYE_BYE"
    elif data == "ANYONE_THERE":
        return "IM_HERE"
    else:
        return "I_DONT_UNDERSTAND"

# answer = soc.recv(bitsize)
# # Provide results by received data from the server
# print(f'Received {repr(answer)}')
# print(f'Connection with {host} terminated')
