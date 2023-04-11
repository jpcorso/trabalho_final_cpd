import pickle

indices_times = []
with open("./indices_arquivos/indices_partidas.bin", "rb") as arquivo:
    print(pickle.load(arquivo))
    arquivo.close()

print(indices_times)