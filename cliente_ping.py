from socket import *
import time

# Define o endereço e a porta do servidor
server_address = ('localhost', 1200)

# Cria o socket UDP do cliente
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Define um timeout de 1 segundo para o recebimento
clientSocket.settimeout(1)

# Loop para enviar 10 mensagens de ping
for i in range(10):
    message = f"Ping {i+1}"
    try:
        # Registra o tempo de envio
        send_time = time.time()

        # Envia a mensagem para o servidor
        clientSocket.sendto(message.encode(), server_address)

        # Espera pela resposta do servidor
        data, server = clientSocket.recvfrom(1024)

        # Registra o tempo de recebimento
        recv_time = time.time()

        # Calcula o Round Trip Time (RTT) em milissegundos
        rtt = (recv_time - send_time) * 1000
        print(f"Resposta de {server[0]}:{server[1]}, RTT: {rtt:.2f} ms")

    except timeout:
        print(f"Tempo limite excedido para Ping {i+1}")

# Fecha o socket do cliente 
clientSocket.close()