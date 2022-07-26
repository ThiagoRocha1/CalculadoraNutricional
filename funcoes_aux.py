def criar_dicionario_alimento(str_alimento):

    '''#Funcao criada para ler os arquvos dos sistema e transforma-los em dicionarios para a manipulacao no sistema
    Recebe um arquivo e retorna um dicionario onde a chave é o alimento e o seu valor a densidade calorica'''


    #Tratamento de exceção.
    #Caso tente colocar o nome de um arquivo de uma forma diferente de uma string

    if type(str_alimento) != str:
        print('Arquivo inserido de maneira invalida!')
        return -1


    #Criar Dicionario Vazio
    dic_alimento ={}

    #Criar variavel para abrir o arquivo 

    arq_alimento = open(f'{str_alimento}','r') # Abrir o arquivo para leitura

    #Ler linhas dos arquivos e retornar uma lista de strings com cada linha do arquivo 
    # Esperado = ['alimento1,densidade\n','alimento2,densidade\n]

    linhas_arquivo_alimento = arq_alimento.readlines() 

   

    #Acessar as linhas do arquivo para separa-la em uma lista

    for linha in linhas_arquivo_alimento:

        #Transformar essa lihna em uma lista

        lista_arquivo_alimento = linha.split(',') #['Alimento','densidade\n']

        #Adicionar no dicionario
        #Para tirar o \n, iremos trasnformar a densidade um float

        dic_alimento[lista_arquivo_alimento[0]] = float(lista_arquivo_alimento[1])# Transformar em float para sumir o \n


    arq_alimento.close() #Fechar o arquivo

    return dic_alimento

def verificar_existencia_alimento (lista_dicionarios,verificar_alimento):
    '''Essa funcao verifica a existencia de um alimento na lista de dicionarios do sistema. Ela rececebe como argumento
    uma lista de dicionarios e um alimento para ser verificado,e retorna a string 'existe' caso o alimento exista e
    nao_existecaso o alimento nao exista'''

    #Tratamento de exceção

    if type(verificar_alimento) != str:
        print('Nome do alimento inserido de maneira inválida.')
        return -1

    #Acessar a lista de dicionarios

    for dicionario in lista_dicionarios:#Acessando Lista de Dicionarios
        if verificar_alimento.lower() in dicionario:#Verificando o alimento
            return 'existe'

    
    if dicionario == lista_dicionarios[-1]: #Caso percorra a lista toda e o alimento nao exista
        return 'nao_existe'

def verificar_entrada_str(string):
    '''Verifica a entrada do tipo string para funcoes; Caso de problema, retornará -1'''
    try: #Verificar se o usuario escreveu um numero

        inteiro = int(string) 
        flutuante = float(string)
        print('Argumento nao pode ser um numero!')
        return 'error'

    except: #Escreveu um dado como uma string

        if type(string) != str or string=='': #Nao digitou um texto
            print('Argumento inserido de maneira incorreta!')
            return 'error'

        else:
            return string.lower()

def verificar_entrada_numero_densidade(numero):
    '''Verifica se a etrada é um número válido'''

    try:
        numero = float(numero)
        
        if numero <= 0:
            raise ValueError

        return numero

    except ValueError:
        print('')
        print('Impossivel transformar valor inserido em um número!')
        print('')

        return -1

    except:
        print('')
        print('Error não identificado!')
        print('')

        return -1

def verifica_entrada_data(numero):
    '''Verifica a entrada para data'''
    #Converter para inteiro
    try:
        numero  = int(numero)

        if numero <0:
            raise ValueError

        return numero
    
    except ValueError:
        return -1

    except:
        return -1

def mostrar_dados_grupo_alimentos():
            print('')
            print('0 - Folhas')
            print('1 - Leguminosa')
            print('2 - Proteina')
            print('3 - Tuberculos')
            print('4 - Legumes')
            print('')

def salvar_dicionario_arquivo(str_arquivo,dic_alimento):
    #Acessando Arquivo
    arq = open(f'{str_arquivo}','w')

    for alimento in dic_alimento:#Acessar cada alimento no dicionario
        arq.write(alimento+','+str(dic_alimento[alimento])+'\n')# Ex: Alimento,DensidadeCalorica\n

    arq.close()

def mostrar_opcoes_menu():

    print('-'*35)
    print('1 - Montar prato aleatório')
    print('2 - Registrar Refeição do dia.')
    print('3 - Olhar Refeição de algum dia.')
    print('4 - Conversor de Calorias.')
    print('5 - Olhar info Alimento.')
    print('6 - Cadastrar novo alimento em um grupo.')
    print('7 - Alterar dados do alimento.')
    print('0 - Sair e Salvar.')
    print('-'*35)


if __name__ =='__main__':
    dic_folhas=criar_dicionario_alimento('folhas.txt')
    dic_leguminosas=criar_dicionario_alimento('leguminosas.txt')
    lista_dicionarios = [dic_folhas,dic_leguminosas]
    
