import functions as fun    #importa arquivo com todas as funções necessarias
import openpyxl
import pickle
brasileirao = 'brasileiraoSerieA.xlsx'

wbBrasileirao = openpyxl.load_workbook(brasileirao) #coloca a variavel em workbook (arquivo é como se fosse um livro)
wsBrasileirao = wbBrasileirao['Sheet1'] #como se estivesse escolhendo a página de um livro, no caso uma aba do excel
matBrasileirao = list(wsBrasileirao)    #para trabalharmos com matrizes ao invés de 'celulas'

partidas = []

fun.colocaTupla(matBrasileirao, partidas)


arbitros = []
with open("arbitros.bin", "rb") as arquivo:
    arbitros = pickle.load(arquivo)
    arquivo.close()
    
locais = []
with open("locais.bin", "rb") as arquivo:
    locais = pickle.load(arquivo)
    arquivo.close()

tecnicos = []
with open("tecnicos.bin", "rb") as arquivo:
    tecnicos = pickle.load(arquivo)
    arquivo.close()

times = []
with open("times.bin", "rb") as arquivo:
    times = pickle.load(arquivo)
    arquivo.close()

for partida in partidas:
    for local in locais:
        if local["estadio"] == partida["estadio"]:
            partida["estadio"] = local["id"]
            partida["publico_max"] = local["id"]
            break
    
    for arbitro in arbitros:
        if arbitro["nome"] == partida["arbitro"]:
            partida["arbitro"] = arbitro["id"]
            break

    for tecnico in tecnicos:
        if partida["tecnico_man"] == tecnico["nome"]:
            partida["tecnico_man"] = tecnico["id"]
            break

    for tecnico in tecnicos:
        if partida["tecnico_vis"] == tecnico["nome"]:
            partida["tecnico_vis"] = tecnico["id"]
            break   

    for time in times:
        if partida["time_vis"] == time["nome"]:
            partida["time_vis"] = time["id"]
            break

    for time in times:
        if partida["time_man"] == time["nome"]:
            partida["time_man"] = time["id"]
            break

with open("partidas.bin", "wb") as arquivo:
    pickle.dump(partidas,arquivo)

print(partidas)