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
        print("Digite 4 - para consultar fluxo de caixa")
        print("Digite 5 - para sair")
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
        #=================CONSULTAR FLUXO DE CAIXA===========================
            print("Seja bem vindo ao sistema de consulta de fluxo de caixa do condomínio")
            lista_meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
            while True:
                while True:
                    try:
                        ano_atual_string = "2023"
                        ano_atual_inteiro = int(ano_atual_string)
                        ano_escolhido = int(input("Digite um ano entre 2020 e o ano atual para consultar: "))
                
                        if ano_escolhido >= 2020 and ano_escolhido <= ano_atual_inteiro:
                                break
                        else: 
                                print("Por favor, digite um ano entre 2020 e 2023!")
                
                    except ValueError:
                        print("Por favor, digite um número inteiro entre 2020 e 2023!")

                print("Escolha um mês: ")
                for i, mes in enumerate(lista_meses, start=1):
                    print("{}. {}".format(i, mes))
            
                while True:
                    try:
                        mes_escolhido= int(input("Escolha um número correspondente ao mês: "))
                        if mes_escolhido >=1 and mes_escolhido<=12:
                                break
                        else:
                                print("Digite um número válido, entre 1 e 12")
                    except ValueError:
                        print("Digite um número entre 1 e 12")

                receita1, despesa1 = funcoes.leitura_dados(ano_escolhido, mes_escolhido)
                saldo = receita1 - despesa1

                if receita1 is not None and despesa1 is not None:
                    print("\nO fluxo de caixa em {} de {} é: ".format(mes_escolhido, ano_escolhido))
                    print("Receita: R$ {}".format(receita1))
                    print("Despesa: R$ {}".format(despesa1))
                    print("Saldo do mês: R$ {}".format(saldo))

                else: 
                    print("Ainda não temos dados referentes ao mês e ano correspondentes!")     

                teste = int(input("\n1- Consultar outro ano/mês \n2 - voltar para menu principal\nO que você deseja fazer agora?  "))
                if(teste == 1):
                    continue
                else:
                    break
            continue
        elif (flag == "5"):
            break
        else:
            os.system("cls")
            print(f"{funcoes.font.FAIL}Valor inválido, Digite novamente{funcoes.font.NORMAL}")

    print(f"{funcoes.font.OKBLUE}Programa Finalizado")
    return 0

if __name__ == "__main__":
    main()