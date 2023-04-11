import pickle 

with open('./arquivos/times.bin', 'rb') as times_f:
    with open('./indices_arquivos/indices_times.bin', 'rb') as indices_times_f:
        # carrega o conteúdo do arquivo para a memória
        indices = pickle.load(indices_times_f);
        times_f.seek(indices[36]["indice"])
        time = pickle.load(times_f)
        print(time)