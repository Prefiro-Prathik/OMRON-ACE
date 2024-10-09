import socket

ace_ip = '127.0.0.1'  # Replace with the actual IP address
ace_port = 43600           # Replace with the actual port number


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to ACE Osram server
    s.connect((ace_ip, ace_port))
    
    # Send a command (e.g., change color)
    s.sendall(b"MOVE TRANS(100, 200, 300)\n")
    
    # Receive response
    data = s.recv(1024)
    print(f"Received response: {data.decode('utf-8')}")
