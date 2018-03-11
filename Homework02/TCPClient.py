from socket import *
import argparse
import pickle
from requisicao import Requisicao

# Tratamento para os argumentos da linha de comando
parser = argparse.ArgumentParser()
parser.add_argument('serverAddress', type=str, help='Ip do Servidor')
parser.add_argument('serverPort', type=int, help='Porta do Servidor')
parser.add_argument('operands', type=int, help='Operandos forma: a b', nargs=2)
parser.add_argument('operation', type=str, help='Operação: soma, sub, div, multi')
args = parser.parse_args()

# Cria socket e conecta com o servidor
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.settimeout(1)
clientSocket.connect((args.serverAddress, args.serverPort))

# Cria objeto do tipo Requisicao
request = Requisicao(args.operands[0], args.operands[1], args.operation)

# Envia o objeto serializado.
clientSocket.send(pickle.dumps(request))
# Recebe resposta do calculo feito pelo servidor
try:
    result = clientSocket.recv(1024)
    print('Result: {}'.format(result.decode()))
except timeout:
    print("Timeout")


clientSocket.close()
