import functions as fun    #importa arquivo com todas as funções necessarias
import pickle

times = []

id_times = 0;

partidas = fun.getPartidas()

for partida in partidas:
    ja_tem = False
    for time in times:

        if partida["time_man"] == time["nome"]:
            ja_tem = True

        if(ja_tem):
            break

    if (not ja_tem):
        times.append({"id": id_times, "nome": partida["time_man"]})
        id_times += 1


##with open("times.bin", "wb") as arquivo:
##    pickle.dump(times, arquivo)
        
print(times)

indices = []; ##aqui entraria a árvore e salvaríamos aqui os indices
with open("./arquivos/times.bin", "wb") as arquivo:
    i=0;
    for time in times:
        indices.append({"indice":arquivo.tell()})
        pickle.dump(time ,arquivo)
        i+=1

with open("./indices_arquivos/indices_times.bin", "wb") as arquivo:
    pickle.dump(indices,arquivo)