import Pyro4

try:
    operando1 = int(input("Entre com o primeiro operando: "))
    operando2 = int(input("Entre com o segundo operando: "))
    operation = input("Entre com a operação (e.g. +, -, *, /): ")

    calculadora = Pyro4.Proxy("PYRONAME:calc.calculadora")
    print("Resultado: ", calculadora.computar(operando1, operando2, operation))
except ValueError:
    print("ERRO: Os valores passados como operando devem ser numéricos!!")
