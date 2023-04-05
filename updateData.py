import functions as fun    #importa arquivo com todas as funções necessarias
import pickle

partidas = fun.getPartidas();

indices_arbitros = []
with open("./indices_arquivos/indices_arbitros.bin", "rb") as arquivo:
    indices_arbitros = pickle.load(arquivo)
    arquivo.close()
    
indices_locais = []
with open("./indices_arquivos/indices_locais.bin", "rb") as arquivo:
    indices_locais = pickle.load(arquivo)
    arquivo.close()

indices_tecnicos = []
with open("./indices_arquivos/indices_tecnicos.bin", "rb") as arquivo:
    indices_tecnicos = pickle.load(arquivo)
    arquivo.close()

indices_times = []
with open("./indices_arquivos/indices_times.bin", "rb") as arquivo:
    indices_times = pickle.load(arquivo)
    arquivo.close()

partidas_f = open('./arquivos/partidas.bin', 'rb')
times_f = open('./arquivos/times.bin', 'rb')
arbitros_f = open('./arquivos/arbitros.bin', 'rb')
locais_f = open('./arquivos/locais.bin', 'rb')
tecnicos_f = open('./arquivos/tecnicos.bin', 'rb')

for partida in partidas:
    for i in range(len(indices_locais)):
        locais_f.seek(indices_locais[i]["indice"])
        local = pickle.load(locais_f)
        if local["estadio"] == partida["estadio"]:
            partida["estadio"] = local["id"]
            partida["publico_max"] = local["id"]
            break
    
    for i in range(len(indices_arbitros)):
        arbitros_f.seek(indices_arbitros[i]["indice"])
        arbitro = pickle.load(arbitros_f)
        if arbitro["nome"] == partida["arbitro"]:
            partida["arbitro"] = arbitro["id"]
            break

    for i in range(len(indices_tecnicos)):
        tecnicos_f.seek(indices_tecnicos[i]["indice"])
        tecnico = pickle.load(tecnicos_f)
        if partida["tecnico_man"] == tecnico["nome"]:
            partida["tecnico_man"] = tecnico["id"]
            break

    for i in range(len(indices_tecnicos)):
        tecnicos_f.seek(indices_tecnicos[i]["indice"])
        tecnico = pickle.load(tecnicos_f)
        if partida["tecnico_vis"] == tecnico["nome"]:
            partida["tecnico_vis"] = tecnico["id"]
            break  

    for i in range(len(indices_times)):
        times_f.seek(indices_times[i]["indice"])
        time = pickle.load(times_f)
        if partida["time_man"] == time["nome"]:
            partida["time_man"] = time["id"]
            break

    for i in range(len(indices_times)):
        times_f.seek(indices_times[i]["indice"])
        time = pickle.load(times_f)
        if partida["time_vis"] == time["nome"]:
            partida["time_vis"] = time["id"]
            break

indices = []; ##aqui entraria a árvore e salvaríamos aqui os indices
with open("./arquivos/partidas.bin", "wb") as arquivo:
    i=0;
    for partida in partidas:
        indices.append({"indice":arquivo.tell()})
        pickle.dump(partida ,arquivo)
        i+=1

with open("./indices_arquivos/indices_partidas.bin", "wb") as arquivo:
    pickle.dump(indices,arquivo)

with open("./indices_arquivos/indices_partidas.bin", "rb") as arquivo:
    teste = pickle.load(arquivo)