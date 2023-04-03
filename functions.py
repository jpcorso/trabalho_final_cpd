import openpyxl

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

