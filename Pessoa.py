class Pessoa:
    
    def __init__(self, primeiro_nome, segundo_nome, conta, cpf, email):
        self.primeiro_nome = primeiro_nome
        self.segundo_nome = segundo_nome
        self.conta = conta
        self.cpf = cpf
        self.email = email
        self.total = 0
        self.extrato = []
        
    def deposito(self):
        while True:
            try:
                valor = float(input('Qual valor a ser depositado? '))
                if valor <= 0:
                    print('Apenas valores positivos e maiores que zero podem ser depositados! Tente novamente.')
                    continue        
                else:
                    self.total += valor
                    self.extrato.append(f'+{valor:.2f}')
                    print(f'Depósito realizado com sucesso!\nVocê depositou R$ {valor:.2f}')
                    break
                           
            except ValueError:
                print('Apenas valores numérios são aceitos, por favor, tente novamente!')
            except:
                print('Ocorreu um erro, tente novamente!')
                
    def saque(self):
        while True:
            try:
                valor = float(input('Qual valor você deseja sacar? '))
                if valor <= 0:
                    print('Apenas valores positivos e maiores que zero podem ser sacados! Tente novamente.')
                    continue
                elif valor > 500:
                    print('Valor excede o limite de R$ 500,00 por saque, tente novamente.')
                    continue
                elif valor > self.total:
                    print(f'Não foi possível realizar o saque por falta de saldo!\nSeu saldo é de R$ {self.total:.2f}')
                else:
                    self.total -= valor
                    self.extrato.append(f'-{valor:.2f}')
                    print(f'O valor foi sacado com sucesso! O saldo atual é de R$ {self.total:.2f}')
                    break
                    
            except ValueError:
                print('Apenas Valores numéricos são aceitos, por favor, tente novamente!')
            except:
                print('Ocorreu um erro, tente novamente!')
    
    def imprimirextrato(self):
        print('\nExtrato do dia x:\n')
        for transacao in self.extrato:
            print(f'R$ {transacao}')
        print(f'\nTotal: R$ {self.total:.2f}')
