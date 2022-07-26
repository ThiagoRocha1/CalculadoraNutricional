from random import choice;
from datetime import date;
from funcoes_aux import *;

def montar_prato(dic_folhas,dic_leguminosas,dic_proteinas,dic_tuberculos,dic_legumes):
    '''Essa funcao irá retornar um prato aleatório dado a quantidade de calorias por grupo que voce desejar. Essa funcao retornará
    a quantidade, em gramas, de cada alimento que você precisará colocar de cada alimento.'''

    #Escolher Calorias para cada grupo.

    cal_folhas = verificar_entrada_numero_densidade(input('Digite a quantidade de calorias que você deseja para folhas: '))
    if cal_folhas == -1:
        print('Error. Argumento inserido de maneira inválida.')
        return -1

    cal_leguminosas = verificar_entrada_numero_densidade(input('Digite a quantidade de calorias que você deseja para leguminosas: '))
    if cal_leguminosas == -1:
        print('Error. Argumento inserido de maneira inválida.')

        return -1

    cal_proteinas = verificar_entrada_numero_densidade(input('Digite a quantidade de calorias que você deseja para proteinas: '))
    if cal_proteinas == -1:
        print('Error. Argumento inserido de maneira inválida.')

        return -1

    cal_tuberculos = verificar_entrada_numero_densidade(input('Digite a quantidade de calorias que você deseja para tuberculos: '))
    if cal_tuberculos == -1:
        print('Error. Argumento inserido de maneira inválida.')

        return -1
    
    cal_legumes = verificar_entrada_numero_densidade(input('Digite a quantidade de calorias que você deseja para legumes: '))
    if cal_legumes == -1:
        print('Error. Argumento inserido de maneira inválida.')

        return -1
    print('')

    #Escolher um alimento nos dicionarios de alimentos e calcular quanto, em gramas, deverá ser consumido ser consumido
    #Essa seçao abaixo transforma as chaves dos dicionarios em uma lista para que se possa acessar uma chave aleatoria
    #O esperado é uma lista com as chaves dos dicionarios. ex: [*dic_folhas = ['folha1','folha2','folha3']
    
    chaves_folhas= [*dic_folhas]
    chaves_leguminosas= [*dic_leguminosas]
    chaves_proteinas= [*dic_proteinas]
    chaves_tuberculos= [*dic_tuberculos]
    chaves_legumes= [*dic_legumes]

    #Escolher um alimento dentro da lista com as chaves dos valores

    folha = choice(chaves_folhas)
    leguminosa = choice(chaves_leguminosas)
    proteina = choice(chaves_proteinas)
    tuberculo = choice(chaves_tuberculos)
    legume = choice(chaves_legumes) 
    

    #Calcular a quantidade que será necessaria de cada alimento.(gramas)

    qnt_folha = float(cal_folhas/dic_folhas[folha])
    qnt_leguminosa = float(cal_leguminosas/dic_leguminosas[leguminosa])
    qnt_proteina = float(cal_proteinas/dic_proteinas[proteina])
    qnt_tuberculo = float(cal_tuberculos/dic_tuberculos[tuberculo])
    qnt_legume = float(cal_legumes/dic_legumes[legume])

    #Mostrar par ao usuario quanto ele deverá consumir de cada grupo.
    print('-'*30)
    print('Está pronto seu prato! Boa refeição :) ')
    print('-'*30)

    print('')
    print(f'Você deverá consumir {qnt_folha:.3f} gramas de {folha}.')
    print(f'Você deverá consumir {qnt_leguminosa:.3f} gramas de {leguminosa}.')
    print(f'Você deverá consumir {qnt_proteina:.3f} gramas de {proteina}.')
    print(f'Você deverá consumir {qnt_tuberculo:.3f} gramas de {tuberculo}.')
    print(f'Você deverá consumir {qnt_legume:.3f} gramas de {legume}.')
    print('')
    print('')

    #Quantidade total de comida e quantas calorias

    calorias_totais = cal_folhas + cal_leguminosas + cal_proteinas + cal_tuberculos + cal_legumes 
    gramas_totais = qnt_folha + qnt_leguminosa + qnt_proteina + qnt_tuberculo + qnt_legume

    print(f'Calorias totais: {calorias_totais}     Peso Total: {gramas_totais:.3f} gramas')

def olhar_info_alimento(lista_dicionarios):
    '''Essa funcao recebe como alimento uma lista de dicionarios e retorna a info de determinado alimento'''

    #Verificar se o alimento existe
    
    alimento = verificar_entrada_str(input('Digite o nome do alimento: ')) #Analisando o input

    if alimento == 'error':
        verificar_entrada_str(alimento)
        return -1

    #Codigo caso o alimento exista
    if verificar_existencia_alimento(lista_dicionarios,alimento) == 'existe':
        #Acessar a lista de dicionarios
        for dicionario in lista_dicionarios:#Acessando Lista de Dicionarios
            if alimento.lower() in dicionario:#Verificando o alimento
                
                #Analisar o grupo que o alimento se econtra

                #Grupo Folhas
                if lista_dicionarios.index(dicionario) == 0:
                    print('')
                    print(f'O alimento: {alimento} pertence ao grupo das folhas e possui {dicionario[alimento]} de Kcal/grama')
                    print('')

                #Grupo Leguminosa
                elif lista_dicionarios.index(dicionario) == 1:
                    print('')
                    print(f'O alimento: {alimento} pertence ao grupo das leguminosas e possui {dicionario[alimento]} de Kcal/grama')
                    print('')

                #Grupo Proteina
                elif lista_dicionarios.index(dicionario) == 2:
                    print('')
                    print(f'O alimento: {alimento} pertence ao grupo das proteínas e possui {dicionario[alimento]} de Kcal/grama')
                    print('')

                #Grupo Tuberculo
                elif lista_dicionarios.index(dicionario) == 3:
                    print('')
                    print(f'O alimento: {alimento} pertence ao grupo dos tuberculos e possui {dicionario[alimento]} de Kcal/grama')
                    print('')

                #Grupo Legume
                elif lista_dicionarios.index(dicionario) == 4:
                    print('')
                    print(f'O alimento: {alimento} pertence ao grupo dos legumes e possui {dicionario[alimento]} de Kcal/grama')
                    print('')

    #Codigo caso o alimento nao exista
    elif verificar_existencia_alimento(lista_dicionarios,alimento) == 'nao_existe':
        print('')
        print('Alimento não cadastrado!')
        return -1

def adicionar_alimento(lista_dicionarios):
    '''Essa funcao permite adicionar um alimento na lista de dicionarios e retorna o dicionario atualizado'''

    #Recebendo o alimento

    alimento = verificar_entrada_str(input('Digite o alimento que deseja adicionar: '))

    if alimento == 'error': #Argumento inserido de maneira inválida
        verificar_entrada_str(alimento)
        return -1

    #Recebendo sua densidade
    densidade_cal = verificar_entrada_numero_densidade(input('Digite a densidade calórica do alimento: '))
    #Densidade negativa
    if densidade_cal < 0:
        verificar_entrada_numero_densidade(densidade_cal)
        return -1

    #Alimento ja cadastrado
    if verificar_existencia_alimento(lista_dicionarios,alimento) == 'existe':
        print('')
        print('Alimento já cadastrado!')
        print('')

        return -1
 
    #Alimento nao cadastrado
    elif verificar_existencia_alimento(lista_dicionarios,alimento) == 'nao_existe':   
        #Inserir o grupo do alimento
        while True:

            print('Digite o grupo que deseja incluir o alimento:')
            print('')
            mostrar_dados_grupo_alimentos() #Mostrar os grupos
            try:
                escolha = int(input('Digite a usa escolha: '))
            except:
                print('Error')
                return -1

            #Dic Folhas
            if escolha == 0:
                lista_dicionarios[0][alimento] = densidade_cal#Add o alimento

                print(lista_dicionarios[0])#Mostra o dic atualizazdo
                print('')

                return lista_dicionarios#Retorna a lista atualizada

            

            #Dic Leguminosa
            if escolha == 1:
                lista_dicionarios[1][alimento] = densidade_cal #Add o alimento

                print(lista_dicionarios[1])#Mostra o dic atualizazdo
                print('')

                return lista_dicionarios #Retorna a lista atualizada
            
            #Dic Proteina

            if escolha == 2:
                lista_dicionarios[2][alimento] = densidade_cal #Add o alimento

                print(lista_dicionarios[2])#Mostra o dic atualizazdo
                print('')

                return lista_dicionarios #Retorna a lista atualizada

            
            #Dic Tuberculo
            if escolha == 3:
                lista_dicionarios[3][alimento] = densidade_cal #Add o alimento

                print(lista_dicionarios[3])#Mostra o dic atualizazdo
                print('')

                return lista_dicionarios #Retorna a lista atualizada

            #Dic Legumes
            if escolha == 4:
                lista_dicionarios[4][alimento] = densidade_cal #Add o alimento

                print(lista_dicionarios[4])#Mostra o dic atualizazdo
                print('')

                return lista_dicionarios #Retorna a lista atualizada

def alterar_alimento(lista_dicionarios):

    #Recebendo o alimento
    alimento = verificar_entrada_str(input('Digite o alimento que deseja alterar: '))

    if alimento == 'error': #Argumento inserido de maneira inválida
        print('Error')
        return -1

    #Recebendo sua densidade
    densidade_cal = verificar_entrada_numero_densidade(input('Digite a calórica do alimento: '))
    #Densidade negativa
    if densidade_cal < 0:
        return -1

    #Alimento ja cadastrado
    if verificar_existencia_alimento(lista_dicionarios,alimento) == 'existe':

        while True:

            print('Digite o grupo que deseja incluir o alimento:')
            print('')
            mostrar_dados_grupo_alimentos() #Mostrar os grupos
            try:
                escolha = int(input('Digite a usa escolha: '))
            except:
                print('Error')
                return -1

            #Dic Folhas
            if escolha == 0:
                lista_dicionarios[0][alimento] = densidade_cal#Add o alimento

                print(lista_dicionarios[0])#Mostra o dic atualizazdo
                print('')

                return lista_dicionarios#Retorna a lista atualizada

            

            #Dic Leguminosa
            if escolha == 1:
                lista_dicionarios[1][alimento] = densidade_cal #Add o alimento

                print(lista_dicionarios[1])#Mostra o dic atualizazdo
                print('')

                return lista_dicionarios #Retorna a lista atualizada
            
            #Dic Proteina

            if escolha == 2:
                lista_dicionarios[2][alimento] = densidade_cal #Add o alimento

                print(lista_dicionarios[2])#Mostra o dic atualizazdo
                print('')

                return lista_dicionarios #Retorna a lista atualizada

            
            #Dic Tuberculo
            if escolha == 3:
                lista_dicionarios[3][alimento] = densidade_cal #Add o alimento

                print(lista_dicionarios[3])#Mostra o dic atualizazdo
                print('')

                return lista_dicionarios #Retorna a lista atualizada

            #Dic Legumes
            if escolha == 4:
                lista_dicionarios[4][alimento] = densidade_cal #Add o alimento

                print(lista_dicionarios[4])#Mostra o dic atualizazdo
                print('')

                return lista_dicionarios #Retorna a lista atualizada 
 
    #Alimento nao cadastrado
    elif verificar_existencia_alimento(lista_dicionarios,alimento) == 'nao_existe':
        print('Alimento não cadastrado.')
        return -1

def conversor_caloria(lista_dicionarios):
    '''Essa funcao converte quanto voce precisa consumir, em gramas de um alimento para o outro. ex:Quero saber quanto
    preciso consumir de arroz tendo 40 gramas de batata doce.'''

    #Receber dados do usuario
    #Tratamento de erro
    #Alimento Inicial

    alimento_inicial  = verificar_entrada_str(input('Digite o nome do alimento inicial: '))

    #Digitou o dado de maneira errada

    if alimento_inicial == 'error' or verificar_existencia_alimento(lista_dicionarios,alimento_inicial) == 'nao_existe':
        print('Error. Alimento não existe e/ou insetido de maneira incorreta.')
        return -1

    #Qunatidade alimento inicial
    qnt_alimento_inicial =  verificar_entrada_numero_densidade(input('Digite a quantidade, em gramas, do alimento que voce tem: '))

    #Digitou o dado de maneira errada
    if qnt_alimento_inicial == -1:
        verificar_entrada_numero_densidade(qnt_alimento_inicial)
        return -1
    
    #Alimento que será convertido
    print('')
    alimento_convertido = verificar_entrada_str(input('Digite o nome do alimento que será convertido: '))
    
    #Digitou o dado de maneira errada
    if alimento_convertido == 'error' or verificar_existencia_alimento(lista_dicionarios,alimento_convertido) == 'nao_existe':
        print('Error. Alimento nao existe ou inserido de maneira errada.')
        return -1

    #Fazer a conversão 
    #Acessar a lista de dicionarios para o alimento inicial
    for dicionario in lista_dicionarios:#Acessando Lista de Dicionarios
        if alimento_inicial in dicionario:#Verificando o alimento
            #Achar a quantidade de Calorias Totais que tem na refeicao

            calorias_totais = dicionario[alimento_inicial]*qnt_alimento_inicial
        
    #Acessar a lista de dicionarios para o alimento convertido

    for dicionario2 in lista_dicionarios:#Acessando Lista de Dicionarios
        if alimento_convertido in dicionario2:#Verificando o alimento

            qnt_final = calorias_totais/dicionario2[alimento_convertido]
            print('')
            print(f'Você deverá consumir {qnt_final:.2f} gramas de {alimento_convertido}>')

def registrar_refeicao(str_historico):
    '''Essa função adiciona uma refeição no arquivo de histórico.'''
    #Abrir o arquivo de historico
    arq_historico = open(f'{str_historico}','a')

    #Pegar a data que o usuário está utilizando o sistema

    data = date.today() #AAA-MM--DD
    data = str(data)#Trasnformar a data em uma string

    #Liha que será escrita
    linha_final= data+',' #Adicionar data na string

    #Quantos alimentos a pessoa consumiu
    print('Máximo de 8 tipos de alimentos distintos em um mesmo prato.')
    print('')
    try:
        num_alimento =int(input('Digite a quantidade de alimentos que você consumiu: '))
        #Ver o numero maximo de alimentos. 8 máx
        if num_alimento >8:
            raise ValueError
        if num_alimento <= 0:
            raise ValueError
    
    except ValueError:#Erro de valor
        print('Numero inválido.')
        return -1
    except:#Erro geral
        print('Error')
        return -1

    else:

        #Pegar as informações do usuário
        for i in range(0,num_alimento):#Pegar os alimentos que a pessoa consumiu

            alimento = input(f'Digite o alimento {i+1}: ')

            #Verificacao do alimento 
            
            if verificar_entrada_str(alimento) == 'error':
                return -1
            
            #Alimento insetido de maneira correta
            else: 
                linha_final = linha_final+alimento.lower()+',' #Expectativa: Data,A1,A2,A3,A4,
                
        
        #Saber quantidade de Kcal
        kcal = verificar_entrada_numero_densidade(input('Digite o numero de Kcal: '))

        if kcal == -1:
            print('Argumento inserido de maneirda inválida!')
            return -1

        kcal = str(kcal) #Transformar em string
        
        #Ajustar os dados da linha final
        linha_final = linha_final+kcal+'\n'

        #Escrever no arquivo de histórico

        arq_historico.write(linha_final)
        arq_historico.close()#Fechar o arquivo

        print('')

        return linha_final

def olhar_refeicao_dia(str_historico):
    '''Essa funcao permite pegar informacoes de refeicoes de um dia'''

    #Receber dados do usuario
    dia = verifica_entrada_data(input ('Digite o dia: '))
    mes = verifica_entrada_data(input ('Digite o mes: '))
    ano = verifica_entrada_data(input ('Digite o ano: '))
    print('')
    
    if dia == -1 or dia > 31 or mes == -1 or mes>12 or ano == -1: #Analisar se os valores foram escritos de maneira correta
        print('Valor inserido de maneira errada!')
        return -1

    data_analisar = date(ano,mes,dia) #Data para Análise Ex: AAAA-MM-DD
    data_analisar = str(data_analisar) #Transformar em String


    #Abrir o arquivo de historico

    arq_historico = open(f'{str_historico}','r') #Abrir o arquivo para saber o num de refeições

    linha = arq_historico.readline() #Ler uma linha do arquvio 

    num_refeicao = 0 #Contador para analsiar quantas refeicoes tiveram no dia
    
    #Loop para ler todas as linhas do histórico
    while linha != '':

        lista_linha = linha.split(',') #Separar as infos da linha em uma lista ex: ['data','a1','kcal']

        if lista_linha[0] == data_analisar: #Houve refeição

            num_refeicao+=1

            print(f'A refeição {num_refeicao} do dia {data_analisar} foi:') #Quantas refeicoes houveram
            print('')

            if lista_linha[0] == data_analisar: #Se a data correspender a de analise

                lista_alimentos = lista_linha[1:-1] #Lista com os alimentos
                
                for alimento in lista_alimentos: #Alimentos
                    print(f'{alimento}',end=';')
                    print('',end='\n')
                
                print('')
                print(f'Com um total de {lista_linha[-1]} calorias.')#Kcal
                print('')
        
        linha = arq_historico.readline()

    #Caso não Haja nenhuma refeição
    if num_refeicao == 0: 
        print('Não há registro de refeições nesse dia.')
        return -1

def salvar(dic_folhas,dic_leguminosas,dic_proteinas,dic_tuberculos,dic_legumes):
    '''Essa função salva os dados de cada dicionario alterado ao sair do sistema'''
    #Acessar os arquivos de cada grupo alimentar

    salvar_dicionario_arquivo('folhas.txt',dic_folhas)#Folhas
    salvar_dicionario_arquivo('leguminosas.txt',dic_leguminosas)#Leguminosas
    salvar_dicionario_arquivo('proteinas.txt',dic_proteinas)#Proteinas
    salvar_dicionario_arquivo('tuberculos.txt',dic_tuberculos)#Tuberculos
    salvar_dicionario_arquivo('legumes.txt',dic_legumes)#Legumes


if __name__ == '__main__':
    dic_folhas=criar_dicionario_alimento('folhas.txt')
    dic_leguminosas=criar_dicionario_alimento('leguminosas.txt')
    dic_proteinas= criar_dicionario_alimento('proteinas.txt')
    dic_tuberculos=criar_dicionario_alimento('tuberculos.txt')
    dic_legumes = criar_dicionario_alimento('legumes.txt')
    lista_dicionarios = [dic_folhas,dic_leguminosas,dic_proteinas,dic_tuberculos,dic_legumes]
    #montar_prato(dic_folhas,dic_leguminosas,dic_proteinas,dic_tuberculos,dic_legumes)
    #print(criar_dicionario_alimento('proteinas.txt'))
    #olhar_info_alimento(lista_dicionarios)
    #print(adicionar_alimento(lista_dicionarios))
    #conversor_caloria(lista_dicionarios)
    #registrar_refeicao('historico.txt')
    #olhar_refeicao_dia('historico.txt')
    #dic_folhas['teste1'] = 1
    #alterar_alimento(lista_dicionarios)
    #adicionar_alimento(lista_dicionarios)
    salvar(dic_folhas,dic_leguminosas,dic_proteinas,dic_tuberculos,dic_legumes)
