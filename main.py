#Trabalho final da disciplina de Classificação e Pesquisa de Dados
#*****************************************************************
#João Pedro Licks Corso - 00337569********************************
#Arthur Ferreira Ely - 00338434***********************************

import functions as fun    #importa arquivo com todas as funções necessarias

#importa arquivos py que criam os arquivos binarios
import getArbitrosFromRawData as arbitros
import getLocaisFromRawData as locais


import openpyxl
import json
import pandas as pd

brasileirao = 'brasileiraoSerieA.xlsx'

#brasileirao = pd.read_excel('brasileiraoSerieA.xls')
#brasileirao.to_excel('brasileiraoSerieA.xlsx', index=False)  #converte xls para xlsx

wbBrasileirao = openpyxl.load_workbook(brasileirao) #coloca a variavel em workbook (arquivo é como se fosse um livro)
wsBrasileirao = wbBrasileirao['Sheet1'] #como se estivesse escolhendo a página de um linvro, no caso uma aba do excel
matBrasileirao = list(wsBrasileirao)    #para trabalharmos com matrizes ao invés de 'celulas'

listaDados = []

fun.colocaTupla(matBrasileirao, listaDados)

#chama escrita de arquivos
arbitros
locais



print(listaDados[0])