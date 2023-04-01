import functions as fun    #importa arquivo com todas as funções necessarias
import openpyxl
import json
import pandas as pd
import pickle 

brasileirao = 'brasileiraoSerieA.xlsx'

wbBrasileirao = openpyxl.load_workbook(brasileirao) #coloca a variavel em workbook (arquivo é como se fosse um livro)
wsBrasileirao = wbBrasileirao['Sheet1'] #como se estivesse escolhendo a página de um livro, no caso uma aba do excel
matBrasileirao = list(wsBrasileirao)    #para trabalharmos com matrizes ao invés de 'celulas'

partidas = []
locais = []

fun.colocaTupla(matBrasileirao, partidas)

id_local = 0

for partida in partidas:
    if len(locais) > 0:
        ja_tem = False;
        for local in locais:
            if partida["estadio"] == local["estadio"]:
                if partida["publico_max"] == local["publico_max"]:
                    ja_tem = True
                else:
                    local["publico_max"] = partida["publico_max"]
                    ja_tem = True
                    break

            if (ja_tem):
                break

        if(not ja_tem):
            locais.append({"id": id_local, "estadio": partida["estadio"], "publico_max": partida["publico_max"]})
            id_local+=1
    else:
        locais.append({"id":0, "estadio": partida["estadio"], "publico_max": partida["publico_max"]})
        id_local+=1

with open("locais.bin", "wb") as arquivo:
    pickle.dump(locais,arquivo)

print(locais)

