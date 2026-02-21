import socket
import threading

def handle_client(conn, addr):
    print(f"Cliente conectado desde {addr}")
    
    try:
        # Recibir el nombre del cliente
        student_name = conn.recv(1024).decode()
        
        # Mostrar el nombre en el servidor
        print(f"Nombre del cliente: {student_name}")
        
        # Respuesta personalizada
        response = f"Hola {student_name}, estás conectado a un servidor concurrente!"
        conn.sendall(response.encode())

    except Exception as e:
        print(f"Error con {addr}: {e}")
    
    finally:
        conn.close()
        print(f"Conexión cerrada con {addr}\n")

# Crear socket del servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5000))
server.listen(5)

print("Servidor concurrente escuchando...")

while True:
    conn, addr = server.accept()
    
    # Crear un hilo por cada cliente
    client_thread = threading.Thread(
        target=handle_client,
        args=(conn, addr)
    )
    client_thread.start()
