import getPartida as fun
import pickle
import time

print("Histórico de um time!");
time_1 = input("Time: ");
# time_1 = "Grêmio";
print("Escolha um período. Vão de 2003 até 2020.");
ano_inicio = input("Início: ");
# ano_inicio = "2003";
ano_fim = input("Fim: ");
# ano_fim = "2020";

inicio = time.time()
# print(time_1 + ", "+ time_2);
temPartidas = True
vitorias_1 = 0
empates = 0
derrotas_1 = 0
qtde_jogos = 0
gols_pro = 0
gols_contra = 0
mais_gols = [{"id": 0, "total_gols": 0, "gols_man": 0, "gols_vis": 0}]
maior_goleada = [{"id": 0, "diff": 0, "gols_man": 0, "gols_vis": 0}]
maior_publico_1 = {"id": 0, "publico": 0}
indices_time1 = None;

with open("./indices_arquivos/indices_times_invertidos.bin", "rb") as arquivo:
    indices_time1 = pickle.load(arquivo)

times_invertidos = open("./arquivos_invertidos/times_invertidos.bin", "rb")
times_invertidos.seek(indices_time1[time_1])
ids_time_1 = pickle.load(times_invertidos)["ids"]
i=0
try:
    times_invertidos.seek(indices_time1[time_1])
    ids_time_1 = pickle.load(times_invertidos)["ids"]
    for i in range(len(ids_time_1)):
        partida = fun.getPartida(ids_time_1[i]);
        i+=1
        ##só como mandante por enquanto
        if (partida["ano_campeonato"] >= int(ano_inicio)) and (partida["ano_campeonato"] <= int(ano_fim)):
            if (partida["time_man"] == time_1):
                if(partida["gols_man"] > partida["gols_vis"]):
                    vitorias_1+=1
                elif(partida["gols_man"] < partida["gols_vis"]):
                    derrotas_1+=1
                else:
                    empates+=1

                total_gols = partida["gols_man"]+partida["gols_vis"]
                if total_gols > mais_gols[0]["total_gols"]:
                    mais_gols = [{
                        "id": partida["id"], 
                        "total_gols": total_gols, 
                    }]
                elif total_gols == mais_gols[0]["total_gols"]:
                    mais_gols.append({
                        "id": partida["id"], 
                        "total_gols": total_gols, 
                    })

                gols_pro += partida["gols_man"]
                gols_contra += partida["gols_vis"]

                diff = abs(partida["gols_man"]-partida["gols_vis"])
                if diff > maior_goleada[0]["diff"]:
                    maior_goleada = [{
                        "id": partida["id"],
                        "diff": diff,
                    }]
                elif diff == maior_goleada[0]["diff"]:
                    maior_goleada.append({
                        "id": partida["id"],
                        "diff": diff,
                    })
                    
                maior_publico = partida["publico"]
                if maior_publico == None:
                    maior_publico = 0

                if maior_publico > maior_publico_1["publico"]:
                    maior_publico_1 = {"id": partida["id"], "publico": maior_publico}
                elif maior_publico == maior_publico_1["publico"]:
                    if maior_publico == None:
                        maior_publico = 0;
                    maior_publico_1 = {"id": partida["id"], "publico": maior_publico}

            elif (partida["time_vis"] == time_1):
                if(partida["gols_man"] > partida["gols_vis"]):
                    derrotas_1+=1
                elif(partida["gols_man"] < partida["gols_vis"]):
                    vitorias_1+=1
                else:
                    empates+=1

                total_gols = partida["gols_man"]+partida["gols_vis"]
                if total_gols > mais_gols[0]["total_gols"]:
                    mais_gols = [{
                        "id": partida["id"], 
                        "total_gols": total_gols, 
                    }]
                elif total_gols == mais_gols[0]["total_gols"]:
                    mais_gols.append({
                        "id": partida["id"], 
                        "total_gols": total_gols, 
                    })

                gols_pro += partida["gols_man"]
                gols_contra += partida["gols_vis"]

                diff = abs(partida["gols_man"]-partida["gols_vis"])
                if diff > maior_goleada[0]["diff"]:
                    maior_goleada = [{
                        "id": partida["id"],
                        "diff": diff,
                    }]
                elif diff == maior_goleada[0]["diff"]:
                    maior_goleada.append({
                        "id": partida["id"],
                        "diff": diff,
                    })
except IndexError as e:
        print("Fim das partidas.");
        print(e);
        temPartidas = False;
fim = time.time()

tempo_exec = fim - inicio;

print("Analisando entre "+ano_inicio+" e "+ano_fim)
print("Tempo empregado: ",tempo_exec,"s")
print("Vitórias: ",vitorias_1)
print("Empates: ",empates)
print("Derrotas:",derrotas_1)
print("Gols feitos:",gols_pro)
print("Gols sofridos:",gols_contra)
print("__________________________________________")
print("Partida com mais gols:")
for partida in mais_gols:
    partida_mais_gols = fun.getPartida(partida["id"]);
    print("------Data: " + partida_mais_gols["data"].strftime('%d/%m/%Y'))
    print("------Qtde Gols: " + str(partida["total_gols"]))
    print("------Gols do " + partida_mais_gols["time_man"] + ": " + str(partida_mais_gols["gols_man"]))
    print("------Gols do "+ partida_mais_gols["time_vis"] + ": " + str(partida_mais_gols["gols_vis"]))
    print("---")
print("__________________________________________")
print("Partida com a maior goleada (maior diferença de gols):")
for partida in maior_goleada:
    partida_goleada = fun.getPartida(partida["id"]);
    print("------Data: " + partida_goleada["data"].strftime('%d/%m/%Y'))
    print("------Gols do " + partida_goleada["time_man"] + ": " + str(partida_goleada["gols_man"]))
    print("------Gols do "+ partida_goleada["time_vis"] + ": " + str(partida_goleada["gols_vis"]))
    print("---")
print("__________________________________________")
print("Partida com mais público para o " + time_1 + ":")
partida_publico = fun.getPartida(maior_publico_1["id"]);
print("------"+partida_publico["time_man"]+" x "+partida_publico["time_vis"])
print("------Data: " + partida_publico["data"].strftime('%d/%m/%Y'))
print("------Estádio: " + partida_publico["estadio"]+"")
print("------Publico: " + str(partida_publico["publico"]))
def printaPartida(partida):
    for key in partida.keys():
        if (key == "data"):
            print(key+": "+ partida[key].strftime('%d/%m/%Y')+"")
        elif (partida[key] != None and key != "id"):
            print(key+": "+str(partida[key])+"")
        

print("Deseja ver mais partidas do "+time_1+"?");
option = input("S/N: ")
j=0
qtde_partidas = input("Quantas partidas deseja ver por vez? ")
modo = input("Da mais recente para mais antiga (D) ou da mais antiga para a mais atual (C)? ")
##tratar 0
while option.upper() == "S":
    if modo.upper() == "C":
        for i in range(int(qtde_partidas)):
            if (i+j) <= len(ids_time_1):
                partida = fun.getPartida(ids_time_1[i+j])
                printaPartida(partida)
                print("_________________________________")
            else:
                print("Sem mais partidas")
                break;
    elif modo.upper() == "D":
        for i in range(int(qtde_partidas)):
            if (i+j) <= len(ids_time_1):
                partida = fun.getPartida(ids_time_1[len(ids_time_1)-i-j-1])
                printaPartida(partida)
                print("_________________________________")
            else:
                print("Sem mais partidas")
                break;
    else:
        break;
    print("Deseja continuar?")
    option = input("S/N: ")
    if option.upper() == "S" : 
        j+=int(qtde_partidas)
