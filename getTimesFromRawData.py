import functions as fun    #importa arquivo com todas as funções necessarias
import openpyxl
import pickle
brasileirao = 'brasileiraoSerieA.xlsx'

wbBrasileirao = openpyxl.load_workbook(brasileirao) #coloca a variavel em workbook (arquivo é como se fosse um livro)
wsBrasileirao = wbBrasileirao['Sheet1'] #como se estivesse escolhendo a página de um livro, no caso uma aba do excel
matBrasileirao = list(wsBrasileirao)    #para trabalharmos com matrizes ao invés de 'celulas'

partidas = []
times = []

id_times = 0;

fun.colocaTupla(matBrasileirao, partidas)

for partida in partidas:
    ja_tem = False
    for time in times:

        if partida["time_man"] == time["nome"]:
            ja_tem = True

        if(ja_tem):
            break

    if (not ja_tem):
        times.append({"id": id_times, "nome": partida["time_man"]})
        id_times += 1

with open("times.bin", "wb") as arquivo:
    pickle.dump(times, arquivo)
        
print(times)