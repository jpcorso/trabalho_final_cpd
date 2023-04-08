import getPartida as fun
import pickle
import time

<<<<<<< HEAD
def teamHistory():
    print("Histórico de um time!");
    time_1 = input("Time: ");
    print("Escolha um período. Vão de 2003 até 2020.");
    ano_inicio = input("Início: ");
    ano_fim= input("Fim: ");

    inicio = time.time()
    # print(time_1 + ", "+ time_2);
    temPartidas = True
    vitorias_1 = 0
    empates = 0
    derrotas_1 = 0
    qtde_jogos = 0
    gols_pro = 0
    gols_contra = 0
    mais_gols = {"id": 0, "total_gols": 0, "gols_man": 0, "gols_vis": 0}
    maior_goleada = {"id": 0, "diff": 0,"gols_man": 0, "gols_vis": 0}
    maior_publico_1 = {"id": 0, "publico": 0}
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
                if (partida["time_man"] == time_1):
                    if(partida["gols_man"] > partida["gols_vis"]):
                        vitorias_1+=1
                    elif(partida["gols_man"] < partida["gols_vis"]):
                        derrotas_1+=1
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

                    gols_pro += partida["gols_man"]
                    gols_contra += partida["gols_vis"]

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
                elif (partida["time_vis"] == time_1):
                    if(partida["gols_man"] > partida["gols_vis"]):
                        derrotas_1+=1
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

                    gols_pro += partida["gols_vis"]
                    gols_contra += partida["gols_man"]

                    diff = abs(partida["gols_man"]-partida["gols_vis"]);
                    if diff > maior_goleada["diff"]:
                        maior_goleada = {
                            "id": partida["id"],
                            "diff": diff,
                            "gols_man": partida["gols_man"], 
                            "gols_vis": partida["gols_vis"], 
                        }
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
    print("Vitórias: ",vitorias_1)
    print("Empates: ",empates)
    print("Derrotas:",derrotas_1)
    print("Gols feitos:",gols_pro)
    print("Gols sofridos:",gols_contra)
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

    print("Fim do loop.")
=======
def printaPartida(partida):
    dictionary = {
        "horario" : "Horário do jogo:",
        "ano_campeonato" : "BRASILEIRÃO",
        "rodada" : "Rodada:",
        "estadio" : "Estádio:",
        "arbitro" : "Árbitro:",
        "publico" : "Público:",
        "publico_max" : "Público máximo:",
        "time_man" : "Time mandante:",
        "time_vis" : "Time visitante:",
        "tecnico_man" : "Técnico mandante:",
        "tecnico_vis" : "Técnico visitante:",
        "colocacao_man" : "Colocação (MANDANTE):",
        "colocacao_vis" : "Colocação (VISITANTE):",
        "valor_equipe_titular_man": "Valor do time titular (MANDANTE): R$",
        "valor_equipe_titular_vis": "Valor do time titular (VISITANTE): R$",
        "idade_media_titular_man": "Idade média do time titular (MANDANTE):",
        "idade_media_titular_vis": "Idade média do time titular (VISITANTE):",
        "gols_man": "Gols (MANDANTE):",
        "gols_vis": "Gols (VISITANTE):",
        "gols_1_tempo_man": "Gols do mandante (1° tempo):",
        "gols_1_tempo_vis": "Gols do visitante (1° tempo):",
        "escanteios_man": "Escanteios (MANDANTE):",
        "escanteios_vis": "Escanteios (VISITANTE):",    
        "faltas_man": "Faltas (MANDANTE):",
        "faltas_vis": "Faltas (VISITANTE):",       
        "chutes_bola_parada_man": "Chutes bola parada (MANDANTE):",
        "chutes_bola_parada_vis": "Chutes bola parada (VISITANTE):",  
        "defesas_man": "Defesas (MANDANTE):",
        "defesas_vis": "Defesas (VISITANTE):",    
        "impedimentos_man": "Impedimentos (MANDANTE):",
        "impedimentos_vis": "Impedimentos (VISITANTE):",   
        "chutes_man": "Chutes (MANDANTE):",
        "chutes_vis": "Chutes (VISITANTE):", 
        "chutes_fora_man": "Chutes fora do gol (MANDANTE):",
        "chutes_fora_vis": "Chutes fora do gol (Visitante):",  
    }
    for key in partida.keys():
        if (key == "data"):
            print("Data do jogo: "+ partida[key].strftime('%d/%m/%Y')+"")
        elif (partida[key] != None and key != "id"):
            print(dictionary[key]+" "+str(partida[key])+"")

def history():
    doFunction = "S"
    while doFunction.upper() == "S":
        print("Histórico de um time!");

        indices_time1 = None;
        with open("./indices_arquivos/indices_times_invertidos.bin", "rb") as arquivo:
            indices_time1 = pickle.load(arquivo)

        times_invertidos = open("./arquivos_invertidos/times_invertidos.bin", "rb")
        timeExiste = False
        while not timeExiste:
            time_1 = input("Time: ");
            try:
                times_invertidos.seek(indices_time1[time_1])
                timeExiste = True
            except KeyError as e:
                print("Não foi encontrado na base de dados. Tente outro ou verifique o nome digitado (case sensitive).");

        ids_time_1 = pickle.load(times_invertidos)["ids"]
        print("Escolha um período. Vão de 2003 até 2020.");
        periodoValido = False
        ano_inicio= 0;
        ano_fim=0;
        while not periodoValido:
            ano_inicio = int(input("Início: "));
            ano_fim = int(input("Fim: "));
            if(ano_fim < ano_inicio or ano_fim > 2020 or ano_inicio < 2003):
                print("Período inválido. Escolha outro período válido.")
            else:
                periodoValido = True

        inicio = time.time()

        temPartidas = True
        vitorias_1 = 0
        empates = 0
        derrotas_1 = 0
        gols_pro = 0
        gols_contra = 0
        mais_gols = [{"id": 0, "total_gols": 0}]
        maior_goleada = [{"id": 0, "diff": 0}]
        maior_publico_1 = {"id": 0, "publico": 0}

        i=0
        indice_final_loop=0

        try:
            times_invertidos.seek(indices_time1[time_1])
            ids_time_1 = pickle.load(times_invertidos)["ids"]
            primeiraPartida = False
            for i in range(len(ids_time_1)):
                partida = fun.getPartida(ids_time_1[i]);
                if (partida["ano_campeonato"] >= int(ano_inicio)) and (partida["ano_campeonato"] <= int(ano_fim)):
                    if (primeiraPartida == False):
                        indice_inicial_arq = i
                        primeiraPartida = True

                    if (partida["time_man"] == time_1):
                        if(partida["gols_man"] > partida["gols_vis"]):
                            vitorias_1+=1
                        elif(partida["gols_man"] < partida["gols_vis"]):
                            derrotas_1+=1
                        else:
                            empates+=1

                        gols_pro+=partida["gols_man"]
                        gols_contra+=partida["gols_vis"]

                        maior_publico = partida["publico"]
                        if maior_publico == None:
                            maior_publico = 0

                        if maior_publico >= maior_publico_1["publico"]:
                            maior_publico_1 = {"id": partida["id"], "publico": maior_publico}
                    elif (partida["time_vis"] == time_1):
                        if(partida["gols_man"] > partida["gols_vis"]):
                            derrotas_1+=1
                        elif(partida["gols_man"] < partida["gols_vis"]):
                            vitorias_1+=1
                        else:
                            empates+=1 

                        gols_pro+=partida["gols_vis"]
                        gols_contra+=partida["gols_man"] 
                
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
                        
                    if (partida["ano_campeonato"] == 2020 and partida["rodada"] == 38):
                        print("Fim das partidas.");
                        indice_final_loop = i;
                        break;  
                elif(partida["ano_campeonato"] > int(ano_fim)): 
                    print("Fim das partidas.");
                    indice_final_loop = i-1;
                    break;
                i+=1
        except IndexError as e:
                print("Fim da análise das partidas partidas.\n");
                print(e);
                temPartidas = False;
        fim = time.time()

        tempo_exec = fim - inicio;

        print(f"_____________{time_1}_____________")
        print(f"Analisando entre {ano_inicio} e {ano_fim}")
        print(f"Tempo empregado: {tempo_exec}s")
        print(f"Vitórias do {time_1}: {vitorias_1}")
        print(f"Empates: {empates}")
        print("__________________________________________")
        print("Partida com mais gols:")
        print(f"-------------Qtde Gols: {mais_gols[0]['total_gols']}-------------")
        for partida in mais_gols:
            partida_mais_gols = fun.getPartida(partida["id"]);
            print(f"------Data: {partida_mais_gols['data'].strftime('%d/%m/%Y')}")
            print(f"------Placar: {partida_mais_gols['time_man']} {str(partida_mais_gols['gols_man'])} x {str(partida_mais_gols['gols_vis'])} {partida_mais_gols['time_vis']}")
            print(f"---")
        print("__________________________________________")
        print("Partida com a maior goleada (maior diferença de gols):")
        for partida in maior_goleada:
            partida_goleada = fun.getPartida(partida["id"]);
            print(f"------Data: {partida_goleada['data'].strftime('%d/%m/%Y')}")
            print(f"------Placar: {partida_goleada['time_man']} {str(partida_goleada['gols_man'])} x {str(partida_goleada['gols_vis'])} {partida_goleada['time_vis']}")
            print(f"---")
        print("__________________________________________")
        print(f"Partida com mais público para o {time_1}:")
        partida_publico = fun.getPartida(maior_publico_1["id"]);
        print(f"------"+partida_publico["time_man"]+" "+str(partida_publico["gols_man"])+" x "+str(partida_publico["gols_vis"])+" "+partida_publico["time_vis"])
        print(f"------Data: " + partida_publico["data"].strftime('%d/%m/%Y'))
        print(f"------Estádio: " + partida_publico["estadio"]+"")
        print(f"------Publico: " + str(partida_publico["publico"]))
        print("__________________________________________")
                
        print(f"Deseja ver as partidas de {time_1} no periodo?")
        option = input("S/N: ")
        qtde_partidas = input("Quantas partidas deseja ver por vez? ")
        modo = input("Da ultima partida até a primeira (D) ou da primeira partida até a ultima (C)? ")
        i=indice_inicial_arq
        while option.upper() == "S" and temPartidas:
            temPartidas = True;
            indice_inicial_loop=i
            if modo.upper() == "C":
                while temPartidas and (i <= (int(qtde_partidas)-1+indice_inicial_loop)):
                    if i <= (len(ids_time_1)-1):
                        partida = fun.getPartida(ids_time_1[i])
                        if (partida["ano_campeonato"] >= int(ano_inicio)) and (partida["ano_campeonato"] <= int(ano_fim)):
                            printaPartida(partida)
                            print("_________________________________")
                        elif (partida["ano_campeonato"] > int(ano_fim)):
                            print("Sem mais partidas")
                            temPartidas = False
                            break;
                        i+=1
                    else:
                        print("Sem mais partidas")
                        temPartidas = False
                        break;
            elif modo.upper() == "D":
                i = indice_final_loop;
                while temPartidas and (i > (indice_final_loop-int(qtde_partidas))):
                    if i >= 0:
                        partida = fun.getPartida(ids_time_1[i])
                        if (partida["ano_campeonato"] >= int(ano_inicio)) and (partida["ano_campeonato"] <= int(ano_fim)):
                            printaPartida(partida)
                            print("_________________________________")
                        elif (partida["ano_campeonato"] < int(ano_inicio)):
                            print("Sem mais partidas")
                            temPartidas = False
                            break;
                        i-=1
                    else:
                        print("Sem mais partidas")
                        temPartidas = False
                        break;
            else:
                print("Saindo da função...")
                break;
            if (temPartidas):
                print("Deseja continuar?")
                option = input("S/N: ")
                if option.upper() == "S" : 
                    indice_inicial_loop = i;
                    indice_final_loop = i;

        print("Deseja escolher outro time para analisar?")
        doFunction = input("S/N: ")

history()
>>>>>>> b3b7c05cc738691674d1ec913636f9fb1067199d
