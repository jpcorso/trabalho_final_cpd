import functions as fun    #importa arquivo com todas as funções necessarias
import pickle

tecnicos = []

id_tecnicos = 0;

partidas = fun.getPartidas()

for partida in partidas:
    ja_tem = False
    for tecnico in tecnicos:

        if partida["tecnico_man"] == tecnico["nome"]:
            ja_tem = True

        if(ja_tem):
            break

    if (not ja_tem):
        tecnicos.append({"id": id_tecnicos, "nome": partida["tecnico_man"]})
        id_tecnicos += 1
        
print(tecnicos)

indices = []; ##aqui entraria a árvore e salvaríamos aqui os indices
with open("./arquivos/tecnicos.bin", "wb") as arquivo:
    i=0;
    for tecnico in tecnicos:
        indices.append({"indice":arquivo.tell()})
        pickle.dump(tecnico ,arquivo)
        i+=1

with open("./indices_arquivos/indices_tecnicos.bin", "wb") as arquivo:
    pickle.dump(indices,arquivo)