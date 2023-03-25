import pickle 

with open("locais.pkl", "rb") as arquivo:
    locais = pickle.load(arquivo)

print(locais)