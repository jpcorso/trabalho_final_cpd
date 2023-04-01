import functions as fun    #importa arquivo com todas as funções necessarias
import openpyxl
import pickle
import struct
brasileirao = 'brasileiraoSerieA.xlsx'

wbBrasileirao = openpyxl.load_workbook(brasileirao) #coloca a variavel em workbook (arquivo é como se fosse um livro)
wsBrasileirao = wbBrasileirao['Sheet1'] #como se estivesse escolhendo a página de um livro, no caso uma aba do excel
matBrasileirao = list(wsBrasileirao)    #para trabalharmos com matrizes ao invés de 'celulas'

partidas = []

fun.colocaTupla(matBrasileirao, partidas)

##id 7029

fopenqSEEK = 32

# abre o arquivo no modo de leitura binária
with open('partidas.bin', 'rb') as f:
    # carrega o conteúdo do arquivo para a memória
    f.seek(7000)

    ##conteudo = pickle.load(f)

    linha = f.readline()

    data_linha = struct.unpack('utf-8', linha)

    linha = linha.decode('utf-8')
    print(linha)
# Traceback (most recent call last):
#   File "getPartida.py", line 25, in <module>
#     linha = linha.decode('utf-8')
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0x94 in position 6: invalid start byte


# percorre os elementos do conteúdo
##for elemento in conteudo:
##    print(elemento)