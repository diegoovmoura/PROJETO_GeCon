# FUNÇÕES DE 1.REGISTRAR OS DADOS DA SOLCITIAÇÃO E 2. EXIBIR NA TELA A SOLICITAÇÃO(MANUTENÇÃO)
def status_manutencao(banco_manutencao,titulo1):  
        manutencoes=open(f'manutenção_{titulo1}.txt', 'x',encoding="utf-8")  

        for e in banco_manutencao:
            manutencoes.write(e+banco_manutencao[e]+'\n')      
        manutencoes.close()  



def exibir_status_mauntencao(banco_manutencao):
  print("Exibindo..")
  for e in banco_manutencao:
    print(e+banco_manutencao[e]) 

  pergunta_alterar=input("Pressione qualquer tecla para avançar ")
  
  while (pergunta_alterar!="S" or pergunta_alterar!="s") or (pergunta_alterar!="n" or pergunta_alterar!="N"): 
            pergunta_alterar=input("Gostaria de editar algo de sua solicitação? ") 
            if (pergunta_alterar=="N" or pergunta_alterar=="n"):
                print("Processo finalizado!")
                break
            elif (pergunta_alterar=="S" or pergunta_alterar=="s"):    
                titulo1=input("Digite o nome da solicitação que você quer ajustar")
                editar_status_manutencao(banco_manutencao,titulo1)
                break 
            else:
                print("Favor, responder S ou N")



def editar_status_manutencao(banco_manutencao,titulo1):
     qm1_ed=input("Alterar tipo de problema para: ")
     qm2_ed=input("Alterar local para: ")
     qm3_ed=input("O problema está afetando outras áreas? ")

     banco_manutencao={"Tipo de problema: ":qm1_ed,"Local: ":qm2_ed,"Está afetando outras áreas?: ":qm3_ed} 
     manutencoes_edit=open(f'manutenção_{titulo1}.txt', 'w',encoding="utf-8")
     for e in banco_manutencao:   
        manutencoes_edit.write(e+banco_manutencao[e]+'\n')  
     manutencoes_edit.close() 
     print("Informações alteradas!")
        


# FUNÇÕES DE 1.REGISTRAR OS DADOS DA SOLCITIAÇÃO E 2. EXIBIR NA TELA A SOLICITAÇÃO (SEGURANÇA)
def status_seguranca(banco_seguranca,titulo2):  
        segurancas=open(f'segurança_{titulo2}.txt', 'x',encoding="utf-8")  

        for e in banco_seguranca:
            segurancas.write(e+banco_seguranca[e]+'\n')      
        segurancas.close() 



def exibir_status_seguranca(banco_seguranca):
    print("Exibindo..")
    for e in banco_seguranca:
        print(e+banco_seguranca[e]) 

    pergunta_alterar=input("Pressione qualquer tecla para avançar ")
  
    while (pergunta_alterar!="S" or pergunta_alterar!="s") or (pergunta_alterar!="n" or pergunta_alterar!="N"): 
            pergunta_alterar=input("Gostaria de editar algo de sua solicitação? ") 
            if (pergunta_alterar=="N" or pergunta_alterar=="n"):
                print("Processo finalizado!")
                break
            elif (pergunta_alterar=="S" or pergunta_alterar=="s"):    
                titulo2=input("Digite o nome da solicitação que você quer ajustar")
                editar_status_seguranca(banco_seguranca,titulo2)
                break 
            else:
                print("Favor, responder S ou N")

           

def editar_status_seguranca(banco_seguranca,titulo2):
     qs1_ed=input("Sugestão/Preocupação do morador: ")
     qs2_ed=input("Incidente(s) identificado(s): ")
     qs3_ed=input("Áreas de melhorias: ")

     banco_seguranca={"Sugestão/Preocupação do morador: ":qs1_ed,"Incidente(s) identificado(s): ":qs2_ed,"Áreas de melhorias: ":qs3_ed} 
     seguranca_edit=open(f'segurança_{titulo2}.txt', 'w',encoding="utf-8")
     for e in banco_seguranca:   
        seguranca_edit.write(e+banco_seguranca[e]+'\n')  
     seguranca_edit.close() 
     print("Informações alteradas!")



# FUNÇÕES DE 1.REGISTRAR OS DADOS DA SOLCITIAÇÃO E 2. EXIBIR NA TELA A SOLICITAÇÃO (COMPORTAMENTO)
def status_comportamento(banco_comportamento,titulo3):  
        comportamentos=open(f'comportamento_{titulo3}.txt', 'x',encoding="utf-8")  

        for e in banco_comportamento:
            comportamentos.write(e+banco_comportamento[e]+'\n')      
        comportamentos.close() 
         


def exibir_status_comportamento(banco_comportamento):
    print("Exibindo..")
    for e in banco_comportamento:
        print(e+banco_comportamento[e])     

    pergunta_alterar=input("Pressione qualquer tecla para avançar ")
  
    while (pergunta_alterar!="S" or pergunta_alterar!="s") or (pergunta_alterar!="n" or pergunta_alterar!="N"): 
            pergunta_alterar=input("Gostaria de editar algo de sua solicitação? ") 
            if (pergunta_alterar=="N" or pergunta_alterar=="n"):
                print("Processo finalizado!")
                break
            elif (pergunta_alterar=="S" or pergunta_alterar=="s"):    
                titulo3=input("Digite o nome da solicitação que você quer ajustar")
                editar_status_seguranca(banco_comportamento,titulo3)
                break 
            else:
                print("Favor, responder S ou N")



def editar_status_comportamento(banco_comportamento,titulo3):
     qc1_ed=input("Situação/Situações: ")
     qc2_ed=input("Áreas com possiveis problemas: ")
     qc3_ed=input("Observações adicionais: ")

     banco_comportamento={"Situação/Situações: ":qc1_ed,"Áreas com possiveis problemas: ":qc2_ed,"Observações adicionais: ":qc3_ed} 
     comportamento_edit=open(f'comportamento_{titulo3}.txt', 'w',encoding="utf-8")
     for e in banco_comportamento:   
        comportamento_edit.write(e+banco_comportamento[e]+'\n')  
     comportamento_edit.close() 
     print("Informações alteradas!")



# FUNÇÕES DE 1.REGISTRAR OS DADOS DA SOLCITIAÇÃO E 2. EXIBIR NA TELA A SOLICITAÇÃO (SERVIÇO)
def status_servico(banco_servico,titulo4):  
        servicos=open(f'serviço_{titulo4}.txt', 'x',encoding="utf-8")  

        for e in banco_servico:
            servicos.write(e+banco_servico[e]+'\n')      
        servicos.close()          



def exibir_status_servico(banco_servico):
    print("Exibindo..")
    for e in banco_servico:
        print(e+banco_servico[e])
        
    pergunta_alterar=input("Pressione qualquer tecla para avançar ")
  
    while (pergunta_alterar!="S" or pergunta_alterar!="s") or (pergunta_alterar!="n" or pergunta_alterar!="N"): 
            pergunta_alterar=input("Gostaria de editar algo de sua solicitação? ") 
            if (pergunta_alterar=="N" or pergunta_alterar=="n"):
                print("Processo finalizado!")
                break
            elif (pergunta_alterar=="S" or pergunta_alterar=="s"):    
                titulo4=input("Digite o nome da solicitação que você quer ajustar")
                editar_status_servico(banco_servico,titulo4)
                break 
            else:
                print("Favor, responder S ou N")



def editar_status_servico(banco_servico,titulo4):
     qsv1_ed=input("Tipo de serviço solicitado: ")
     qsv2_ed=input("Localização do serviço: ")
     qsv3_ed=input("Descrição do problema: ")

     banco_servico={"Tipo de serviço solicitado: ":qsv1_ed,"Localização do serviço: ":qsv2_ed,"Descrição do problema: ":qsv3_ed} 
     servico_edit=open(f'serviço_{titulo4}.txt', 'w',encoding="utf-8")
     for e in banco_servico:   
        servico_edit.write(e+banco_servico[e]+'\n')  
     servico_edit.close() 
     print("Informações alteradas!")



# SEGUNDA ETAPA DO CÓDIGO (RESPONDER E INSERIR INPUTS de acordo com CATEGORIA SELECIONADA)
def solict(select_categoria):



    # SOLICITAÇÃO DE MANUTENÇÃO
    if select_categoria==1:  
        titulo1=input("Escreva o titulo da solicitação: ")
        qm1=input("Qual é a natureza do problema? (Exemplo: vazamento de água, problema elétrico, infiltração, etc.)")  
        while (qm1=="" or qm1==" "):
          print("Favor, preencher o campo!")
          qm1=input("Qual é a natureza do problema? (Exemplo: vazamento de água, problema elétrico, infiltração, etc.)")   
          
        qm2=input("Qual é a localização exata do problema que precisa de manutenção?")
        while (qm2=="" or qm2==" "):
          print("Favor, preencher o campo!")
          qm2=input("Qual é a localização exata do problema que precisa de manutenção?")   
                          
        qm3=input("O problema está afetando outras áreas ou unidades do condomínio?")  
        while ( qm3=="" or  qm3==" "):
          print("Favor, preencher o campo!")
          qm3=input("O problema está afetando outras áreas ou unidades do condomínio?")   
    

        banco_manutencao={"Tipo de problema: ":qm1,"Local: ":qm2,"Está afetando outras áreas?: ":qm3} 
        status_manutencao(banco_manutencao, titulo1)
        check=input("Pressiona qualquer tecla para prosseguir! ") 
        
        while (check!="S" or check!="s") or (check!="n" or check!="N"):
           
            check=input("Gostaria de verificar o status da solicitação? ") 
            if (check=="S" or check=="s"):    
                exibir_status_mauntencao(banco_manutencao)
                break 

            elif(check=="N" or check=="n"):
                print("Processo finalizado! Notificação encaminhada!")
                break
            else:
                print("Favor, responder S ou N")
        


    # SOLICITAÇÃO PARA SEGURANÇA
    elif select_categoria==2:
        titulo2=input("Escreva o titulo da solicitação: ")
        qs1=input("Qualquer a sugestão ou preocupação específica que você gostaria de compartilhar em relação à segurança do condomínio?")
        while (qs1=="" or qs1==" "):
          print("Favor, preencher o campo!")
          qs1=input("Qualquer asugestão ou preocupação específica que você gostaria de compartilhar em relação à segurança do condomínio?")
          

        qs2=input("Você já identificou algum incidente recente que tenha levantado preocupações de segurança no condomínio?")
        while (qs2=="" or qs2==" "):
          print("Favor, preencher o campo!")
          qs2=input("Você já identificou algum incidente recente que tenha levantado preocupações de segurança no condomínio?")   
          
                 
        qs3=input("Quais são as áreas específicas do condomínio que você acredita precisarem de melhorias na segurança?")  
        while ( qs3=="" or  qs3==" "):
          print("Favor, preencher o campo!")
          qs3=input("Quais são as áreas específicas do condomínio que você acredita precisarem de melhorias na segurança?")   
    
        
        banco_seguranca={"Sugestão/Preocupação do morador: ":qs1,"Incidente(s) identificado(s): ":qs2,"Áreas de melhorias: ":qs3}  
        status_seguranca(banco_seguranca,titulo2)
        check=input("Pressiona qualquer tecla para prosseguir! ") 

        while (check!="S" or check!="s") or (check!="n" or check!="N"):
           
            check=input("Gostaria de verificar o status da solicitação? ") 
            if (check=="S" or check=="s"):    
                exibir_status_seguranca(banco_seguranca)
                break 

            elif(check=="N" or check=="n"):
                print("Processo finalizado! Notificação encaminhada!")
                break
            else:
                print("Favor, responder S ou N")



    # SOLICITAÇÃO PARA RECLAMAÇÃO DE COMPORTAMENTO
    elif select_categoria==3:
        titulo3=input("Escreva o titulo da solicitação: ")
        qc1=input("Houve alguma situação específica recentemente que chamou a sua atenção em relação ao comportamento dos moradores?")
        while (qc1=="" or qc1==" "):
          print("Favor, preencher o campo!")
          qc1=input("Houve alguma situação específica recentemente que chamou a sua atenção em relação ao comportamento dos moradores?")

        qc2=input("Existem áreas comuns onde o comportamento dos moradores é mais problemático? Se sim, quais áreas?")
        while (qc2=="" or qc2==" "):
          print("Favor, preencher o campo!")
          qc2=input("Existem áreas comuns onde o comportamento dos moradores é mais problemático? Se sim, quais áreas?")   
          
                 
        qc3=input("Existe alguma observação ou preocupação adicional que você gostaria de compartilhar em relação ao comportamento no condomínio?")  
        while ( qc3=="" or  qc3==" "):
          print("Favor, preencher o campo!")
          qc3=input("Existe alguma observação ou preocupação adicional que você gostaria de compartilhar em relação ao comportamento no condomínio?")   
    

        banco_comportamento={"Situação/Situações: ":qc1,"Áreas com possiveis problemas: ":qc2,"Observações adicionais: ":qc3}  
        status_comportamento(banco_comportamento,titulo3) 
        check=input("Pressiona qualquer tecla para prosseguir! ") 
        
        while (check!="S" or check!="s") or (check!="n" or check!="N"):
           
            check=input("Gostaria de verificar o status da solicitação? ") 
            if (check=="S" or check=="s"):    
                exibir_status_comportamento(banco_comportamento)
                break 

            elif(check=="N" or check=="n"):
                print("Processo finalizado! Notificação encaminhada!")
                break
            else:
                print("Favor, responder S ou N")




    # SOLICITAÇÃO DE SERVIÇOS
    elif select_categoria==4:
        titulo4=input("Escreva o titulo da solicitação: ")
        qsv1=input("Qual é o tipo de serviço que você está solicitando para o condomínio?")
        while (qsv1=="" or qsv1==" "):
          print("Favor, preencher o campo!")
          qsv1=input("Qual é o tipo de serviço que você está solicitando para o condomínio?")

        qsv2=input("Qual é a localização exata do serviço que precisa ser realizado?")
        while (qsv2=="" or qsv2==" "):
          print("Favor, preencher o campo!")
          qsv2=input("Qual é a localização exata do serviço que precisa ser realizado?")   
          
                 
        qsv3=input("Descreva em detalhes o problema ou a necessidade que justifica a solicitação deste serviço")  
        while ( qsv3=="" or  qsv3==" "):
          print("Favor, preencher o campo!")
          qsv3=input("Descreva em detalhes o problema ou a necessidade que justifica a solicitação deste serviço")   
    

        banco_servico={"Tipo de serviço solicitado: ":qsv1,"Localização do serviço: ":qsv2,"Descrição do problema: ":qsv3}
        status_servico(banco_servico,titulo4)
        check=input("Pressiona qualquer tecla para prosseguir! ") 
        
        while (check!="S" or check!="s") or (check!="n" or check!="N"):
           
            check=input("Gostaria de verificar o status da solicitação? ") 
            if (check=="S" or check=="s"):    
                exibir_status_servico(banco_servico)
                break 

            elif(check=="N" or check=="n"):
                print("Processo finalizado! Notificação encaminhada!")
                break
            else:
                print("Favor, responder S ou N")
    else:
        print("Favor, inserir categoria válida")
      


# INICIO DO CÓDIGO: 

while True:
    try:
        print("Categorias para solicitação: ")
        print("1 - Manutenção")
        print("2 - Segurança")
        print("3 - Comportamento")
        print("4 - Serviço")  
        select_categoria=int(input("Favor, selecionar uma das categorias acima: "))
        solict(select_categoria)


        retornar_select=input("Deseja realizar outra solicitação?")
        if(retornar_select=="S" or retornar_select=="s"):
            print("Continuando...")
        elif(retornar_select=="N" or retornar_select=="n"):
            print("Processo finalizado!")
            break
        else:
            print("Favor, responder S ou N")
    except ValueError or select_categoria!=1 or select_categoria!=2 or select_categoria!=3 or select_categoria!=4:
        print("Digitar valor adequado")