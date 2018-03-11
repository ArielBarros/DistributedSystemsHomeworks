class Requisicao(object):
    def __init__(self, num1, num2, operation):
        self.num1 = num1
        self.num2 = num2
        self.operation = operation

    def computation(self):
        if self.operation == 'soma':
            return self.num1 + self.num2
        elif self.operation == 'sub':
            return self.num1 - self.num2
        elif self.operation == 'multi':
            return self.num1 * self.num2
        elif self.operation == 'div':
            return self.num1 / self.num2
        else:
            return None
