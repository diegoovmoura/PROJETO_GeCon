from tqdm import tqdm
from time import sleep


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

def login():
    print(LINES)
    print("Digite seu usuario e senha")
    print(LINES)
    user = input(f"{font.WARNING}USUÁRIO:{font.NORMAL} ")
    passw = input(f"{font.WARNING}SENHA:{font.NORMAL} ")

    if user in registros:
        if registros[user] == passw:
            for i in tqdm(range(100)):
                sleep(0.005)
            return [True, user]
        else:
            return [False, user]
    else:
        return [False, user]

def registrar():
    print(LINES)
    print("Informe seu usuario e sua senha")
    print(LINES)

    while(True):
        user = input(f"{font.WARNING}USUÁRIO:{font.NORMAL} ")
        passw = input(f"{font.WARNING}SENHA:{font.NORMAL} ")
        passw2 = input(f"{font.WARNING}CONFIRME SUA SENHA: {font.NORMAL}")

        if passw2 == passw:
            break
        else:
            print(f"{font.FAIL}Senhas incongruentes tente novamente{font.NORMAL}")

    for i in tqdm(range(100)):
        sleep(0.01)
    registros[user] = passw