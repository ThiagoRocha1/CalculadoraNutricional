from funcoes import *;


def sistema (str_folhas='folhas.txt',str_leguminosas='leguminosas.txt',str_proteinas='proteinas.txt',str_tuberculos='tuberculos.txt',str_legumes='legumes.txt',str_historico='historico.txt'):
    #Criar os dicionários do sistema
    dic_folhas=criar_dicionario_alimento(f'{str_folhas}')
    dic_leguminosas=criar_dicionario_alimento(f'{str_leguminosas}')
    dic_proteinas= criar_dicionario_alimento(f'{str_proteinas}')
    dic_tuberculos=criar_dicionario_alimento(f'{str_tuberculos}')
    dic_legumes = criar_dicionario_alimento(f'{str_legumes}')
    lista_dicionarios = [dic_folhas,dic_leguminosas,dic_proteinas,dic_tuberculos,dic_legumes]

    #Mostrando as opções 

    while True:
        print('')
        print('Olá! Seja bem vindo ao Foodie!')

        mostrar_opcoes_menu()

        try:
            escolha = int(input('Digite sua escolha:'))

        except KeyboardInterrupt :
            print('Sistema interrompido.')
            break

        except:
            print('Você digitou um valor inválido, reniciando o sistema!')
            print('')
            continue

        if escolha == 1:#Montar Prato Aleatório
            print('')
            print('Escolha 1')
            print('')
            montar_prato(dic_folhas,dic_leguminosas,dic_proteinas,dic_tuberculos,dic_legumes)


        if escolha == 2:# Registrar Refeição do dia
            print('')
            print('Escolha 2')
            print('')
            print(registrar_refeicao(f'{str_historico}'))


        if escolha == 3:#Olhar Refeição de algum dia
            print('')
            print('Escolha 3')
            print('')
            olhar_refeicao_dia(f'{str_historico}')

        if escolha == 4:#Conversor de Calorias
            print('')
            print('Escolha 4')
            print('')
            conversor_caloria(lista_dicionarios)

        if escolha == 5:#Olhar info Alimento
            print('')
            print('Escolha 5')
            print('')
            olhar_info_alimento(lista_dicionarios)


        if escolha == 6:#Cadastrar novo alimento em um grupo
            print('')
            print('Escolha 6')
            print('')
            adicionar_alimento(lista_dicionarios)


        if escolha == 7:#Alterar dados
            print('')
            print('Escolha 7')
            print('')
            alterar_alimento(lista_dicionarios)


        if escolha == 0:
            salvar(dic_folhas,dic_leguminosas,dic_proteinas,dic_tuberculos,dic_legumes)
            print('Até breve! ::) ')
            break
        
sistema()
  