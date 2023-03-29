from ContaCorrente import ContaCorrente

class ContaCorrenteViewer():
    # classe auxiliar cuja única funcionalidade é exibir os dados dos clientes de conta corrente
     
    def __init__(self):
        pass
    

    def visualizar_dados_do_cliente_conta_corrente(self, id_alvo: str):
        # exibe os dados do cliente com base no seu ID.

        for cliente in ContaCorrente.clientes_conta_corrente:
            if cliente["ID do cliente"] == "CC" + id_alvo:
                print(cliente)
            else:
                print("[ERRO] Não há nenhum cliente de conta corrente com esse ID.")
                    # erro caso não exista cliente com o ID fornecido
        

    def visualizar_clientes_conta_corrente(self):
        print(ContaCorrente.clientes_conta_corrente)
            # exibe todos os cliente de conta corrente

paulo = ContaCorrente(id_cliente="1", saldo=1000, limite_cheque_especial=200)

paulo.depositar_dinheiro(valor_do_deposito=-100)

paulo.sacar_dinheiro(valor_do_saque=-2020)

corrente=ContaCorrenteViewer()

corrente.visualizar_dados_do_cliente_conta_corrente("2")
