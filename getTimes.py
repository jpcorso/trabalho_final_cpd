import pickle 

with open("times.bin", "rb") as arquivo:
    times = pickle.load(arquivo)

print(times)