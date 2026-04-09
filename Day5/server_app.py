import socketserver

# --- Configuration ---
HOST = 'localhost'
PORT = 9090
USE_TCP = True  # Flag: True = TCP, False = UDP


class TCPHandler(socketserver.BaseRequestHandler):
    """Called automatically for each incoming TCP connection."""

    def handle(self):
        message = self.request.recv(1024).decode()   # Receive message
        print(f"[TCP] Received from {self.client_address}: {message}")

        self.request.send(b"HI")                     # Respond with "HI"
        print("[TCP] Sent: HI")


class UDPHandler(socketserver.BaseRequestHandler):
    """Called automatically for each incoming UDP packet."""

    def handle(self):
        message = self.request[0].decode()           # Receive message
        sock = self.request[1]
        print(f"[UDP] Received from {self.client_address}: {message}")

        sock.sendto(b"HI", self.client_address)      # Respond with "HI"
        print("[UDP] Sent: HI")


if USE_TCP:
    server = socketserver.TCPServer((HOST, PORT), TCPHandler)
    print(f"[TCP] Server listening on {HOST}:{PORT}... (Ctrl+C to stop)")
else:
    server = socketserver.UDPServer((HOST, PORT), UDPHandler)
    print(f"[UDP] Server listening on {HOST}:{PORT}... (Ctrl+C to stop)")

server.serve_forever()  # Keep running, handles each request automatically

