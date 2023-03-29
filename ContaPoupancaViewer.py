from ContaPoupanca import ContaPoupanca

class ContaPoupancaViewer():
    # classe auxiliar cuja única funcionalidade é exibir os dados dos clientes de conta poupança

    def __init__(self):
        pass

    def visualizar_clientes_conta_poupanca(self):
        print(ContaPoupanca.clientes_conta_poupanca)
            # exibe todos os cliente de conta corrente