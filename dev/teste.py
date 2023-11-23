import os

def texto(intrucoes:str):
    print("=======================================")
    print(intrucoes)
    print("=======================================")


def main():
    os.system("cls")
    while True:
        texto("Categorias para solicitação: \n1 - Manutenção\n2 - Segurança\n3 - Comportamento\n4 - Serviço\n5 - Voltar para o menu")
        select_categoria=int(input("Favor, selecionar uma das categorias acima: "))

        if select_categoria == 1:
            solicitacao = input("Escreva o titulo da solicitação: ")

            pergunta_1 = input("Qual é a natureza do problema? (Exemplo: vazamento de água, infiltração, etc.): ")
            pergunta_2 = input("Qual é a localização exata do problema que precisa de manutenção?: ")
            pergunta_3 = input("O problema está afetando outras áreas ou unidades do condomínio?: ")

            with open(f"Manutenção_{solicitacao}", "w", encoding="utf-8") as file:
                file.write(f"natureza do problema: {pergunta_1}\nlocalização exata do problema: {pergunta_2}\nO problema está afetando outras áreas: {pergunta_3}\n")

            status = input("Gostaria de verificar o status da manutenção?\nS - sim\nN - não: ")
            if status.upper() == "S":
                with open(f"Manutenção_{solicitacao}", "r", encoding="utf-8") as file:
                    linhas = file.readlines()

                for linha in linhas:
                    print(linha, end="")

        elif select_categoria == 2:
            solicitacao = input("Escreva o titulo da solicitação: ")

            pergunta_1=input("Qualquer a sugestão ou preocupação específica que você gostaria de compartilhar em relação à segurança do condomínio?")
            pergunta_2=input("Você já identificou algum incidente recente que tenha levantado preocupações de segurança no condomínio?")
            pergunta_3=input("Quais são as áreas específicas do condomínio que você acredita precisarem de melhorias na segurança?")

            with open(f"Manutenção_{solicitacao}", "w", encoding="utf-8") as file:
                file.write(f"sugestão ou preocupação específica: {pergunta_1}\njá identificou algum incidente?: {pergunta_2}\nQuais são as áreas específicas do condomínio: {pergunta_3}\n")

            status = input("Gostaria de verificar o status da manutenção?\nS - sim\nN - não: ")
            if status.upper() == "S":
                with open(f"Manutenção_{solicitacao}", "r", encoding="utf-8") as file:
                    linhas = file.readlines()

                for linha in linhas:
                    print(linha, end="")

        elif select_categoria == 3:
            solicitacao = input("Escreva o titulo da solicitação: ")

            pergunta_1=input("Houve alguma situação específica recentemente que chamou a sua atenção em relação ao comportamento dos moradores?")
            pergunta_2=input("Existem áreas comuns onde o comportamento dos moradores é mais problemático? Se sim, quais áreas?")
            pergunta_3=input("Existe alguma observação ou preocupação adicional que você gostaria de compartilhar em relação ao comportamento no condomínio?")

            with open(f"Manutenção_{solicitacao}", "w", encoding="utf-8") as file:
                file.write(f"Houve alguma situação específica?: {pergunta_1}\nLocais propensos: {pergunta_2}\nObservação ou preocupação adicional: {pergunta_3}\n")

            status = input("Gostaria de verificar o status da manutenção?\nS - sim\nN - não: ")
            if status.upper() == "S":
                with open(f"Manutenção_{solicitacao}", "r", encoding="utf-8") as file:
                    linhas = file.readlines()

                for linha in linhas:
                    print(linha, end="")

        elif select_categoria == 4:
            solicitacao = input("Escreva o titulo da solicitação: ")

            pergunta_1 = input("Qual é o tipo de serviço que você está solicitando para o condomínio?")
            pergunta_2 = input("Qual é a localização exata do serviço que precisa ser realizado?")
            pergunta_3 = input("Descreva em detalhes o problema ou a necessidade que justifica a solicitação deste serviço") 

            with open(f"Manutenção_{solicitacao}", "w", encoding="utf-8") as file:
                file.write(f"Tipo de serviço: {pergunta_1}\nLocalização exata do serviço: {pergunta_2}\nDescrição do problema: {pergunta_3}\n")

            status = input("Gostaria de verificar o status da manutenção?\nS - sim\nN - não: ")
            if status.upper() == "S":
                print()
                with open(f"Manutenção_{solicitacao}", "r", encoding="utf-8") as file:
                    linhas = file.readlines()

                for linha in linhas:
                    print(linha, end="")

        elif select_categoria == 5:
            break

        else:
            os.system("cls")
            print("comando invalido!")

if __name__ == "__main__":
    main()