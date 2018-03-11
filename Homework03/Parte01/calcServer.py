import Pyro4

@Pyro4.expose
class Calculadora(object):
	def computar(self, operando1, operando2, operation):
		if(operation == '+'):
			return operando1 + operando2
		elif(operation == '-'):
			return operando1 - operando2
		elif(operation == '*'):
			return operando1 * operando2
		elif (operation == '/'):
			try:
				return operando1 / operando2
			except ZeroDivisionError:
				return "ERRO! Em uma divisão, o 2º operando não pode ser 0 (zero)."
		else:
			return "ERRO! O caractere informado não representa um operando (+, -, *, /)."


print("Iniciando servidor...\n")

daemon = Pyro4.Daemon()                # Cria um Pyro daemon
ns = Pyro4.locateNS()                  # Procura um name server
uri = daemon.register(Calculadora)     # Registra Calculadora como um objeto Pyro
ns.register("calc.calculadora", uri)   # Registra o objeto com um nome no nameserver

print("Servidor pronto para uso.\n\nAperte CTRL+C para encerrar.")
daemon.requestLoop()                   # Inicia um loop que espera por conexoes
