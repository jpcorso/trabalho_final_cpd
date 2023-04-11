import getPartida as fun
import pickle
import trieTree as trieTree
i=1
tem_partida=True
arbitros=[]
primeira_partida = fun.getPartida(0);
if (primeira_partida["arbitro"] == '' or primeira_partida["arbitro"] == None):
    primeiro_tecnico = 'Sem arbitro';
else:
    primeiro_tecnico = fun.getPartida(0)["arbitro"];

arbitros.append({"nome": primeiro_tecnico, "ids":[0]})
while tem_partida:
    try:
        partida = fun.getPartida(i);
        if (partida["arbitro"] == '' or partida["arbitro"] == None):
            partida["arbitro"] = 'Sem arbitro'
        arbitro_partida = partida["arbitro"]
        ja_tem_arb = False;
        j=0
        for arbitro in arbitros:
            if(arbitro_partida == arbitro["nome"]):
                arbitros[j]["ids"].append(i)
                ja_tem_arb = True;
                break;
            j+=1
        if(not ja_tem_arb):
            arbitros.append({"nome": partida["arbitro"], "ids":[i]})
        print(i)
        i+=1    
    except IndexError as e:
        print("Fim das partidas.")
        tem_partida = False

arvore_trie = trieTree.Trie()

with open("./arquivos_invertidos/arbitros_invertidos.bin", "wb") as arquivo:
    for arbitro in arbitros:
        print(arbitro)
        arvore_trie.inserir_time(arbitro["nome"].title(),arquivo.tell())
        pickle.dump(arbitro, arquivo)

with open("./indices_arquivos/indices_arbitros_invertidos.bin", "wb") as arquivo:
    pickle.dump(arvore_trie,arquivo)
