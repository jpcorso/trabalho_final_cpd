import pickle

def getPartida(id):
    #abre os arquivos binários com nossos dados
    partidas_f = open('./arquivos/partidas.bin', 'rb')
    times_f = open('./arquivos/times.bin', 'rb')
    arbitros_f = open('./arquivos/arbitros.bin', 'rb')
    locais_f = open('./arquivos/locais.bin', 'rb')
    tecnicos_f = open('./arquivos/tecnicos.bin', 'rb')

    #abre os arquivos de indices de cada arquivo
    indices_partidas_f = open('./indices_arquivos/indices_partidas.bin', 'rb')
    indices_times_f = open('./indices_arquivos/indices_times.bin', 'rb')
    indices_arbitros_f = open('./indices_arquivos/indices_arbitros.bin', 'rb')
    indices_locais_f = open('./indices_arquivos/indices_locais.bin', 'rb')
    indices_tecnicos_f = open('./indices_arquivos/indices_tecnicos.bin', 'rb')

    indices_partida = pickle.load(indices_partidas_f)
    partidas_f.seek(indices_partida[id]["indice"])
    partida = pickle.load(partidas_f)

    indices_arbitros = pickle.load(indices_arbitros_f)
    arbitros_f.seek(indices_arbitros[partida["arbitro"]]["indice"])
    arbitro = pickle.load(arbitros_f)

    partida["arbitro"] = arbitro["nome"]

    indices_locais = pickle.load(indices_locais_f)
    locais_f.seek(indices_locais[partida["estadio"]]["indice"])
    local = pickle.load(locais_f)

    partida["estadio"] = local["estadio"]
    partida["publico_max"] = local["publico_max"] 

    ############################################################

    indices_times = pickle.load(indices_times_f)
    times_f.seek(indices_times[partida["time_man"]]["indice"])
    times = pickle.load(times_f)
    partida["time_man"] = times["nome"]

    times_f.seek(indices_times[partida["time_vis"]]["indice"])
    times = pickle.load(times_f)
    partida["time_vis"] = times["nome"]

    indices_tecnicos = pickle.load(indices_tecnicos_f)
    tecnicos_f.seek(indices_tecnicos[partida["tecnico_man"]]["indice"])
    tecnicos = pickle.load(tecnicos_f)
    partida["tecnico_man"] = tecnicos["nome"]

    tecnicos_f.seek(indices_tecnicos[partida["tecnico_vis"]]["indice"])
    tecnicos = pickle.load(tecnicos_f)
    partida["tecnico_vis"] = tecnicos["nome"]

    #fecha os arquivos
    partidas_f.close()
    times_f.close()
    arbitros_f.close()
    locais_f.close()
    tecnicos_f.close()
    indices_partidas_f.close()
    indices_times_f.close()
    indices_arbitros_f.close()
    indices_locais_f.close()
    indices_tecnicos_f.close()

    return partida