import functions as fun    #importa arquivo com todas as funções necessarias
import pickle

tecnicos = []

id_tecnicos = 0;

partidas = fun.getPartidas()

for partida in partidas:
    ja_tem_man = False
    ja_tem_vis = False
    for tecnico in tecnicos:
        if partida["tecnico_man"] == tecnico["nome"]:
            ja_tem_man = True

        if partida["tecnico_vis"] == tecnico["nome"]:
            ja_tem_vis = True

        if(ja_tem_man and ja_tem_vis):
            break
    
    if (not ja_tem_man):
        tecnicos.append({"id": id_tecnicos, "nome": partida["tecnico_man"]})
        id_tecnicos += 1

    if (not ja_tem_vis):
        tecnicos.append({"id": id_tecnicos, "nome": partida["tecnico_vis"]})
        id_tecnicos += 1
        
indices = []; ##aqui entraria a árvore e salvaríamos aqui os indices
with open("./arquivos/tecnicos.bin", "wb") as arquivo:
    for tecnico in tecnicos:
        indices.append({"indice":arquivo.tell()})
        pickle.dump(tecnico ,arquivo)

with open("./indices_arquivos/indices_tecnicos.bin", "wb") as arquivo:
    pickle.dump(indices,arquivo)