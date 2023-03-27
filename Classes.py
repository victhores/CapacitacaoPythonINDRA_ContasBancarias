from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, id_cliente: str, saldo: float):
        self.id_cliente = id_cliente
        self.saldo = saldo

    @abstractmethod
    def depositar_dinheiro(self, valor_do_deposito):
        pass

    @abstractmethod
    def sacar_dinheiro(self, valor_do_saque):
        pass
    

class ContaCorrente(Conta):
    clientes_conta_corrente: list[dict[str, object]] = []

    def __init__(self, id_cliente, saldo, limite_cheque_especial: float):
        super().__init__(id_cliente, saldo)
        self.limite_cheque_especial = limite_cheque_especial
        self.clientes_conta_corrente.append({"ID do cliente": "CC" + self.id_cliente,
                                             "Tipo de conta": "Conta Corrente",
                                             "Saldo Atual": self.saldo,
                                             "Limite de Cheque Especial": self.limite_cheque_especial})
    
    def GET_ID_CLIENTE(self):
        return "CC" + self.id_cliente
    
    def GET_SALDO(self):
        return self.saldo

    def SET_SALDO(self, novo_saldo):
        self.saldo = novo_saldo
        for cliente in self.clientes_conta_corrente:
            if cliente["ID do cliente"] == self.GET_ID_CLIENTE():
                cliente["Saldo Atual"] = self.saldo


    def depositar_dinheiro(self, valor_do_deposito: float):
        self.SET_SALDO(self.GET_SALDO() + valor_do_deposito)

    def sacar_dinheiro(self, valor_do_saque: float):
        limite_para_saque = self.GET_SALDO() + self.limite_cheque_especial
        if limite_para_saque >= valor_do_saque:
            self.SET_SALDO(self.GET_SALDO() - valor_do_saque)
        else:
            print("Saldo insuficiente.")





class ContaPoupanca(Conta):
    clientes_conta_poupanca: list[dict[str, object]] = []

    def __init__(self, id_cliente, saldo, taxa_de_rendimento: float):
        super().__init__(id_cliente, saldo)
        self.taxa_de_rendimento = taxa_de_rendimento / 100
        self.clientes_conta_poupanca.append({"ID do cliente": "CP" + self.id_cliente,
                                             "Tipo de conta": "Conta Poupança",
                                             "Saldo Atual": self.saldo})

    def GET_ID_CLIENTE(self):
        return "CP" + self.id_cliente

    def GET_SALDO(self):
        return self.saldo

    def SET_SALDO(self, novo_saldo):
        self.saldo = novo_saldo
        for cliente in self.clientes_conta_poupanca:
            if cliente["ID do cliente"] == self.GET_ID_CLIENTE():
                cliente["Saldo Atual"] = self.saldo
                return self.saldo


    def depositar_dinheiro(self, valor_do_deposito: float):
        self.SET_SALDO(self.GET_SALDO() + valor_do_deposito)

    def sacar_dinheiro(self, valor_do_saque: float):
        limite_para_saque = self.GET_SALDO()
        if limite_para_saque >= valor_do_saque:
            self.SET_SALDO(self.GET_SALDO() - valor_do_saque)
        else:
            print("Saldo insuficiente.")

    def verificar_rendimento_no_tempo_determinado(self, tempo: int, unidade_de_tempo: str):
        self.tempo = tempo
        self.unidade_de_tempo = unidade_de_tempo

class PoupancaViewer():
    def __init__(self):
        pass

    def visualizar_clientes_conta_poupanca(self):
        print(ContaPoupanca.clientes_conta_poupanca)

class CorrenteViewer():
    def __init__(self):
        pass
    
    def visualizar_clientes_conta_corrente(self):
        print(ContaCorrente.clientes_conta_corrente)


poupanca = PoupancaViewer()
victor = ContaPoupanca(id_cliente="09", saldo=1000.0, taxa_de_rendimento=10)
poupanca.visualizar_clientes_conta_poupanca()
victor.depositar_dinheiro(20.0)
poupanca.visualizar_clientes_conta_poupanca()
victor.sacar_dinheiro(12)
poupanca.visualizar_clientes_conta_poupanca()
