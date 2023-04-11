import functions as fun    #importa arquivo com todas as funções necessarias
import json
import pandas as pd
import pickle 

locais = []

partidas = fun.getPartidas()

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

indices = []; ##aqui entraria a árvore e salvaríamos aqui os indices
with open("./arquivos/locais.bin", "wb") as arquivo:
    for local in locais:
        indices.append({"indice":arquivo.tell()})
        pickle.dump(local ,arquivo)

with open("./indices_arquivos/indices_locais.bin", "wb") as arquivo:
    pickle.dump(indices,arquivo)

