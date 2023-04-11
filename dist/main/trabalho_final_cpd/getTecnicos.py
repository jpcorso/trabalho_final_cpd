import pickle 

with open('./arquivos/tecnicos.bin', 'rb') as tecnicos_f:
    with open('./indices_arquivos/indices_tecnicos.bin', 'rb') as indices_tecnicos_f:
        # carrega o conteúdo do arquivo para a memória
        indices = pickle.load(indices_tecnicos_f);
        tecnicos_f.seek(indices[3]["indice"])
        tecnicos = pickle.load(tecnicos_f)
        print(tecnicos)