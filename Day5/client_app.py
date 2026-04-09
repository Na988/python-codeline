import socket
import uuid

# --- Configuration (must match server) ---
HOST = '192.168.100.220'
PORT = 9090
USE_TCP = True  # Flag: True = TCP, False = UDP

MESSAGE = f"Hello from Client [ID: {uuid.uuid4()}]"

if USE_TCP:
    # TCP Client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))          # Connect to the server
    print(f"[TCP] Connected to server at {HOST}:{PORT}")

    client_socket.send(MESSAGE.encode())         # Send the message
    print(f"[TCP] Sent: {MESSAGE}")

    response = client_socket.recv(1024)          # Wait for server response
    print(f"[TCP] Server replied: {response.decode()}")

    client_socket.close()

else:
    # UDP Client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    client_socket.sendto(MESSAGE.encode(), (HOST, PORT))  # Send the message
    print(f"[UDP] Sent: {MESSAGE}")

    response, server_addr = client_socket.recvfrom(1024)  # Wait for server response
    print(f"[UDP] Server replied: {response.decode()}")

    client_socket.close()
