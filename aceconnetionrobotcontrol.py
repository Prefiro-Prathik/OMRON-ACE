import socket

ace_ip = '127.0.0.1'  # Replace with actual IP address
ace_port = 48987      # Replace with actual port number

vplus_program = """
.PROGRAM rob.pythonfunction()

    SIGNAL 1

.END
"""
# Adding a newline or proper delimiter
vplus_program += "\n"  # Adjust based on ACE system's protocol

# Create a TCP/IP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        # Connect to the ACE Osram server
        s.connect((ace_ip, ace_port))
        print(f"Connected to ACE Osram server at {ace_ip}:{ace_port}")

        # Send the V+ program
        s.sendall(vplus_program.encode('utf-8'))
        print("V+ program sent.")

        # Try receiving a response later (optional)
        try:
            data = s.recv(1024)  # This can be optional
            print(f"Received response: {data.decode('utf-8')}")
        except socket.error:
            print("No response received or connection closed.")

    except socket.error as e:
        print(f"Socket error: {e}")
