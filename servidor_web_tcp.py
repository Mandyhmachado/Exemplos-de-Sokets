from socket import *
import sys
import os

# Define o endereço IP e a porta para o servidor
serverPort = 8080
serverSocket = socket(AF_INET, SOCK_STREAM)

# Associa o socket ao endereço e porta
try:
    serverSocket.bind(('', serverPort))
except error as e:
    print(f"Erro ao associar o socket: {e}")
    sys.exit()

# Coloca o socket em modo de escuta (permite até 1 conexão pendente)
serverSocket.listen(1)
print(f'Servidor web rodando na porta {serverPort}')

def serve_file(connectionSocket, filepath, content_type='application/octet-stream'):
    try:
        with open(filepath, 'rb') as f:
            outputdata = f.read()
        response = b'HTTP/1.1 200 OK\r\n'
        response += f'Content-Type: {content_type}\r\n'.encode()
        response += b'\r\n'
        response += outputdata
        connectionSocket.sendall(response)
        return True
    except FileNotFoundError:
        response = b'HTTP/1.1 404 Not Found\r\n\r\n<html><body><h1>404 Not Found</h1></body></html>\r\n'
        connectionSocket.sendall(response)
        return False

while True:
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        print(f'Recebida requisição de {addr}: {message.splitlines()[0]}')

        filename = message.split()[1]
        filepath = filename[1:]

        if filepath == 'qrcode_perguntas.png':
            serve_file(connectionSocket, filepath, 'image/png')
        elif filepath == 'style.css':
            serve_file(connectionSocket, filepath, 'text/css')
        elif filepath == '':
            serve_file(connectionSocket, 'index.html', 'text/html; charset=utf-8')
        elif filepath == 'index.html':
            serve_file(connectionSocket, filepath, 'text/html; charset=utf-8')
        else:
            serve_file(connectionSocket, filepath, 'text/html; charset=utf-8')

    except Exception as e:
        print(f"Erro ao processar a requisição: {e}")

    finally:
        connectionSocket.close()