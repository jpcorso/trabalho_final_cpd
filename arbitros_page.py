
import pickle 

indices_arbitros_f = open('./indices_arquivos/indices_arbitros.bin', 'rb')
indices_arbitros = pickle.load(indices_arbitros_f)

arbitros_f = open('./arquivos_invertidos/arbitros_invertidos.bin', 'rb')
arbitros = pickle.load(arbitros_f)

nomeArbitro = input("Pesquise um árbitro... ")

partidas = 0
for i in range(len(indices_arbitros)):
    arbitros_f.seek(indices_arbitros[i]["indice"])
    arbitros = pickle.load(arbitros_f)
    
    if nomeArbitro == arbitros[i]["nome"]:
        partidas +=1

#print(partidas)