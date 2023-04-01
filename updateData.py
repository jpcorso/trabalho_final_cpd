import scripts.functions as fun    #importa arquivo com todas as funções necessarias
import pickle

partidas = fun.getPartidas();

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

indices = []; ##aqui entraria a árvore e salvaríamos aqui os indices
with open("partidas.bin", "wb") as arquivo:
    i=0;
    for partida in partidas:
        indices.append({"indice":arquivo.tell()})
        pickle.dump(partida ,arquivo)
        i+=1

with open("indices_partidas.bin", "wb") as arquivo:
    pickle.dump(indices,arquivo)

with open("indices_partidas.bin", "rb") as arquivo:
    teste = pickle.load(arquivo)