import getPartida as fun
import pickle
import trieTree as trie
i=1
tem_partida=True
times=[]
times.append({"nome": fun.getPartida(0)["time_man"], "ids":[0]})
times.append({"nome": fun.getPartida(0)["time_vis"], "ids":[0]})
while tem_partida:
    try:
        partida = fun.getPartida(i);
        time_man = partida["time_man"]
        ja_tem_man = False;
        time_vis = partida["time_vis"]
        ja_tem_vis = False;
        j=0
        for time in times:
            if(time_man == time["nome"]):
                times[j]["ids"].append(i)
                ja_tem_man = True;
                break;
            j+=1
        if(not ja_tem_man):
            times.append({"nome": fun.getPartida(i)["time_man"], "ids":[i]})

        k=0
        for time in times:
            if(time_vis == time["nome"]):
                times[k]["ids"].append(i)
                ja_tem_vis = True;
                break;
            k+=1
        if(not ja_tem_vis):
            times.append({"nome": fun.getPartida(i)["time_vis"], "ids":[i]})      
        i+=1
    except IndexError as e:
        print("Fim das partidas.")
        tem_partida = False


arvore_trie = trie.Trie()

with open("./arquivos_invertidos/times_invertidos.bin", "wb") as arquivo:
    i=0;
    for time in times:
        arvore_trie.inserir_time(time["nome"].title(),arquivo.tell())
        pickle.dump(time, arquivo)
        i+=1

with open("./indices_arquivos/indices_times_invertidos.bin", "wb") as arquivo:
    pickle.dump(arvore_trie,arquivo)

