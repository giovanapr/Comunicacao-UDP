import socket

# Configurações do servidor
HOST = "10.10.2.1"  # Endereço IP do servidor
PORT = 20000        # Porta do servidor

# Criando o socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print(f"Servidor UDP rodando em {HOST}:{PORT}")

while True:
    data, addr = server_socket.recvfrom(1024)  # Recebe dados do cliente
    print(f"Mensagem recebida de {addr}: {data.decode()}")

    # Responde ao cliente
    response = "Mensagem recebida!"
    server_socket.sendto(response.encode(), addr)
