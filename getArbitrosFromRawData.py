import functions as fun    #importa arquivo com todas as funções necessarias
import pickle

partidas = []
arbitros = []
id_local = 0;

partidas = fun.getPartidas()

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

indices = []; ##aqui entraria a árvore e salvaríamos aqui os indices
with open("./arquivos/arbitros.bin", "wb") as arquivo:
    for arbitro in arbitros:
        indices.append({"indice":arquivo.tell()})
        pickle.dump(arbitro ,arquivo)

with open("./indices_arquivos/indices_arbitros.bin", "wb") as arquivo:
    pickle.dump(indices,arquivo)