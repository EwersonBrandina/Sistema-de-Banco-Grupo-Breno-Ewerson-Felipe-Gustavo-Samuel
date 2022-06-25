class Historico:

    def __init__(self, msg= 'Transferência: ', transacoes = []):
        self.transacoes = transacoes
        self.msg = msg

    def transacoes_bancarias(self):
        self.msg = 'Transações:'
        for i in self.transacoes:
            self.msg += '\n - ' + i
