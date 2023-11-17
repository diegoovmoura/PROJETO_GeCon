import os
from time import sleep
import funcoes

os.system("cls")


def main():
    while(True):
        print(funcoes.LINES)
        print("Digite 1 - para fazer o login")
        print("Digite 2 - para fazer se registrar")
        print("Digite 3 - para cancelar")
        print(funcoes.LINES)
        flag = input()

 # ===================================ANALIZAR ESCOLHA=======================================
        if (flag == "1"):
            os.system("cls")
            flag2 = funcoes.login()
            if flag2[0] == True:
                break
            else:
                os.system("cls")
                print(f"{funcoes.font.FAIL}usuário ou senha invalidos{funcoes.font.NORMAL}")
        elif (flag == "2"):
            os.system("cls")
            funcoes.registrar()
            os.system("cls")
            print(f"{funcoes.font.OKGREEN}Usuário registrado com sucesso{funcoes.font.NORMAL}")
        elif (flag == "3"):
            print(f"{funcoes.font.OKBLUE}Programa Finalizado")
            return 0
        else:
            os.system("cls")
            print(f"{funcoes.font.FAIL}Valor inválido, Digite novamente{funcoes.font.NORMAL}")


    print(f"{funcoes.font.OKCYAN}Bem vindo(a) {flag2[1]}{funcoes.font.NORMAL}")
    sleep(1)
    os.system("cls")
    while(True):
        print(f"{funcoes.font.OKCYAN}Login como: {flag2[1]}{funcoes.font.NORMAL}")
        print(funcoes.LINES)
        print("Digite 1 - para fazer uma reserva da area de lazer")
        print("Digite 2 - para ver os status de manutenções")
        print("Digite 3 - para fazer um registro de melhoria")
        print("Digite 4 - para sair")
        print(funcoes.LINES)
        flag = input()
 #====================================ANALIZAR ESCOLHA=======================================
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
            print(f"{funcoes.font.FAIL}Valor inválido, Digite novamente{funcoes.font.NORMAL}")

    print(f"{funcoes.font.OKBLUE}Programa Finalizado")
    return 0

if __name__ == "__main__":
    main()