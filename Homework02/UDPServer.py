from socket import *
import argparse
import threading
import sys

# Função a ser passada para thread que irá tratar a requisição
def atendeReq(message, clientAddress):
    print('Cliente {} enviou a mensagem "{}"'.format(clientAddress, message.decode()))
    print('Para encerrar o servidor tecle CTRL+C\n\n')
    modifiedMessage = message[::-1]
    serverSocket.sendto(modifiedMessage, clientAddress)

# Recebendo argumentos de entrada do usuário
parser = argparse.ArgumentParser()
parser.add_argument('serverPort', type=int, help='Porta do Servidor')
args = parser.parse_args()

# Crição e inicialização do socket do servidor
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', args.serverPort))
print('Servidor Escutando...')
print('Para encerrar o servidor tecle CTRL+C\n\n')

# Recepção das requisições do cliente e criação da thread para atender
try:
    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        threading.Thread(target=atendeReq, args=(message, clientAddress)).start()
except KeyboardInterrupt:
    print("\nEncerrando servidor")
    sys.exit()
