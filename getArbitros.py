import pickle 

with open('./arquivos/arbitros.bin', 'rb') as arbitros_f:
    with open('./indices_arquivos/indices_arbitros.bin', 'rb') as indices_arbitros_f:
        # carrega o conteúdo do arquivo para a memória
        indices = pickle.load(indices_arbitros_f);
        arbitros_f.seek(indices[4]["indice"])
        arbitro = pickle.load(arbitros_f)
        print(arbitro)