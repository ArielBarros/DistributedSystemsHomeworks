from socket import *
import argparse
import threading
import pickle
import sys
from requisicao import Requisicao

# Tratamento para os argumentos da linha de comando
parser = argparse.ArgumentParser()
parser.add_argument('serverPort', type=int, help='Porta do Servidor')
args = parser.parse_args()

lock = threading.Lock()

def handlerConnection(conn, clientAddress):
    # Recebe e Deserializa objeto do tipo Requisicao
    request = pickle.loads(conn.recv(1024))
    # Realiza o calculo
    result = request.computation()
    # Escreve no log, utilizando a trava do monitor
    with lock:
        arq = open("access.log", "a", encoding="utf-8")
        arq.write("[{} {} {}][{}]\n".format(request.num1, request.num2, request.operation, clientAddress))
        arq.close()
    # Envia resposta ao cliente e fecha conexao
    conn.send(str(result).encode())
    conn.close()

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', args.serverPort))
serverSocket.listen(5)
print('Servidor Escutando...')
print('Para encerrar o servidor tecle CTRL+C\n\n')

try:
    while True:
        # Para cada novo cliente uma Thread eh disparada e trata a requisicao
        connectionSocket, clientAddress = serverSocket.accept()
        threading.Thread(target=handlerConnection, args=(connectionSocket, clientAddress[0])).start()
except KeyboardInterrupt:
    print("Encerrando servidor")
    sys.exit()
