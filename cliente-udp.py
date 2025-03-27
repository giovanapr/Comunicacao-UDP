import socket

# Configurações do servidor
HOST = "10.10.2.1"
PORT = 20000

# Criando o socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Mensagem para o servidor
message = "Olá, servidor!"
client_socket.sendto(message.encode(), (HOST, PORT))
print(message)
# Recebendo a resposta do servidor
data, server = client_socket.recvfrom(1024)
print(f"Resposta do servidor: {data.decode()}")

# Fecha o socket
client_socket.close()
