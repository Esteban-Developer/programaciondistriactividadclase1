import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5000))

# Pedir el nombre al usuario
nombre_estudiante = input("Ingrese su nombre: ")

# Enviar el nombre al servidor
client.sendall(nombre_estudiante.encode())

# Recibir la respuesta del servidor
respuesta = client.recv(1024).decode()
print("Respuesta del servidor:", respuesta)

client.close()
