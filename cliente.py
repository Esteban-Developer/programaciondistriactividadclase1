import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5000))

nombre = client.recv(1024).decode()
print(f"Hola, el estudiante conectado es: {nombre}")

client.close()
