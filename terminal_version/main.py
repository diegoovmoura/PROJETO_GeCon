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
        os.system("cls")
        print(f"{funcoes.font.OKCYAN}Login como: {flag2[1]}{funcoes.font.NORMAL}")
        print(funcoes.LINES)
        print("Digite 1 - para fazer ou cancelar uma reserva da area de lazer")
        print("Digite 2 - para ver os status de manutenções")
        print("Digite 3 - para fazer um registro de melhoria")
        print("Digite 4 - para consultar fluxo de caixa")
        print("Digite 5 - para sair")
        print(funcoes.LINES)
        flag = input()
#===================================================FAZER RESERVA=============================================
        if (flag == "1"):
            while True:
                os.system("cls")
                funcoes.texto("1 - Fazer reserva\n2 - Mostrar reservas\n3 - Cancelar uma reserva\n4 - Sair")

                escolha = input("Escolha uma opção (1/2/3/4): ")

                if escolha == "1":
                    area = input("Digite a area da reserva (Piscina/Churrasqueira/PlayGround): ")
                    nome = input("Digite o nome para a reserva: ")
                    data = input("Digite a data da reserva: ")
                    funcoes.fazer_reserva(area, nome, data)

                elif escolha == "2":
                    funcoes.mostrar_reservas()

                elif escolha == "3":
                    funcoes.remover_reserva()

                elif escolha == "4":
                    print("Saindo do sistema de reservas. Até mais!")
                    break

                else:
                    print("Opção inválida. Tente novamente.")
#=========================================CONSULTAR STATUS DE MANUTENÇÃO===========================================
        elif (flag == "2"):
            projetos = funcoes.ler_projeto(funcoes.proj)
            funcoes.listar_nomes_obras(projetos)
            while True:
                escolha = input("Digite o nome da obra para ver os detalhes ou 'sair' para encerrar: ").lower()
                if escolha == 'sair':
                    break
                funcoes.mostrar_status(projetos, escolha)

#=========================================FAZER REGISTRO DE MELHORIAS=====================================================
        elif (flag == "3"):
            while True:
                os.system("cls")
                funcoes.texto("Categorias para solicitação: \n1 - Manutenção\n2 - Segurança\n3 - Comportamento\n4 - Serviço\n5 - para editar solicitação\n6 - Voltar para o menu")
                select_categoria=int(input("Favor, selecionar uma das categorias acima: "))

                if select_categoria == 1:
                    solicitacao = input("Escreva o titulo da solicitação: ")
                    pergunta_1 = input("Qual é a natureza do problema? (Exemplo: vazamento de água, infiltração, etc.): ")
                    pergunta_2 = input("Qual é a localização exata do problema que precisa de manutenção?: ")
                    pergunta_3 = input("O problema está afetando outras áreas ou unidades do condomínio?: ")

                    with open(f"{funcoes.melhorias}Manutenção_{solicitacao}.txt", "w", encoding="utf-8") as file:
                        file.write(f"natureza do problema: {pergunta_1}\nlocalização exata do problema: {pergunta_2}\nO problema está afetando outras áreas: {pergunta_3}\n")

                    status = input("Gostaria de verificar o status da manutenção?\nS - sim\nN - não: ")
                    if status.upper() == "S":
                        with open(f"{funcoes.melhorias}Manutenção_{solicitacao}.txt", "r", encoding="utf-8") as file:
                            linhas = file.readlines()

                        for linha in linhas:
                            print(linha, end="")

                elif select_categoria == 2:
                    solicitacao = input("Escreva o titulo da solicitação: ")

                    pergunta_1=input("Qualquer a sugestão ou preocupação específica que você gostaria de compartilhar em relação à segurança do condomínio?")
                    pergunta_2=input("Você já identificou algum incidente recente que tenha levantado preocupações de segurança no condomínio?")
                    pergunta_3=input("Quais são as áreas específicas do condomínio que você acredita precisarem de melhorias na segurança?")

                    with open(f"{funcoes.melhorias}Manutenção_{solicitacao}.txt", "w", encoding="utf-8") as file:
                        file.write(f"sugestão ou preocupação específica: {pergunta_1}\njá identificou algum incidente?: {pergunta_2}\nQuais são as áreas específicas do condomínio: {pergunta_3}\n")

                    status = input("Gostaria de verificar o status da manutenção?\nS - sim\nN - não: ")
                    if status.upper() == "S":
                        with open(f"{funcoes.melhorias}Manutenção_{solicitacao}.txt", "r", encoding="utf-8") as file:
                            linhas = file.readlines()

                        for linha in linhas:
                            print(linha, end="")

                elif select_categoria == 3:
                    solicitacao = input("Escreva o titulo da solicitação: ")

                    pergunta_1=input("Houve alguma situação específica recentemente que chamou a sua atenção em relação ao comportamento dos moradores?")
                    pergunta_2=input("Existem áreas comuns onde o comportamento dos moradores é mais problemático? Se sim, quais áreas?")
                    pergunta_3=input("Existe alguma observação ou preocupação adicional que você gostaria de compartilhar em relação ao comportamento no condomínio?")

                    with open(f"{funcoes.melhorias}Manutenção_{solicitacao}.txt", "w", encoding="utf-8") as file:
                        file.write(f"Houve alguma situação específica?: {pergunta_1}\nLocais propensos: {pergunta_2}\nObservação ou preocupação adicional: {pergunta_3}\n")

                    status = input("Gostaria de verificar o status da manutenção?\nS - sim\nN - não: ")
                    if status.upper() == "S":
                        with open(f"{funcoes.melhorias}Manutenção_{solicitacao}.txt", "r", encoding="utf-8") as file:
                            linhas = file.readlines()

                        for linha in linhas:
                            print(linha, end="")

                elif select_categoria == 4:
                    solicitacao = input("Escreva o titulo da solicitação: ")

                    pergunta_1 = input("Qual é o tipo de serviço que você está solicitando para o condomínio?")
                    pergunta_2 = input("Qual é a localização exata do serviço que precisa ser realizado?")
                    pergunta_3 = input("Descreva em detalhes o problema ou a necessidade que justifica a solicitação deste serviço") 

                    with open(f"{funcoes.melhorias}Manutenção_{solicitacao}.txt", "w", encoding="utf-8") as file:
                        file.write(f"Tipo de serviço: {pergunta_1}\nLocalização exata do serviço: {pergunta_2}\nDescrição do problema: {pergunta_3}\n")

                    status = input("Gostaria de verificar o status da manutenção?\nS - sim\nN - não: ")
                    if status.upper() == "S":
                        print()
                        with open(f"{funcoes.melhorias}Manutenção_{solicitacao}.txt", "r", encoding="utf-8") as file:
                            linhas = file.readlines()

                        for linha in linhas:
                            print(linha, end="")

                elif select_categoria == 5:
                    funcoes.editar_solicitacao()

                elif select_categoria == 6:
                    break

                else:
                    os.system("cls")
                    print("comando invalido!")
#=========================================CONSULTAR FLUXO DE CAIXA=====================================================
        elif (flag == "4"):
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