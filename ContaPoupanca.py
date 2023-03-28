from Conta import Conta

class ContaPoupanca(Conta):
    clientes_conta_poupanca: list[dict[str, object]] = []


    def __init__(self, id_cliente, saldo, taxa_de_rendimento: float):
        super().__init__(id_cliente, saldo)
        if saldo >= 0:
            if taxa_de_rendimento >= 0:
                self.taxa_de_rendimento = taxa_de_rendimento / 100
                self.clientes_conta_poupanca.append({"ID do cliente": "CP" + self.id_cliente,
                                                    "Tipo de conta": "Conta Poupança",
                                                    "Saldo Atual": self.saldo})
            else:
                print("[ERRO 04] O valor inserido em 'taxa_de_rendimento' é inválido. Tente Novamente.")
        else:
            print("[ERRO 00] O valor inserido em 'saldo' é inválido. Tente Novamente.")


    def get_id_cliente(self):
        return "CP" + self.id_cliente


    def get_saldo(self):
        return self.saldo


    def set_saldo(self, novo_saldo):
        self.saldo = novo_saldo
        for cliente in self.clientes_conta_poupanca:
            if cliente["ID do cliente"] == self.get_id_cliente():
                cliente["Saldo Atual"] = self.saldo
                return self.saldo


    def get_taxa_de_rendimento(self):
        return self.taxa_de_rendimento


    def depositar_dinheiro(self, valor_do_deposito: float):
        if valor_do_deposito >= 0:
            self.set_saldo(self.get_saldo() + valor_do_deposito)
        else:
            print("[ERRO 01] O valor inserido em 'valor_do_deposito' é inválido. Tente Novamente.")


    def sacar_dinheiro(self, valor_do_saque: float):
        if valor_do_saque >= 0:
            limite_para_saque = self.get_saldo()
            if limite_para_saque >= valor_do_saque:
                self.set_saldo(self.get_saldo() - valor_do_saque)
            else:
                print("Saldo insuficiente.")
        else:
            print("[ERRO 02] O valor inserido em 'valor_do_saque' é inválido. Tente Novamente.")


    def verificar_rendimento_no_tempo_determinado(self, tempo: int, unidade_de_tempo: str):
        if tempo >= 0:
            unidades_disponiveis_tempo = {"ano": 1,
                                        "mês": 12, 
                                        "semana": 52.179, 
                                        "dia": 365.4, 
                                        "hora": 8766, 
                                        "minuto": 525960, 
                                        "segundo": 31557600}
            
            if unidade_de_tempo in unidades_disponiveis_tempo:
                taxa_de_rendimento_acumulada = (1 + self.get_taxa_de_rendimento()) ** (tempo / unidades_disponiveis_tempo[unidade_de_tempo])
                saldo_final = self.get_saldo() * taxa_de_rendimento_acumulada
                rendimento = saldo_final - self.get_saldo()
                print(f"O rendimento após {tempo} {unidade_de_tempo}(s) é de R${rendimento:.2f}. Saldo final: R${saldo_final:.2f}")
            else:
                print("Unidade de tempo inválida.")
        else:
            print("[ERRO 0] O valor inserido em 'tempo' é inválido. Tente Novamente.")
