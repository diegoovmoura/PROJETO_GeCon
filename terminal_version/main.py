import os
from time import sleep
import lib

os.system("cls")


def main():
    while(True):
        print(lib.LINES)
        print("Digite 1 - para fazer o login")
        print("Digite 2 - para fazer se registrar")
        print("Digite 3 - para cancelar")
        print(lib.LINES)
        flag = input()

 # ===================================ANALIZAR ESCOLHA=======================================
        if (flag == "1"):
            os.system("cls")
            flag2 = lib.login()
            if flag2[0] == True:
                break
            else:
                os.system("cls")
                print(f"{lib.font.FAIL}usuário ou senha invalidos{lib.font.NORMAL}")
        elif (flag == "2"):
            os.system("cls")
            lib.registrar()
            os.system("cls")
            print(f"{lib.font.OKGREEN}Usuário registrado com sucesso{lib.font.NORMAL}")
        elif (flag == "3"):
            print(f"{lib.font.OKBLUE}Programa Finalizado")
            return 0
        else:
            os.system("cls")
            print(f"{lib.font.FAIL}Valor inválido, Digite novamente{lib.font.NORMAL}")


    print(f"{lib.font.OKCYAN}Bem vindo(a) {flag2[1]}{lib.font.NORMAL}")
    sleep(1)
    os.system("cls")
    while(True):
        print(f"{lib.font.OKCYAN}Login como: {flag2[1]}{lib.font.NORMAL}")
        print(lib.LINES)
        print("Digite 1 - para fazer uma reserva da area de lazer")
        print("Digite 2 - para ver os status de manutenções")
        print("Digite 3 - para fazer um registro de melhoria")
        print("Digite 4 - para sair")
        print(lib.LINES)
        flag = input()
 # ===================================ANALIZAR ESCOLHA=======================================
        if (flag == "1"):
            break
        elif (flag == "2"):
            break
        elif (flag == "3"):
            break
        elif (flag == "4"):
            break
        else:
            os.system("cls")
            print(f"{lib.font.FAIL}Valor inválido, Digite novamente{lib.font.NORMAL}")

    print(f"{lib.font.OKBLUE}Programa Finalizado")
    return 0

if __name__ == "__main__":
    main()