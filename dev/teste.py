import os

def texto(intrucoes:str):
    print("=======================================")
    print(intrucoes)
    print("=======================================")


def main():
    os.system("cls")
    while True:
        texto("Categorias para solicitação: \n1 - Manutenção\n2 - Segurança\n3 - Comportamento\n4 - Serviço")
        select_categoria=int(input("Favor, selecionar uma das categorias acima: "))

        if select_categoria == 1:
            solicitacao = input("Escreva o titulo da solicitação: ")

            print("Favor, preencher os campos!: ")
            natureza = input("Qual é a natureza do problema? (Exemplo: vazamento de água, infiltração, etc.): ")
            localizacao = input("Qual é a localização exata do problema que precisa de manutenção?: ")
            afetando_terceiros = input("O problema está afetando outras áreas ou unidades do condomínio?: ")

            with open(f"Manutenção_{solicitacao}", "w", encoding="utf-8") as file:
                file.write(f"natureza do problema: {natureza}\nlocalização exata do problema: {localizacao}\nO problema está afetando outras áreas: {afetando_terceiros}")

            status = input("Gostaria de verificar o status da manutençã?")
            if status.upper() == "S":
                with open(f"Manutenção_{solicitacao}", "r", encoding="utf-8") as file:
                    linhas = file.readlines()

                for linha in linhas:
                    print(linha, end="")

        elif select_categoria == 2:
            solicitacao = input("Escreva o titulo da solicitação: ")

            print("Favor, preencher os campos!: ")
            natureza = input("Qual é a natureza do problema? (Exemplo: vazamento de água, infiltração, etc.): ")
            localizacao = input("Qual é a localização exata do problema que precisa de manutenção?: ")
            afetando_terceiros = input("O problema está afetando outras áreas ou unidades do condomínio?: ")

            with open(f"Manutenção_{solicitacao}", "w", encoding="utf-8") as file:
                file.write(f"natureza do problema: {natureza}\nlocalização exata do problema: {localizacao}\nO problema está afetando outras áreas: {afetando_terceiros}")

            status = input("Gostaria de verificar o status da manutençã?")
            if status.upper() == "S":
                with open(f"Manutenção_{solicitacao}", "r", encoding="utf-8") as file:
                    linhas = file.readlines()

                for linha in linhas:
                    print(linha, end="")
        elif select_categoria == 3:
            solicitacao = input("Escreva o titulo da solicitação: ")

            print("Favor, preencher os campos!: ")
            natureza = input("Qual é a natureza do problema? (Exemplo: vazamento de água, infiltração, etc.): ")
            localizacao = input("Qual é a localização exata do problema que precisa de manutenção?: ")
            afetando_terceiros = input("O problema está afetando outras áreas ou unidades do condomínio?: ")

            with open(f"Manutenção_{solicitacao}", "w", encoding="utf-8") as file:
                file.write(f"natureza do problema: {natureza}\nlocalização exata do problema: {localizacao}\nO problema está afetando outras áreas: {afetando_terceiros}")

            status = input("Gostaria de verificar o status da manutençã?")
            if status.upper() == "S":
                with open(f"Manutenção_{solicitacao}", "r", encoding="utf-8") as file:
                    linhas = file.readlines()

                for linha in linhas:
                    print(linha, end="")
        elif select_categoria == 4:
            solicitacao = input("Escreva o titulo da solicitação: ")

            print("Favor, preencher os campos!: ")
            natureza = input("Qual é a natureza do problema? (Exemplo: vazamento de água, infiltração, etc.): ")
            localizacao = input("Qual é a localização exata do problema que precisa de manutenção?: ")
            afetando_terceiros = input("O problema está afetando outras áreas ou unidades do condomínio?: ")

            with open(f"Manutenção_{solicitacao}", "w", encoding="utf-8") as file:
                file.write(f"natureza do problema: {natureza}\nlocalização exata do problema: {localizacao}\nO problema está afetando outras áreas: {afetando_terceiros}")

            status = input("Gostaria de verificar o status da manutençã?")
            if status.upper() == "S":
                with open(f"Manutenção_{solicitacao}", "r", encoding="utf-8") as file:
                    linhas = file.readlines()

                for linha in linhas:
                    print(linha, end="")
        else:
            os.system("cls")
            print("comando invalido porra!")

if __name__ == "__main__":
    main()