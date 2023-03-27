from abc import abstractmethod


class Conta:
    def __init__(self, id_cliente: int, saldo: float):
        self.id_cliente = id_cliente
        self.saldo = saldo

    @abstractmethod
    def depositar_dinheiro(self, valor_do_deposito):
        pass

    @abstractmethod
    def sacar_dinheiro(self, valor_do_saque):
        pass
    

class ContaCorrente(Conta):
    def __init__(self, id_cliente, saldo, limite_cheque_especial):
        super().__init__(id_cliente, saldo)
        self.limite_cheque_especial = limite_cheque_especial

    def depositar_dinheiro(self, valor_do_deposito: float):
        self.valor_do_deposito = valor_do_deposito

    def sacar_dinheiro(self, valor_do_saque: float):
        self.valor_do_saque = valor_do_saque





class ContaPoupanca(Conta):
    def __init__(self, id_cliente, saldo, taxa_de_rendimento):
        super().__init__(id_cliente, saldo)
        self.taxa_de_rendimento = taxa_de_rendimento
        
    def depositar_dinheiro(self, valor_do_deposito: float):
        self.valor_do_deposito = valor_do_deposito

    def sacar_dinheiro(self, valor_do_saque: float):
        self.valor_do_saque = valor_do_saque

    def verificar_rendimento_ao_ano(self, tempo, unidade_de_tempo: str):
        self.tempo = tempo
        self.unidade_de_tempo = unidade_de_tempo