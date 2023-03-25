import pickle 

with open("arbitros.pkl", "rb") as arquivo:
    arbitros = pickle.load(arquivo)

print(arbitros)