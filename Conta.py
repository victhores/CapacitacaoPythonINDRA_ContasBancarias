from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, id_cliente: str, saldo: float):
        self.id_cliente = id_cliente
        self.saldo = saldo

    @abstractmethod
    def get_id_cliente(self):
        pass
    
    @abstractmethod
    def get_saldo(self):
        pass

    @abstractmethod
    def set_saldo(self, novo_saldo):
        pass

    @abstractmethod
    def depositar_dinheiro(self, valor_do_deposito):
        pass

    @abstractmethod
    def sacar_dinheiro(self, valor_do_saque):
        pass