from time import sleep

path_to_registers = './Arquivos/registers.txt'
fluxo_caixa = './terminal_version/Arquivos/Fluxo_caixa_condominio.txt'

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

registros = {"diego": "123",
             "hugo": "333",
             "renato": "123"
             }


def texto(intrucoes:str):
    print("=======================================")
    print(intrucoes)
    print("=======================================")

def login():
    texto("Digite seu usuário e senha")
    user = input(f"{font.WARNING}USUÁRIO:{font.NORMAL} ")
    passw = input(f"{font.WARNING}SENHA:{font.NORMAL} ")

    if user in registros:
        if registros[user] == passw:
            return [True, user]
        else:
            return [False, user]
    else:
        return [False, user]

def registrar():
    registers = open(path_to_registers, 'a')
    texto("Digite seu usuário e senha")

    while(True):
        user = input(f"{font.WARNING}USUÁRIO:{font.NORMAL} ")
        passw = input(f"{font.WARNING}SENHA:{font.NORMAL} ")
        passw2 = input(f"{font.WARNING}CONFIRME SUA SENHA: {font.NORMAL}")

        if passw2 == passw:
            break
        else:
            print(f"{font.FAIL}Senhas incongruentes tente novamente{font.NORMAL}")

    registros[user] = passw
    registers.write(user + ' ' + passw + '\n')
    registers.close()

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