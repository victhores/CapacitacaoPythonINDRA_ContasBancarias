from Conta import Conta

class ContaPoupanca(Conta):
    clientes_conta_poupanca: list[dict[str, object]] = [] # lista contendo os dados de todos os clientes de conta poupança do banco
    lista_id_clientes_de_conta_poupanca = [] # lista responsável por guardar os IDs existentes em contas poupança


    def __init__(self, id_cliente: str, saldo: str, taxa_de_rendimento: float):
        super().__init__(id_cliente, saldo)
        if id_cliente not in self.lista_id_clientes_de_conta_poupanca:
            # verifica se o ID inserido para o novo cliente já não existe, e adiciona-o à lista caso seja um valor inédito
                # caso o cliente já exista, retorna mensagem informando o erro e continua a leitura do código, sem adicionar o referido cliente ao banco 
            
            self.lista_id_clientes_de_conta_poupanca.append(id_cliente)
            
            if saldo >= 0:
                # verifica se o saldo inserido para o novo cliente não é negativo, e adiciona-o à conta caso retorne True
                    # caso o saldo inicial seja negativo, retorna mensagem informando o erro e continua a leitura do código, sem adicionar o referido cliente ao banco 
                
                if taxa_de_rendimento >= 0:
                    # realiza a mesma verificação anterior, mas agora sobre a taxa de rendimento da conta poupança
                    # a taxa de rendimento é um valor em porcentagem ao ano, que diz respeito a quanto o montante inicial renderá após certo tempo
                        
                        self.taxa_de_rendimento = taxa_de_rendimento / 100
                            # tendo em vista que a taxa de rendimento é um valor que deve ser multiplicado pelo montante para resultar no lucro,
                            # aqui é feita a divisão da mesma por 100, para que seja a operação possa ser feita corretamente

                        self.clientes_conta_poupanca.append({"ID do cliente": "CP" + self.id_cliente, # identificação do cliente
                                                            "Tipo de conta": "Conta Poupança", # tipo de conta
                                                            "Saldo Atual": self.saldo}) # saldo inicial
                else:
                    raise ValueError("[ERRO 05] O valor inserido em 'taxa_de_rendimento' é inválido. Tente Novamente.")
                        # erro caso a taxa de rendimento < 0
            else:
                raise ValueError("[ERRO 01] O valor inserido em 'saldo' é inválido. Tente Novamente.")
                    # erro caso saldo < 0
        else:
            raise ValueError("[ERRO 00] O valor inserido em 'id_cliente' já está em uso. Tente outro ID.")
                # erro caso já exista um cliente com o mesmo ID no banco.


    def get_id_cliente(self):
        return "CP" + self.id_cliente
            # getter do ID do cliente

    def get_saldo(self):
        return self.saldo
            # getter do saldo atual do cliente


    def set_saldo(self, novo_saldo):
        self.saldo = novo_saldo
        for cliente in self.clientes_conta_poupanca:
            if cliente["ID do cliente"] == self.get_id_cliente():
                cliente["Saldo Atual"] = self.saldo
                return self.saldo
        # setter do saldo do cliente, tanto na lista de clientes de conta poupança quanto no atributo do mesmo
        # realiza uma varredura na lista de clientes e, através do ID do cliente, localiza a chave de "Saldo Atual", modificando o seu valor


    def get_taxa_de_rendimento(self):
        return self.taxa_de_rendimento
            # getter do limite de cheque especial do cliente


    def depositar_dinheiro(self, valor_do_deposito: float):
        if valor_do_deposito >= 0:
            # verifica se o valor do depósito não é negativo e realiza a operação caso retorne True
                # caso o valor do depósito seja negativo, retorna mensagem informando o erro e continua a leitura do código, sem realizar a operação 

            self.set_saldo(self.get_saldo() + valor_do_deposito)
                # atualiza o saldo, somando-o com o valor informado como valor do depósito

        else:
            raise ValueError("[ERRO 02] O valor inserido em 'valor_do_deposito' é inválido. Tente Novamente.")
                # erro caso valor do depósito < 0


    def sacar_dinheiro(self, valor_do_saque: float):
        if valor_do_saque >= 0:
            # verifica se o valor do saque não é negativo e realiza a operação caso retorne True
                # caso o valor do saque seja negativo, retorna mensagem informando o erro e continua a leitura do código, sem realizar a operação 

            limite_para_saque = self.get_saldo()
                # variável responsável por estabelecer um limite de saque. no caso, o próprio saldo
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
            raise ValueError("[ERRO 03] O valor inserido em 'valor_do_saque' é inválido. Tente Novamente.")
                # erro caso valor do saque < 0


    def verificar_rendimento_no_tempo_determinado(self, tempo: int, unidade_de_tempo: str):
        if tempo >= 0:
            # verifica se o atributo tempo não é negativo e realiza a operação caso retorne True
                # caso tempo seja negativo, retorna mensagem informando o erro e continua a leitura do código, sem realizar a operação 
    
            unidades_de_tempo_disponiveis = {"ano": 1,
                                             "mês": 12,
                                             "semana": 52.179,
                                             "dia": 365.4,
                                             "hora": 8766,
                                             "minuto": 525960,
                                             "segundo": 31557600}
                # o dicionário acima é responsável por conter as unidades de tempo disponíveis para conversão, bem como as bases
                # utilizadas para calcular a taxa equivalente
            
            if unidade_de_tempo in unidades_de_tempo_disponiveis:
                # verifica se a unidade de tempo informada é válida e realiza a operação caso retorne True
                    # caso a unidade de tempo não esteja em 'unidades_de_tempo_disponiveis', retorna mensagem informando o erro 
                    # e continua a leitura do código, sem realizar a operação 

                taxa_equivalente = (1 + self.get_taxa_de_rendimento()) ** (tempo / unidades_de_tempo_disponiveis[unidade_de_tempo])
                    # realiza o cálculo da taxa equivalente, com base no tempo e na unidade de medida informados ao chamar o método

                saldo_final = self.get_saldo() * taxa_equivalente
                    # realiza o cálculo do montante final de acordo com as características do investimento e o montante inicial

                rendimento = saldo_final - self.get_saldo()
                    # calcula o rendimento total do investimento com base no saldo final e o inicial

                print(f"Seu saldo atual é de R${self.get_saldo():.2f}")
                print(f"O rendimento após {tempo} {unidade_de_tempo}(s) é de R${rendimento:.6f}. Saldo final: R${saldo_final:.2f}")
                aplicar = input("Deseja aplicar o seu dinheiro nesse investimento? S/N\n")
                aplicar.casefold()
                    # permite que o usuário escolha se aplicará o dinheiro nesse investimento

                tupla_aceitar_aplicacao_no_investimento = ("sim", "s")
                if aplicar in tupla_aceitar_aplicacao_no_investimento:
                    # verifica se a entrada recebida pelo terminal confirma o depósito, e atualiza o valor caso retorne True

                    self.set_saldo(saldo_final)
                    print(f"Dinheiro aplicado. Saldo atual: R${self.get_saldo():.2f}")
                else:
                    print(f"Dinheiro não aplicado. Saldo atual: R${self.get_saldo():.2f}")

            else:
                print("[ERRO 07] Unidade de tempo inválida. Tente Novamente.")
                    # erro caso unidade de tempo não esteja em 'unidades_de_tempo_disponiveis'
        
        else:
            print("[ERRO 06] O valor inserido em 'tempo' é inválido. Tente Novamente.")
                # erro caso tempo < 0


victor = ContaPoupanca(id_cliente="1", saldo=1000, taxa_de_rendimento=5)

victor.depositar_dinheiro(valor_do_deposito=200)

victor.sacar_dinheiro(valor_do_saque=6000)

victor.verificar_rendimento_no_tempo_determinado(tempo=23, unidade_de_tempo="ano")