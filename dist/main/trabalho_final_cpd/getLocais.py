import pickle
# abre o arquivo no modo de leitura binária
with open('./arquivos/partidas.bin', 'rb') as partidas_f:
    with open('./indices_arquivos/indices_partidas.bin', 'rb') as indices_partidas_f:
        # carrega o conteúdo do arquivo para a memória
        indices = pickle.load(indices_partidas_f);
        partidas_f.seek(indices[7029]["indice"])
        partida = pickle.load(partidas_f)
        print(partida)
