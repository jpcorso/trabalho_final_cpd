import pickle 

with open("arbitros.bin", "rb") as arquivo:
    arbitros = pickle.load(arquivo)

print(arbitros)