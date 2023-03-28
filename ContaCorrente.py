from Conta import Conta

class ContaCorrente(Conta):
    clientes_conta_corrente: list[dict[str, object]] = []

    def __init__(self, id_cliente, saldo, limite_cheque_especial: float):
        super().__init__(id_cliente, saldo)
        if saldo >= 0:
            if limite_cheque_especial >= 0:
                self.limite_cheque_especial = limite_cheque_especial
                self.clientes_conta_corrente.append({"ID do cliente": "CC" + self.id_cliente,
                                                    "Tipo de conta": "Conta Corrente",
                                                    "Saldo Atual": self.saldo,
                                                    "Limite de Cheque Especial": self.limite_cheque_especial})
            else:
                print("[ERRO 03] O valor inserido em 'limite_cheque_especial' é inválido. Tente Novamente.")
        else:
            print("[ERRO 00] O valor inserido em 'saldo' é inválido. Tente Novamente.")
        
    def get_id_cliente(self):
        return "CC" + self.id_cliente


    def get_saldo(self):
        return self.saldo

    def set_saldo(self, novo_saldo):
        self.saldo = novo_saldo
        for cliente in self.clientes_conta_corrente:
            if cliente["ID do cliente"] == self.get_id_cliente():
                cliente["Saldo Atual"] = self.saldo
                return self.saldo
            
    def get_limite_de_cheque_especial(self):
        return self.limite_cheque_especial                

    def depositar_dinheiro(self, valor_do_deposito: float):
        if valor_do_deposito >= 0:
            self.set_saldo(self.get_saldo() + valor_do_deposito)
        else:
            print("[ERRO 01] O valor inserido em 'valor_do_deposito' é inválido. Tente Novamente.")

    def sacar_dinheiro(self, valor_do_saque: float):
        if valor_do_saque >= 0:
            limite_para_saque = self.get_saldo() + self.get_limite_de_cheque_especial()
            if limite_para_saque >= valor_do_saque:
                self.set_saldo(self.get_saldo() - valor_do_saque)
            else:
                print("Saldo insuficiente.")
        else:
            print("[ERRO 02] O valor inserido em 'valor_do_saque' é inválido. Tente Novamente.")
