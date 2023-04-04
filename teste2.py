import getPartida as fun
import pickle
import time

time_1 = input("Primeiro time: ");
time_2 = input("Segundo time: ");
print("Escolha um período. Vão de 2003 até 2020.");
ano_inicio = input("Início: ");
ano_fim= input("Fim: ");

inicio = time.time()
# print(time_1 + ", "+ time_2);
temPartidas = True
partidas_times = []
vitorias_1 = 0
vitorias_2 = 0
empates = 0
mais_gols = {"id": 0, "total_gols": 0, "gols_man": 0, "gols_vis": 0}
maior_goleada = {"id": 0, "diff": 0,"gols_man": 0, "gols_vis": 0}
maior_publico_1 = {"id": 0, "publico": 0}
maior_publico_2 = {"id": 0, "publico": 0}
jogo_mais_falta = {"id": 0, "faltas": 0} ## fazer depois
indices_time1 = None;

with open("./indices_arquivos/indices_times_invertidos.bin", "rb") as arquivo:
    indices_time1 = pickle.load(arquivo)

times_invertidos = open("./arquivos_invertidos/times_invertidos.bin", "rb")

i=0
try:
    times_invertidos.seek(indices_time1[time_1])
    ids_time_1 = pickle.load(times_invertidos)["ids"]
    for i in range(len(ids_time_1)):
        partida = fun.getPartida(ids_time_1[i]);
        i+=1
        if (partida["ano_campeonato"] >= int(ano_inicio)) and (partida["ano_campeonato"] <= int(ano_fim)):
            if (partida["time_man"] == time_1 and partida["time_vis"] == time_2):
                if(partida["gols_man"] > partida["gols_vis"]):
                    vitorias_1+=1
                elif(partida["gols_man"] < partida["gols_vis"]):
                    vitorias_2+=1
                else:
                    empates+=1

                total_gols = partida["gols_man"]+partida["gols_vis"];
                if total_gols > mais_gols["total_gols"]:
                    mais_gols = {
                        "id": partida["id"], 
                        "total_gols": total_gols, 
                        "gols_man": partida["gols_man"], 
                        "gols_vis": partida["gols_vis"], 
                    }

                diff = abs(partida["gols_man"]-partida["gols_vis"]);
                if diff > maior_goleada["diff"]:
                    maior_goleada = {
                        "id": partida["id"],
                        "diff": diff,
                        "gols_man": partida["gols_man"], 
                        "gols_vis": partida["gols_vis"], 
                    }
                maior_publico = partida["publico"]
                if maior_publico == None:
                    maior_publico = 0

                if maior_publico > maior_publico_1["publico"]:
                    maior_publico_1 = {"id": partida["id"], "publico": maior_publico}
            elif (partida["time_man"] == time_2 and partida["time_vis"] == time_1):
                if(partida["gols_man"] > partida["gols_vis"]):
                    vitorias_2+=1
                elif(partida["gols_man"] < partida["gols_vis"]):
                    vitorias_1+=1
                else:
                    empates+=1

                total_gols = partida["gols_man"]+partida["gols_vis"];
                if total_gols > mais_gols["total_gols"]:
                    mais_gols = {
                        "id": partida["id"], 
                        "total_gols": total_gols, 
                        "gols_man": partida["gols_man"], 
                        "gols_vis": partida["gols_vis"], 
                    }

                diff = abs(partida["gols_man"]-partida["gols_vis"]);
                if diff > maior_goleada["diff"]:
                    maior_goleada = {
                        "id": partida["id"],
                        "diff": diff,
                        "gols_man": partida["gols_man"], 
                        "gols_vis": partida["gols_vis"], 
                    }

                maior_publico = partida["publico"]
                if maior_publico == None:
                    maior_publico = 0

                if maior_publico > maior_publico_2["publico"]:
                    maior_publico_2 = {"id": partida["id"], "publico": maior_publico}
        else:
            break
except IndexError as e:
        print("Fim das partidas.");
        print(e);
        temPartidas = False;
except TypeError as e:
    print("probleminha, ein ",i);
    i+=1
fim = time.time()

tempo_exec = fim - inicio;

print("Analisando entre "+ano_inicio+" e "+ano_fim)
print("Tempo empregado: ",tempo_exec,"s")
print("Vitórias do " + time_1 + ": ",vitorias_1)
print("Vitórias do "+ time_2 + ":",vitorias_2)
print("Empates: ",empates)
print("Partida com mais gols:")
print("------Data: " + fun.getPartida(mais_gols["id"])["data"].strftime('%d/%m/%Y'))
print("------Qtde Gols: " + str(mais_gols["total_gols"]))
print("------Gols do " + fun.getPartida(mais_gols["id"])["time_man"] + ": " + str(mais_gols["gols_man"]))
print("------Gols do "+ fun.getPartida(mais_gols["id"])["time_vis"] + ": " + str(mais_gols["gols_vis"]))
print("Partida com a maior goleada:")
print("------Data: " + fun.getPartida(maior_goleada["id"])["data"].strftime('%d/%m/%Y'))
print("------Gols do " + fun.getPartida(maior_goleada["id"])["time_man"] + ": " + str(maior_goleada["gols_man"]))
print("------Gols do "+ fun.getPartida(maior_goleada["id"])["time_vis"] + ": " + str(maior_goleada["gols_vis"]))
print("Partida com mais público para o " + time_1 + ":")
print("------Data: " + fun.getPartida(maior_publico_1["id"])["data"].strftime('%d/%m/%Y'))
print("------Publico: " + str(maior_publico_1["publico"]))
print("Partida com mais público para o "+ time_2 + ":")
print("------Data: " + fun.getPartida(maior_publico_2["id"])["data"].strftime('%d/%m/%Y'))
print("------Publico: " + str(maior_publico_2["publico"]))

print("Fim do loop.")