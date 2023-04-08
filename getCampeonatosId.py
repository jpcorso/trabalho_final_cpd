import getPartida as fun
import pickle 

def createFile():
    temPartidas = True
    i=0;
    ids_campeonatos = {}
    ano_atual = 2003;
    while temPartidas:
        try:
            partida = fun.getPartida(i);
            ano = partida["ano_campeonato"]
            if ano not in ids_campeonatos:
                ids_campeonatos[ano] = [partida["id"]]
            if(ano_atual != ano):
                ids_campeonatos[ano_atual].append(partida["id"])
                ano_atual = ano
            i+=1;
        except IndexError as e:
            print("Sem mais partidas.");
            ids_campeonatos[ano_atual].append(i-1)
            temPartidas = False;
    
    print(ids_campeonatos)

    with open('./indices_arquivos/indices_ano_campeonatos.bin', 'wb') as f:
        pickle.dump(ids_campeonatos,f)

createFile()