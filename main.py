#Trabalho final da disciplina de Classificação e Pesquisa de Dados
#*****************************************************************
#João Pedro Licks Corso - 00337569********************************
#Arthur Ferreira Ely - 00338434***********************************

import functions as fun    #importa arquivo com todas as funções necessarias
import getPartida as getPart
import teamHistory as TH
import rankings as RK
import arbitros_page as ARB
#importa arquivos py que criam os arquivos binarios
import pandas as pd

def opcao_um():
    TH.teamHistory()

def opcao_dois():
    print("Opção 2 selecionada.")

def opcao_tres():
    ARB.arbitros()

def opcao_quatro():
    RK.rankings()


while True:
    # SWITCH
    print("futeTUDO - Saiba tudo sobre o mundo da bola")
    print("-------------------------------------------")
    print("o que você deseja saber?")
    print("1 - Históricos")
    print("2 - Confrontos")
    print("3 - Árbitros")
    print("4 - Rankings")
    print("5 - Sair")
    opcao = input("Digite o número da opção desejada (1, 2, 3 ou 4): ")

    # Executa a opção selecionada pelo usuário
    if opcao == "1":
        opcao_um()
    elif opcao == "2":
        opcao_dois()
    elif opcao == "3":
        opcao_tres()
    elif opcao == "4":
        opcao_quatro()
    elif opcao == "5":
        print("Encerrando programa...")
        break
    else:
        print("Opção inválida. Digite apenas 1, 2, 3 ou 4.")