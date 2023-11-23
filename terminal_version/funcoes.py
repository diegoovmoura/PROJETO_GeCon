from time import sleep

path_to_registers = './Arquivos/registers.txt'
reserva = './Arquivos/reservas.txt'
melhorias = './Arquivos/melhorias/'
fluxo_caixa = './terminal_version/Arquivos/Fluxo_caixa_condominio.txt'
proj = './Arquivos/proj.txt'

LINES = "======================================="

class font:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    NORMAL = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def texto(intrucoes:str):
    print("=======================================")
    print(intrucoes)
    print("=======================================")

def login():
    texto("Digite seu usuário e senha")
    user = input(f"{font.WARNING}USUÁRIO:{font.NORMAL} ")
    passw = input(f"{font.WARNING}SENHA:{font.NORMAL} ")

    with open(path_to_registers, "r", encoding="utf-8") as file:
        linhas = file.readlines()

    for linha in linhas:
        linha = linha.replace("\n", "")
        aux = linha.split(";")
        if user == aux[0] and passw == aux[1]:
            return [True, user]
        
    return [False, user]

def registrar():
    with open(path_to_registers, 'a') as registers:
        texto("Digite seu usuário e senha")

        while(True):
            user = input(f"{font.WARNING}USUÁRIO:{font.NORMAL} ")
            passw = input(f"{font.WARNING}SENHA:{font.NORMAL} ")
            passw2 = input(f"{font.WARNING}CONFIRME SUA SENHA: {font.NORMAL}")

            if passw2 == passw:
                break
            else:
                print(f"{font.FAIL}Senhas incongruentes tente novamente{font.NORMAL}")

        registers.write(f"{user};{passw}\n")

# Consulta dos dados do fluxo de caixa
def leitura_dados(ano, mes):
    with open(fluxo_caixa, 'r') as arquivo1:
        for linha in arquivo1: 
            print(fluxo_caixa)
            partes = linha.strip().split(',')
            ano_arquivo = int(partes[0])
            mes_arquivo = int(partes[1])
            if ano_arquivo == ano and mes_arquivo == mes:
                receita = float(partes[2])
                despesa = float(partes[3])
                return receita, despesa
            
def ler_projeto(nome_arquivo):
    projetos = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            projetos.append(linha.strip().split(','))
    return projetos

def listar_nomes_obras(projetos):
    print("\nNomes das Obras:")
    for projeto in projetos:
        print(f"- {projeto[0]}")
    print()

def mostrar_status(projetos, nome_obra):
    for projeto in projetos:
        if projeto[0].lower() == nome_obra.lower():
            print("\nDetalhes da Obra:")
            print(f"Lugar: {projeto[0]}")
            print(f"Status: {projeto[1]}")
            print(f"Duração: {projeto[2]}")
            print(f"Motivo: {projeto[3]}\n")
            return
    print("Obra não encontrada.\n")

def fazer_reserva(area, nome, data):
    with open(f"{reserva}", "a", encoding="utf-8") as file:
        file.write(f"{area.capitalize()};{nome.capitalize()};{data}\n")

def mostrar_reservas():
    with open(f"{reserva}", "r", encoding="utf-8") as file:
        linhas  = file.readlines()

    print("Reservas feitas: ")
    for linha in linhas:
        linha = linha.replace("\n", "")
        aux = linha.split(";")
        print(f"Area: {aux[0]} \nFeita por: {aux[1]} \nData: {aux[2]}")
        print()

    continuar = input("pressione enter para continuar: ")

def remover_reserva():

    nome = input("Digite o nome registrado da reserva: ").capitalize()
    area = input("Digite a area em que deseja cancelar: ").capitalize()

    with open(f"{reserva}", "r", encoding="utf-8") as file:
        linhas  = file.readlines()

    with open(f"{reserva}", "w", encoding="utf-8") as file:
        for linha in linhas:
            aux = linha.replace("\n", "")
            aux = aux.split(";")

            if nome != aux[1] and area != aux[0]:
                file.write(linha)
    
    print("Reserva removida com sucesso!")
    continuar = input("pressione enter para continuar: ")


def editar_solicitacao():
    titulo = input("Titulo da solicitação a ser editada: ")

    perguntas = []
    with open(f"{melhorias}Manutenção_{titulo}.txt", "r", encoding="utf-8") as file:
        linhas = file.readlines()

    for i in range(len(linhas)):
        aux = linhas[i].split(":")
        perguntas.append(aux[0])

    qsv1_ed=input(f"{perguntas[0]}: ")
    qsv2_ed=input(f"{perguntas[1]}: ")
    qsv3_ed=input(f"{perguntas[2]}: ")
    data = [qsv1_ed, qsv2_ed, qsv3_ed]


    with open(f"{melhorias}Manutenção_{titulo}.txt", "w", encoding="utf-8") as file:
        for i in range(len(linhas)):
            aux = linhas[i].split(":")
            file.write(f"{aux[0]}: {data[i]}\n")

    print("Solicitação alterada com sucesso!")
    continuar = input("pressione enter para continuar: ")