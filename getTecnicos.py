import pickle 

with open("tecnicos.bin", "rb") as arquivo:
    tecnicos = pickle.load(arquivo)

print(tecnicos)