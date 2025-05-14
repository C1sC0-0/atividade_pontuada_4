import os
import time
import csv
from dataclasses import dataclass

# Limpa a tela
os.system("cls || clear")

# Criando a classe Funcionario
@dataclass
class Funcionario:
    nome: str
    cargo: str
    salario: str

# Lista de funcionários
funcionarios = []

# Verifica se a lista está vazia
def verificar_lista_vazia(lista):
    if not lista:
        print("\nA lista está vazia.")
        return True
    return False

# Adicionar novo funcionário
def adicionar_funcionario(lista):
    nome = input("Digite o nome do funcionário: ")
    cargo = input("Digite o cargo do funcionário: ")
    salario = input("Digite o salário do funcionário: ")

    novo = Funcionario(nome, cargo, salario)
    lista.append(novo)

    print(f"\nFuncionário {nome} adicionado com sucesso.")

# Mostrar todos os funcionários
def mostrar_funcionarios(lista):
    if verificar_lista_vazia(lista):
        return

    print("\n- Lista de Funcionários -")
    for f in lista:
        print(f"- Nome: {f.nome} | Cargo: {f.cargo} | Salário: {f.salario}")

# Atualizar informações de um funcionário
def atualizar_funcionario(lista):
    if verificar_lista_vazia(lista):
        return

    nome_antigo = input("Digite o nome do funcionário que deseja atualizar: ")
    for f in lista:
        if f.nome == nome_antigo:
            novo_nome = input("Digite o novo nome: ")
            novo_cargo = input("Digite o novo cargo: ")
            novo_salario = input("Digite o novo salário: ")

            f.nome = novo_nome
            f.cargo = novo_cargo
            f.salario = novo_salario

            print(f"\nFuncionário {nome_antigo} foi atualizado com sucesso.")
            return

    print(f"\nFuncionário {nome_antigo} não encontrado.")

# Excluir funcionário
def excluir_funcionario(lista):
    if verificar_lista_vazia(lista):
        return

    nome_remover = input("Digite o nome do funcionário que deseja remover: ")
    for f in lista:
        if f.nome == nome_remover:
            lista.remove(f)
            print(f"\nFuncionário {nome_remover} foi removido com sucesso.")
            return

    print(f"\nFuncionário {nome_remover} não encontrado.")

# Salvar dados em CSV
def salvar_dados(lista):
    with open("funcionarios.csv", "w", newline="", encoding="utf-8") as arq:
        escritor = csv.writer(arq)
        escritor.writerow(["nome", "cargo", "salario"])  # Cabeçalho
        for f in lista:
            escritor.writerow([f.nome, f.cargo, f.salario])
    print("\nDados salvos com sucesso em 'funcionarios.csv'.")

# Carregar dados do CSV
def carregar_dados(lista):
    try:
        with open("funcionarios.csv", "r", encoding="utf-8") as arq:
            leitor = csv.reader(arq)
            next(leitor)  # pula cabeçalho
            for linha in leitor:
                nome, cargo, salario = linha
                lista.append(Funcionario(nome, cargo, salario))
        print("\nDados carregados com sucesso.")
    except FileNotFoundError:
        print("\nArquivo 'funcionarios.csv' não encontrado. Nenhum dado carregado.")

# Menu principal
while True:
    print("""
    - Gerenciador de Funcionários -
    1 - Adicionar Funcionário
    2 - Listar Funcionários
    3 - Atualizar Funcionário
    4 - Excluir Funcionário
    5 - Salvar Dados
    6 - Carregar Dados
    7 - Sair
    """)

    try:
        opcao = int(input("Digite uma das opções acima: "))
    except ValueError:
        print("\nDigite um número válido.")
        time.sleep(2)
        os.system("cls || clear")
        continue

    match opcao:
        case 1:
            adicionar_funcionario(funcionarios)
        case 2:
            mostrar_funcionarios(funcionarios)
        case 3:
            atualizar_funcionario(funcionarios)
        case 4:
            excluir_funcionario(funcionarios)
        case 5:
            salvar_dados(funcionarios)
        case 6:
            carregar_dados(funcionarios)
        case 7:
            print("\nSaindo do programa.")
            break
        case _:
            print("\nOpção inválida. Tente novamente.")

    if opcao != 1:
        time.sleep(10)
    os.system("cls || clear")