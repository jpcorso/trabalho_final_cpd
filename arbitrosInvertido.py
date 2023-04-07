import getPartida as fun
import pickle

indices_partidas_f = open('./indices_arquivos/indices_partidas.bin', 'rb')
indices_partida = pickle.load(indices_partidas_f)

arbitros_f = open('./arquivos/arbitros.bin', 'rb')
#arbitros = pickle.load(arbitros_f)

indices_arbitros_f = open('./indices_arquivos/indices_arbitros.bin', 'rb')
indices_arbitros = pickle.load(indices_arbitros_f)

partidas_f = open('./arquivos/partidas.bin', 'rb')

arbitrosInvertido = []

for i in range(len(indices_arbitros)):
    arbitros_f.seek(indices_arbitros[i]["indice"])
    arbitros = pickle.load(arbitros_f)
    arbitro_dict = {"nome": arbitros["nome"], "id_arb": arbitros["id"], "ids": []}
    arbitrosInvertido.append(arbitro_dict)

    partidas_f.seek(0)
    
    for j in range(len(indices_partida)):
        partida = (pickle.load(partidas_f))
        if partida["arbitro"] == arbitro_dict["id_arb"]:
            arbitro_dict["ids"].append(partida["id"])
            continue

        arbitro_ids = [a["id_arb"] for a in arbitrosInvertido]

        if partida["arbitro"] not in arbitro_ids:
            arbitro_dict = {"nome": arbitros["nome"], "id_arb": partida["arbitro"], "ids": [partida["id"]]}
            arbitrosInvertido.append(arbitro_dict)
        else:
            index = arbitro_ids.index(partida["arbitro"])
            arbitrosInvertido[index]["ids"].append(partida["id"])

for arbitro in arbitrosInvertido:
    del arbitro['id_arb']

    #for arbitro in arbitrosInvertido:
        #arbitro["id_arb"] = 

with open("./arquivos_invertidos/arbitros_invertidos.bin", "wb") as arquivo:
    pickle.dump(arbitrosInvertido,arquivo)


print(arbitrosInvertido)