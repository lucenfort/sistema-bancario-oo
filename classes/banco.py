import textwrap
from classes.usuario import Usuario
from classes.conta import Conta
import re

class Banco:
    LIMITE_SAQUES = 3
    LIMITE_SAQUE_VALOR = 500

    def __init__(self):
        self.usuarios = []
        self.contas = []

    def menu(self):
        """
        Exibe o menu de opções e retorna a escolha do usuário.
        """
        menu = """\n
        ================ MENU ================
        [d]\tDepositar
        [s]\tSacar
        [e]\tExtrato
        [nc]\tNova conta
        [lc]\tListar contas
        [nu]\tNovo usuário
        [q]\tSair
        => """
        return input(textwrap.dedent(menu))

    def criar_usuario(self):
        """
        Cria um novo usuário no banco.
        """
        cpf = input("Informe o CPF (somente número): ")
        if not re.match(r"^\d{11}$", cpf):
            print("\n@@@ CPF inválido! @@@")
            return

        if self.filtrar_usuario(cpf):
            print("\n@@@ Já existe usuário com esse CPF! @@@")
            return

        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        self.usuarios.append(Usuario(nome, data_nascimento, cpf, endereco))
        print("=== Usuário criado com sucesso! ===")

    def filtrar_usuario(self, cpf):
        """
        Filtra e retorna um usuário pelo CPF.
        """
        return next((usuario for usuario in self.usuarios if usuario.cpf == cpf), None)

    def criar_conta(self):
        """
        Cria uma nova conta bancária para um usuário existente.
        """
        cpf = input("Informe o CPF do usuário: ")
        usuario = self.filtrar_usuario(cpf)

        if usuario:
            numero_conta = len(self.contas) + 1
            conta = Conta("0001", numero_conta, usuario)
            self.contas.append(conta)
            print("\n=== Conta criada com sucesso! ===")
        else:
            print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

    def listar_contas(self):
        """
        Lista todas as contas existentes no banco.
        """
        for conta in self.contas:
            linha = f"""\
                Agência:\t{conta.agencia}
                C/C:\t\t{conta.numero_conta}
                Titular:\t{conta.usuario.nome}
            """
            print("=" * 100)
            print(textwrap.dedent(linha))

    def depositar(self, conta):
        """
        Realiza um depósito na conta selecionada.
        """
        valor = self.validar_valor(input("Informe o valor do depósito: "))
        if valor:
            conta.saldo += valor
            conta.extrato += f"Depósito:\tR$ {valor:.2f}\n"
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    def sacar(self, conta):
        """
        Realiza um saque na conta selecionada, considerando limites e saldo.
        """
        valor = self.validar_valor(input("Informe o valor do saque: "))
        if valor:
            excedeu_saldo = valor > conta.saldo
            excedeu_limite = valor > Banco.LIMITE_SAQUE_VALOR
            excedeu_saques = conta.numero_saques >= Banco.LIMITE_SAQUES

            if excedeu_saldo:
                print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
            elif excedeu_limite:
                print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
            elif excedeu_saques:
                print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
            else:
                conta.saldo -= valor
                conta.extrato += f"Saque:\t\tR$ {valor:.2f}\n"
                conta.numero_saques += 1
                print("\n=== Saque realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    def exibir_extrato(self, conta):
        """
        Exibe o extrato da conta selecionada.
        """
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not conta.extrato else conta.extrato)
        print(f"\nSaldo:\t\tR$ {conta.saldo:.2f}")
        print("==========================================")

    def selecionar_conta(self):
        """
        Seleciona uma conta pelo número informado pelo usuário.
        """
        numero_conta = int(input("Informe o número da conta: "))
        for conta in self.contas:
            if conta.numero_conta == numero_conta:
                return conta
        print("\n@@@ Conta não encontrada! @@@")
        return None

    @staticmethod
    def validar_valor(valor_str):
        """
        Valida se a string informada é um valor monetário positivo.
        """
        try:
            valor = float(valor_str)
            if valor > 0:
                return valor
        except ValueError:
            pass
        return None

    def executar(self):
        """
        Método principal que executa o loop do menu de opções do banco.
        """
        acoes = {
            "d": self.acao_depositar,
            "s": self.acao_sacar,
            "e": self.acao_extrato,
            "nu": self.criar_usuario,
            "nc": self.criar_conta,
            "lc": self.listar_contas,
            "q": self.sair,
        }

        while True:
            opcao = self.menu()
            acao = acoes.get(opcao, self.acao_invalida)
            acao()

    def acao_depositar(self):
        """
        Ação de depósito, solicita a seleção de uma conta e realiza o depósito.
        """
        conta = self.selecionar_conta()
        if conta:
            self.depositar(conta)

    def acao_sacar(self):
        """
        Ação de saque, solicita a seleção de uma conta e realiza o saque.
        """
        conta = self.selecionar_conta()
        if conta:
            self.sacar(conta)

    def acao_extrato(self):
        """
        Ação de exibir extrato, solicita a seleção de uma conta e exibe o extrato.
        """
        conta = self.selecionar_conta()
        if conta:
            self.exibir_extrato(conta)

    def sair(self):
        """
        Ação de sair do sistema.
        """
        print("Saindo do sistema.")
        exit()

    def acao_invalida(self):
        """
        Ação para opção inválida do menu.
        """
        print("Operação inválida, por favor selecione novamente a operação desejada.")
