# Sistema Bancário Orientado a Objetos

## Descrição breve
Este repositório contém a implementação de um sistema bancário orientado a objetos, onde os dados de clientes e contas bancárias são armazenados em objetos ao invés de dicionários, seguindo o modelo de classes UML.

## Descrição completa
Neste projeto, atualizamos a implementação de um sistema bancário simples para utilizar programação orientada a objetos. Os dados dos clientes e contas bancárias são armazenados em objetos, seguindo boas práticas de programação e um modelo de classes UML. O objetivo é melhorar a legibilidade, manutenção e eficiência do código.

### UML
A UML disponibilizada por Guilherme Carvalho (Python Consultant, Oak Solutions) para o desafio da DIO.

![47bd63b3-362c-45d7-9602-455d02942292-removebg-preview](https://github.com/lucenfort/sistema-bancario-oo/assets/55037889/b56cd548-752e-47c8-afe3-9d078cdd1a9e)


### Funcionalidades implementadas:
- **Criação de Usuários**: Cadastro de novos usuários com nome, CPF, data de nascimento e endereço.
- **Criação de Contas**: Criação de novas contas bancárias associadas a usuários existentes.
- **Depósitos**: Realização de depósitos em contas bancárias.
- **Saques**: Realização de saques com verificação de saldo, limite de saque e limite de saques diários.
- **Exibição de Extrato**: Exibição do extrato da conta com todas as transações realizadas.
- **Listagem de Contas**: Listagem de todas as contas bancárias cadastradas.
- **Menu Interativo**: Menu interativo para navegação pelas funcionalidades do sistema.

### Estrutura do código:
O código está organizado em três classes principais:
- `Usuario`: Representa um usuário do banco.
- `Conta`: Representa uma conta bancária.
- `Banco`: Gerencia as operações bancárias, como criar usuários, contas, realizar depósitos, saques, exibir extratos, e listar contas.

### Requisitos
- Python 3.x

### Como executar
Clone o repositório e execute o arquivo principal:
```bash
git clone https://github.com/seu-usuario/sistema-bancario-oo.git
cd sistema-bancario-oo
python main.py

