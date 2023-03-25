import functions as fun    #importa arquivo com todas as funções necessarias
import openpyxl
import pickle
brasileirao = 'brasileiraoSerieA.xlsx'

wbBrasileirao = openpyxl.load_workbook(brasileirao) #coloca a variavel em workbook (arquivo é como se fosse um livro)
wsBrasileirao = wbBrasileirao['Sheet1'] #como se estivesse escolhendo a página de um livro, no caso uma aba do excel
matBrasileirao = list(wsBrasileirao)    #para trabalharmos com matrizes ao invés de 'celulas'

partidas = []
tecnicos = []

id_tecnicos = 0;

fun.colocaTupla(matBrasileirao, partidas)

for partida in partidas:
    ja_tem = False
    for tecnico in tecnicos:

        if partida["tecnico_man"] == tecnico["nome"]:
            ja_tem = True

        if(ja_tem):
            break

    if (not ja_tem):
        tecnicos.append({"id": id_tecnicos, "nome": partida["tecnico_man"]})
        id_tecnicos += 1

with open("tecnicos.bin", "wb") as arquivo:
    pickle.dump(tecnicos,arquivo)
        
print(tecnicos)