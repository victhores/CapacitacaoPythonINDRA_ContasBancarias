from ContaPoupanca import ContaPoupanca

class ContaPoupancaViewer():
    # classe auxiliar cuja única funcionalidade é exibir os dados dos clientes de conta poupança

    def __init__(self):
        pass


    def get_dados_do_cliente_conta_poupanca(self, id_alvo: str):
        # exibe os dados do cliente com base no seu ID

        for cliente in ContaPoupanca.clientes_conta_poupanca:
            if cliente["ID do cliente"] == "CP" + id_alvo:
                print(cliente)
        else:
            print("[ERRO] Não há nenhum cliente de conta poupança com esse ID.")
            # erro caso não exista cliente com o ID fornecido


    def visualizar_clientes_conta_poupanca(self):
        print(ContaPoupanca.clientes_conta_poupanca)
            # exibe todos os cliente de conta corrente