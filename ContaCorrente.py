from Conta import Conta
class ContaCorrente(Conta):
    clientes_conta_corrente: list[dict[str, object]] = [] # lista contendo os dados de todos os clientes de conta corrente do banco
    lista_id_clientes_de_conta_corrente = [] # lista responsável por guardar os IDs existentes em contas correntes

    def __init__(self, id_cliente: str, saldo: float, limite_cheque_especial: float):
        super().__init__(id_cliente, saldo) 
        if id_cliente not in self.lista_id_clientes_de_conta_corrente:
            # verifica se o ID inserido para o novo cliente já não existe, e adiciona-o à lista caso seja um valor inédito
                # caso o cliente já exista, retorna mensagem informando o erro e continua a leitura do código, sem adicionar o referido cliente ao banco 
            
            self.lista_id_clientes_de_conta_corrente.append(id_cliente)
            
            if saldo >= 0:
                # verifica se o saldo inserido para o novo cliente não é negativo, e adiciona-o à conta caso retorne True
                    # caso o saldo inicial seja negativo, retorna mensagem informando o erro e continua a leitura do código, sem adicionar o referido cliente ao banco 
                
                if limite_cheque_especial >= 0: 
                    # realiza a mesma verificação anterior, mas agora sobre o limite de cheque especial
                    # o limite de cheque especial é um valor "bônus" cedido pelo banco, e pode ser utilizado em operações de saque
                    
                    self.limite_cheque_especial = limite_cheque_especial
                    self.clientes_conta_corrente.append({"ID do cliente": "CC" + self.id_cliente, # identificação do cliente
                                                        "Tipo de conta": "Conta Corrente", # tipo de conta
                                                        "Saldo Atual": self.saldo, # saldo inicial
                                                        "Limite de Cheque Especial": self.limite_cheque_especial}) # limite de cheque especial
                else:
                    raise ValueError("[ERRO 05] O valor inserido em 'limite_cheque_especial' é inválido. Tente Novamente.")
                        # erro caso limite de cheque especial < 0
            
            else:
                raise ValueError("[ERRO 01] O valor inserido em 'saldo' é inválido. Tente Novamente.")
                    # erro caso saldo < 0
        
        else:
            raise ValueError("[ERRO 00] O valor inserido em 'id_cliente' já está em uso. Tente outro ID.")
                # erro caso já exista um cliente com o mesmo ID no banco.
        

    def get_id_cliente(self):
        return "CC" + self.id_cliente
            # getter do ID do cliente


    def get_saldo(self):
        return self.saldo
            # getter do saldo atual do cliente


    def set_saldo(self, novo_saldo):
        self.saldo = novo_saldo
        for cliente in self.clientes_conta_corrente:
            if cliente["ID do cliente"] == self.get_id_cliente():
                cliente["Saldo Atual"] = self.saldo
                return self.saldo
        # setter do saldo do cliente, tanto na lista de clientes de conta corrente quanto no atributo do mesmo
        # realiza uma varredura na lista de clientes e, através do ID do cliente, localiza a chave de "Saldo Atual", modificando o seu valor
            

    def get_limite_de_cheque_especial(self):
        return self.limite_cheque_especial  
            # getter do limite de cheque especial do cliente              


    def depositar_dinheiro(self, valor_do_deposito: float):
        if valor_do_deposito >= 0:
            # verifica se o valor do depósito não é negativo e realiza a operação caso retorne True
                # caso o valor do depósito seja negativo, retorna mensagem informando o erro e continua a leitura do código, sem realizar a operação 
            
            self.set_saldo(self.get_saldo() + valor_do_deposito)
                # atualiza o saldo, somando-o com o valor informado como valor do depósito
        
        else:
            print("[ERRO 02] O valor inserido em 'valor_do_deposito' é inválido. Tente Novamente.")
                # erro caso valor do depósito < 0


    def sacar_dinheiro(self, valor_do_saque: float):
        if valor_do_saque >= 0:
            # verifica se o valor do saque não é negativo e realiza a operação caso retorne True
                # caso o valor do saque seja negativo, retorna mensagem informando o erro e continua a leitura do código, sem realizar a operação 
            
            limite_para_saque = self.get_saldo() + self.get_limite_de_cheque_especial()
                # variável responsável por estabelecer um limite de saque
                    # não é possível realizar o saque caso o valor do saque seja maior do que o montante disponível na conta
            
            if limite_para_saque >= valor_do_saque:
                # verifica se o valor disponível em conta permite que seja realizado um saque no valor especificado
                    # se permitir, realiza o saque e atualiza o saldo em conta, descontando o valor sacado
                    # se não permitir, retorna mensagem informando o erro e continua a leitura do código, sem realizar a operação 
                
                self.set_saldo(self.get_saldo() - valor_do_saque)
            else:
                print(f"[ERRO 04] Saldo insuficiente. Tente sacar um valor menor do que R${limite_para_saque:.2f}")
                    # erro caso o saldo disponível para saque seja menor do que o valor solicitado
        
        else:
            print("[ERRO 03] O valor inserido em 'valor_do_saque' é inválido. Tente Novamente.")
                # erro caso valor do saque < 0

