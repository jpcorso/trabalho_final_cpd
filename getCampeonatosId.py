import getPartida as fun
import pickle 

def createFile():
    temPartidas = True
    i=0;
    ids_campeonatos = {}
    while temPartidas:
        try:
            partida = fun.getPartida(i);
            ano = partida["ano_campeonato"]
            if ano not in ids_campeonatos:
                ids_campeonatos[ano] = partida["id"]
            i+=1;
        except IndexError as e:
            print("Sem mais partidas.");
            temPartidas = False;
    
    with open('./indices_arquivos/ano_campeonatos.bin', 'wb') as f:
        pickle.dump(ids_campeonatos,f)