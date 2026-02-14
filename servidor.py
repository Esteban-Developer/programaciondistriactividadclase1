import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5000))
server.listen(1)

print("Servidor esperando conexión...")

conn, addr = server.accept()
print("Cliente conectado:", addr)

nombre_estudiante = "Esteban Murillo"
conn.sendall(nombre_estudiante.encode())

conn.close()
