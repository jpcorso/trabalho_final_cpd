import pickle 

with open("locais.bin", "rb") as arquivo:
    locais = pickle.load(arquivo)

print(locais)