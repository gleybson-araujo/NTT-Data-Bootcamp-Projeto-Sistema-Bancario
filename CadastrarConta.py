import re
import random
from Pessoa import Pessoa

lista_pessoas = []
class CadastrarConta:
    def __init__(self) -> None:
        pass
    
    def exibir_menu_cadastro(self):
        print('===================================')
        print('==    Boas vindas ao NTT Bank    ==')
        print('===================================')
        
    def cadastrar_nova_conta(self):
        while True:
            try:
                cpf = input('Digite o seu CPF: ')
                if not self.validar_cpf(cpf):
                    print("CPF inválido, tente novamente!")
                elif self.cpf_ja_existe(cpf):
                    print("Já existe uma conta vinculada a este CPF! Tente novamente.")
                else:
                    break
            except ValueError:
                print('Ocorreu um erro ao digitar seu CPF, tente novamente!')
        
        while True:
            try:
                primeiro_nome = input('\nDigite o seu primeiro nome: ')
                if not re.match("^[A-Za-z ]+$", primeiro_nome):
                    print('\nNome inválido, o nome só pode conter letras sem acentuação.')
                segundo_nome = input('\nDigite o seu sobrenome: ')
                if not re.match("^[A-Za-z ]+$", segundo_nome):
                    print('\nNome inválido, o nome só pode conter letras sem acentuação.')
                else:  
                    break
            except ValueError:
                print('Ocorreu um erro ao digitar seu nome, tente novamente!')
        
        while True:
            try:
                email = input('\nDigite o seu e-mail: ')
                if not re.match('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$', email):
                    print('\nEmail inválido, tente novamente!')
                elif self.email_ja_existe(email):
                    print('\nJá existe uma conta vinculada a este email! Tente novamente.')
                else:
                    confirmacao_email = input('\nDigite seu e-mail novamente: ')
                    if email != confirmacao_email:
                        print("\nE-mail não confere, tente novamente!")
                    else:
                        break
            except ValueError:
                print('Ocorreu um erro ao digitar seu e-mail, tente novamente!')
        conta = self.gerar_numero_conta_unico(cpf)
        nova_pessoa = Pessoa(primeiro_nome.upper(), segundo_nome.upper(), conta, cpf, email.upper())
        lista_pessoas.append(nova_pessoa)
        
        print(f'\nParabéns, {nova_pessoa.primeiro_nome.capitalize()}! Sua conta foi criada com sucesso!\nO número da sua conta é {conta}!')
        
        
    def validar_cpf(self, cpf):
        cpf = ''.join(filter(str.isdigit, cpf))
        
        if len(cpf) != 11:
            return False
        if cpf == cpf[0] * 11:
            return False
        
        soma = 0
        for i in range(9):
            soma += int(cpf[i]) * (10 - i)
            
        resto = soma % 11
        
        digito1 = 0 if resto < 2 else 11 - resto
        
        soma = 0
        for i in range(10):
            soma += int(cpf[i]) * (11 - i)
        
        resto = soma % 11
        digito2 = 0 if resto < 2 else 11 - resto        
        
        return digito1 == int(cpf[9]) and digito2 == int(cpf[10])
    
    def cpf_ja_existe(self, cpf):
        for pessoa in lista_pessoas:
            if pessoa.cpf == cpf:
                return True
        return False

    def email_ja_existe(self, email):
        for pessoa in lista_pessoas:
            if pessoa.email == email:
                return True
        return False
    
    #algoritmo para gerar um numero de conta único
    def gerar_numero_conta_unico(self, cpf):
        numero_conta = f"{cpf[7:11]}{random.randint(100000, 999999)}"
        return int(numero_conta)
    
oie = CadastrarConta()
oie.cadastrar_nova_conta()

print(lista_pessoas[0].cpf, lista_pessoas[0].primeiro_nome, lista_pessoas[0].segundo_nome, lista_pessoas[0].email)