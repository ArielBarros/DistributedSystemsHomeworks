from socket import *
import argparse

# Recebendo argumentos de entrada do usuário
parser = argparse.ArgumentParser()
parser.add_argument('serverAddress', type=str, help='Ip do Servidor')
parser.add_argument('serverPort', type=int, help='Porta do Servidor')
parser.add_argument('message', type=str, help='Mensagem a ser enviada')
args = parser.parse_args()

# Crição do socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Setando valor de timeout para 1 segundo
clientSocket.settimeout(1)
# Envio da requisição para o servidor
clientSocket.sendto(args.message.encode(), (args.serverAddress, args.serverPort))

# Tentativa de recepção de resposta do servidor
try:
    data, addr = clientSocket.recvfrom(1024)
    print('{}'.format(data.decode()))
# Tratamento da exceção por timeout
except timeout:
    print("Timeout")

clientSocket.close()
