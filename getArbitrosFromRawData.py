import functions as fun    #importa arquivo com todas as funções necessarias
import openpyxl
import pickle
brasileirao = 'brasileiraoSerieA.xlsx'

wbBrasileirao = openpyxl.load_workbook(brasileirao) #coloca a variavel em workbook (arquivo é como se fosse um livro)
wsBrasileirao = wbBrasileirao['Sheet1'] #como se estivesse escolhendo a página de um livro, no caso uma aba do excel
matBrasileirao = list(wsBrasileirao)    #para trabalharmos com matrizes ao invés de 'celulas'

partidas = []
arbitros = []
id_local = 0;
fun.colocaTupla(matBrasileirao, partidas)

for partida in partidas:
    if len(arbitros) > 0:
        ja_tem = False;
        for arbitro in arbitros:
            if partida["arbitro"] == arbitro["nome"]:
                ja_tem = True

            if (ja_tem):
                break

        if(not ja_tem):
            arbitros.append({"id": id_local, "nome": partida["arbitro"]})
            id_local+=1
    else:
        arbitros.append({"id": 0, "nome": partida["arbitro"]})
        id_local+=1

with open("arbitros.bin", "wb") as arquivo:
    pickle.dump(arbitros,arquivo)

print(arbitros)