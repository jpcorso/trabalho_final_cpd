import openpyxl
import pickle
import heapq
#import getPartida

def getPartidas():

    brasileirao = 'brasileiraoSerieA.xlsx'

    wbBrasileirao = openpyxl.load_workbook(brasileirao) #coloca a variavel em workbook (arquivo é como se fosse um livro)
    wsBrasileirao = wbBrasileirao['Sheet1'] #como se estivesse escolhendo a página de um livro, no caso uma aba do excel
    matBrasileirao = list(wsBrasileirao)    #para trabalharmos com matrizes ao invés de 'celulas'

    partidas = []

    subtitulo = ["id"]
    qtdeSubtitulos = 36
    
    for i in range (qtdeSubtitulos):
        subtitulo.append(matBrasileirao[0][i+1].value)
    
    for j in range(1, len(matBrasileirao)): #percorre a coluna, começamos do 1 porque não queremos a primeira linha
        linha = []  #armazena uma linha, que será posteriormente um elemento da nossa lista, criando uma tupla
        jogo = {}
        for k in range(qtdeSubtitulos):
            jogo[subtitulo[k]] = matBrasileirao[j][k].value # Adding new key-value pair

        linha.append(jogo)
        partidas.append(jogo)
        ##print(jogo)

    return partidas

def maisGols():

    partidas_f = open('./arquivos/partidas.bin', 'rb')
    times_f = open('./arquivos/times.bin', 'rb')

    #abre os arquivos de indices de cada arquivo
    indices_times_f = open('./indices_arquivos/indices_times.bin', 'rb')
    indices_partidas_f = open('./indices_arquivos/indices_partidas.bin', 'rb')

    indices_times = pickle.load(indices_times_f)

    indices_partida = pickle.load(indices_partidas_f)
  
   
    gols = []
    golsTupla = []
    for i in range(len(indices_times)):
        gols.append(0)
        times_f.seek(indices_times[i]["indice"])
        times = (pickle.load(times_f))  

        for j in range(len(indices_partida)):
            partidas_f.seek(indices_partida[j]["indice"])
            partida = pickle.load(partidas_f)

            if times["id"] == partida["time_man"]:
                if partida["gols_man"] is None:
                    partida["gols_man"] == 0
                else:
                    gols[i] += partida["gols_man"]
            
            if times["id"] == partida["time_vis"]:
                if partida["gols_vis"] is None:
                    partida["gols_vis"] == 0
                else:
                    gols[i] += partida["gols_vis"]
                    
    golsAndIndices = [(valor, indice) for indice, valor in enumerate(gols)]

    # Classificar a lista de tuplas com base nos valores (ordenados em ordem decrescente)
    golsOrdenados = sorted(golsAndIndices, reverse=True)

    # Pegar os 10 primeiros elementos da lista ordenada (ou seja, os 10 maiores valores) e suas posições correspondentes
    #top10 = golsOrdenados[:10]

    # Imprimir os 10 maiores valores e suas posições
    for valor, posicao in golsOrdenados:
        times_f.seek(indices_times[posicao]["indice"])
        time = pickle.load(times_f)
        #print(f"Gols: {valor}, Time: {time['nome']}")

        nova_tupla_gols = (time['nome'], valor,)
        golsTupla.append(nova_tupla_gols)

    with open("./rankings/gols.bin", "wb") as arquivo:
        pickle.dump(golsTupla,arquivo)

    #print(golsTupla)
      
    
def maiorPublico():

    partidas_f = open('./arquivos/partidas.bin', 'rb')
    locais_f = open('./arquivos/locais.bin', 'rb')
    times_f = open('./arquivos/times.bin', 'rb')

    indices_times_f = open('./indices_arquivos/indices_times.bin', 'rb')
    indices_partidas_f = open('./indices_arquivos/indices_partidas.bin', 'rb')
    indices_locais_f = open('./indices_arquivos/indices_locais.bin', 'rb')

    indices_locais = pickle.load(indices_locais_f)
    indices_partida = pickle.load(indices_partidas_f)
    indices_times = pickle.load(indices_times_f)

    publico = []
    estadios = []
    publicoTupla = []
    for i in range(len(indices_partida)):
        publico.append(0)
        estadios.append(0)
        partidas_f.seek(indices_partida[i]["indice"])
        partida = pickle.load(partidas_f)

        if partida["publico"] is None:
            partida["publico"] = 0
        else:
            publico[i] = partida["publico"]
            estadios[i] = partida["estadio"]

    for i in range(len(indices_locais)):
        for j in range(len(estadios)):
            locais_f.seek(indices_locais[i]["indice"])
            local = pickle.load(locais_f)
        
            if local["id"] == estadios[j]:
                estadios[j] = local["estadio"]

    #print(estadios)

    publicoAndIndices = [(valor, indice) for indice, valor in enumerate(publico)]

    publicoSorted = sorted(publicoAndIndices, reverse = True)

    top10 = publicoSorted[:10]

    for valor, posicao in top10:
        partidas_f.seek(indices_partida[posicao]["indice"])
        partida = pickle.load(partidas_f)

        nova_tupla_publico = (partida["id"])
        publicoTupla.append(nova_tupla_publico)

    with open("./rankings/publico.bin", "wb") as arquivo:
        pickle.dump(publicoTupla,arquivo)

    #print(publicoTupla)

        #print(f"Publico: {valor}, Partida: {time_man['nome']} vs {time_vis['nome']}")

def mediaIdade():

    partidas_f = open('./arquivos/partidas.bin', 'rb')
    times_f = open('./arquivos/times.bin', 'rb')

    # abre os arquivos de indices de cada arquivo
    indices_times_f = open('./indices_arquivos/indices_times.bin', 'rb')
    indices_partidas_f = open('./indices_arquivos/indices_partidas.bin', 'rb')

    indices_times = pickle.load(indices_times_f)
    indices_partida = pickle.load(indices_partidas_f)

    idade_media_man = []
    idade_media_vis = []
    data = []

    for i in range(len(indices_partida)):
        idade_media_man.append(0)
        idade_media_vis.append(0)
        data.append(0)

        partidas_f.seek(indices_partida[i]["indice"])
        partida = pickle.load(partidas_f)

        if partida["idade_media_titular_man"] is None:
            partida["idade_media_titular_man"] = 0
        else:
            idade_media_man[i] = partida["idade_media_titular_man"]

        if partida["idade_media_titular_vis"] is None:
            partida["idade_media_titular_vis"] = 0
        else:
            idade_media_vis[i] = partida["idade_media_titular_vis"]

        data[i] = partida["data"]

    IdadeManAndIndices = [(valor, indice, "m") for indice, valor in enumerate(idade_media_man)]
    IdadeVisAndIndices = [(valor, indice, "v") for indice, valor in enumerate(idade_media_vis)]

    #para pegar o rankings dos times mais velhos
    idadeManSorted = sorted(IdadeManAndIndices, reverse=True)
    idadeVisSorted = sorted(IdadeVisAndIndices, reverse=True)

    topFinal = idadeManSorted + idadeVisSorted
    topFinal50 = topFinal[:50]
    topFinalSorted = sorted(topFinal50, reverse=True)


    #para pegar o ranking de times mais novos
    idadeManRevSorted = sorted(IdadeManAndIndices, reverse=False)
    idadeVisRevSorted = sorted(IdadeVisAndIndices, reverse=False)

    topFinalRev = idadeManRevSorted + idadeVisRevSorted
    
    topFinalRev = tuple([tupla for tupla in topFinalRev if tupla[0] != 0])

    topFinalRev50 = topFinalRev[:50] 
            
    topFinalSortedRev = sorted(topFinalRev50, reverse=False)

    #print(topFinalSortedRev)
    
    #print(topFinalRev)
    #top10 = top20[:10]

    ano_ja_ta = set() # conjunto para armazenar os times que já apareceram na lista

    #coloca na tupla para maiores idades
    idadeTupla = []
    for valor, posicao, flag in topFinalSorted:
        partidas_f.seek(indices_partida[posicao]["indice"])
        partida = pickle.load(partidas_f)

        if flag == "m":
            times_f.seek(indices_times[partida['time_man']]["indice"])
            time = pickle.load(times_f)

        if flag == "v":
            times_f.seek(indices_times[partida['time_vis']]["indice"])
            time = pickle.load(times_f)

        if partida['ano_campeonato'] in ano_ja_ta: # verifica se o time já está na lista
            continue

        nova_tupla_idade = (time['nome'], valor, data[posicao])
        idadeTupla.append(nova_tupla_idade)  

        #print(f"Idade Média: {valor}, Time: {time['nome']}, Ano:{ano[posicao]}")
        ano_ja_ta.add(partida['ano_campeonato']) # adiciona o time ao conjunto

    with open("./rankings/media_idade_maior.bin", "wb") as arquivo:
        pickle.dump(idadeTupla,arquivo)

    #print(idadeTupla)

    #coloca na tupla para menores idades
    idadeTuplaRev = []
    ano_ja_ta_rev = set()

    for valor, posicao, flag in topFinalSortedRev:
        partidas_f.seek(indices_partida[posicao]["indice"])
        partida = pickle.load(partidas_f)

        if flag == "m":
            times_f.seek(indices_times[partida['time_man']]["indice"])
            time = pickle.load(times_f)

        if flag == "v":
            times_f.seek(indices_times[partida['time_vis']]["indice"])
            time = pickle.load(times_f)

        if partida['ano_campeonato'] in ano_ja_ta_rev: # verifica se o time já está na lista
            continue

        nova_tupla_idade_rev = (time['nome'], valor, data[posicao])
        idadeTuplaRev.append(nova_tupla_idade_rev)  

        #print(f"Idade Média: {valor}, Time: {time['nome']}, Ano:{ano[posicao]}")
        ano_ja_ta_rev.add(partida['ano_campeonato']) # adiciona o time ao conjunto

    with open("./rankings/media_idade_menor.bin", "wb") as arquivo:
        pickle.dump(idadeTuplaRev,arquivo)

    #print(idadeTuplaRev)

def vitoriasDerrotas():

    partidas_f = open('./arquivos/partidas.bin', 'rb')
    times_f = open('./arquivos/times.bin', 'rb')

    #abre os arquivos de indices de cada arquivo
    indices_times_f = open('./indices_arquivos/indices_times.bin', 'rb')
    indices_partidas_f = open('./indices_arquivos/indices_partidas.bin', 'rb')

    indices_times = pickle.load(indices_times_f)
    indices_partida = pickle.load(indices_partidas_f)

    vitorias = []
    derrotas = []

    for i in range(len(indices_times)):
        vitorias.append(0)
        derrotas.append(0)
        times_f.seek(indices_times[i]["indice"])
        time = (pickle.load(times_f))
        for j in range(len(indices_partida)):

            partidas_f.seek(indices_partida[j]["indice"])
            partida = pickle.load(partidas_f)

            if partida["gols_vis"] is None:
                partida["gols_vis"] = 0

            if partida["gols_man"] is None:
                partida["gols_man"] = 0

            if partida["time_man"] == time["id"]:
                if partida["gols_man"] > partida["gols_vis"]:
                    vitorias[i] += 1
                elif partida["gols_man"] < partida["gols_vis"]:
                    derrotas[i] += 1
            
            if partida["time_vis"] == time["id"]:
                if partida["gols_vis"] > partida["gols_man"]:
                    vitorias[i] += 1
                elif partida["gols_vis"] < partida["gols_man"]:
                    derrotas[i] += 1

    vitAndIndices = [(valor, indice) for indice, valor in enumerate(vitorias)]
    # Classificar a lista de tuplas com base nos valores (ordenados em ordem decrescente)
    vitOrdenadas = sorted(vitAndIndices, reverse=True)
    # Pegar os 10 primeiros elementos da lista ordenada (ou seja, os 10 maiores valores) e suas posições correspondentes
    #top10Vit = vitOrdenadas[:10]

    derAndIndices = [(valor, indice) for indice, valor in enumerate(derrotas)]
    derOrdenadas = sorted(derAndIndices, reverse=True)
    #top10Der = derOrdenadas[:10]

    vitoriasTupla = []
    derrotasTupla = []
    # Imprimir os 10 maiores valores e suas posições
    for valor, posicao in vitOrdenadas:
        times_f.seek(indices_times[posicao]["indice"])
        time = pickle.load(times_f)
        #print(f"Vitórias: {valor}, Time: {time['nome']}")
        
        nova_tupla_vit = (time['nome'], valor)
        vitoriasTupla.append(nova_tupla_vit)  

    for valor, posicao in derOrdenadas:
        times_f.seek(indices_times[posicao]["indice"])
        time = pickle.load(times_f)

        nova_tupla_der = (time['nome'], valor)
        derrotasTupla.append(nova_tupla_der)

    with open("./rankings/vitorias.bin", "wb") as arquivo:
        pickle.dump(vitoriasTupla,arquivo)

    with open("./rankings/derrotas.bin", "wb") as arquivo:
        pickle.dump(derrotasTupla,arquivo)
    
    #print(vitoriasTupla)
    #print(derrotasTupla)

def precoTimes():
     
    partidas_f = open('./arquivos/partidas.bin', 'rb')
    times_f = open('./arquivos/times.bin', 'rb')

    #abre os arquivos de indices de cada arquivo
    indices_times_f = open('./indices_arquivos/indices_times.bin', 'rb')
    indices_partidas_f = open('./indices_arquivos/indices_partidas.bin', 'rb')

    indices_times = pickle.load(indices_times_f)
    indices_partida = pickle.load(indices_partidas_f)

    precosMan = []
    precosVis = []
    ano = []
    for i in range(len(indices_partida)):
        partidas_f.seek(indices_partida[i]["indice"])
        partida = pickle.load(partidas_f)
        precosMan.append(0)
        precosVis.append(0)
        ano.append(0)
        for j in range(len(indices_times)):
            times_f.seek(indices_times[j]["indice"])
            time = (pickle.load(times_f))

            if partida["time_man"] == time["id"]:
                if partida["valor_equipe_titular_man"] is None:
                    partida["valor_equipe_titular_man"] = 0
                else:
                    precosMan[i] = partida["valor_equipe_titular_man"]

            if partida["time_vis"] == time["id"]:
                if partida["valor_equipe_titular_vis"] is None:
                    partida["valor_equipe_titular_vis"] = 0
                else:
                    precosVis[i] = partida["valor_equipe_titular_vis"]

            ano[i] = partida["ano_campeonato"]

    valorManAndIndices = [(valor, indice, "m") for indice, valor in enumerate(precosMan)]
    valorVisAndIndices = [(valor, indice, "v") for indice, valor in enumerate(precosVis)]

    valorManSorted = sorted(valorManAndIndices, reverse=True)
    valorVisSorted = sorted(valorVisAndIndices, reverse=True)

    topFinal = valorManSorted + valorVisSorted
    topFinal300 = topFinal[:300]
    topFinalSorted = sorted(topFinal300, reverse=True)

    #para pegar o ranking de times mais baratos
    valorManRevAndIndices = sorted(valorManAndIndices, reverse=False)
    valorVisRevAndIndices = sorted(valorVisAndIndices, reverse=False)

    finalRevPreco = valorManRevAndIndices + valorVisRevAndIndices
    
    finalRevPreco = tuple([tupla for tupla in finalRevPreco if tupla[0] != 0])

    finalRevPreco300 = finalRevPreco[:300] 
            
    topFinalSortedRev = sorted(finalRevPreco300, reverse=False)

    maisCarosTupla = []
    ano_ja_foi = set()

    manOuVis = ""
    manOuVisBar = ""
    for valor, posicao, flag in topFinalSorted:
        partidas_f.seek(indices_partida[posicao]["indice"])
        partida = pickle.load(partidas_f)

        if flag == "m":
            manOuVis = "m"

        if flag == "v":
            manOuVis = "v"

        if partida['ano_campeonato'] in ano_ja_foi: # verifica se o time já está na lista
            continue

        nova_tupla_preco = (partida["id"], manOuVis)
        maisCarosTupla.append(nova_tupla_preco)  

        #print(f"Idade Média: {valor}, Time: {time['nome']}, Ano:{ano[posicao]}")
        ano_ja_foi.add(partida['ano_campeonato']) # adiciona o time ao conjunto

    with open("./rankings/mais_caros.bin", "wb") as arquivo:
        pickle.dump(maisCarosTupla,arquivo)

    maisBaratosTupla = []
    ano_ja_ta_rev = set()

    for valor, posicao, flag in topFinalSortedRev:
        partidas_f.seek(indices_partida[posicao]["indice"])
        partida = pickle.load(partidas_f)

        if flag == "m":
            manOuVisBar = "m"

        if flag == "v":
            manOuVisBar = "v"

        if partida['ano_campeonato'] in ano_ja_ta_rev: # verifica se o time já está na lista
            continue

        nova_tupla_idade_rev = (partida["id"], manOuVisBar)
        maisBaratosTupla.append(nova_tupla_idade_rev)  

        #print(f"Idade Média: {valor}, Time: {time['nome']}, Ano:{ano[posicao]}")
        ano_ja_ta_rev.add(partida['ano_campeonato']) # adiciona o time ao conjunto

    with open("./rankings/mais_baratos.bin", "wb") as arquivo:
        pickle.dump(maisBaratosTupla,arquivo)

    #print(precosVis)
    #print(maisCarosTupla)
    #print(maisBaratosTupla)
    #print(ano)

precoTimes()
#vitoriasDerrotas()
#mediaIdade()
#maisGols()
#maiorPublico()