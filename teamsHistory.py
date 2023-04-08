import getPartida as fun
import pickle
import time

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

def indice_do_time(time,indices_times):
    timeExiste = indices_times.pesquisa_time(time.title())
    if (not timeExiste):
        print("Não foi encontrado na base de dados. Cuide com os acentos.")
        for i in range(len(time)):
            sugestoes = indices_times.todos_os_times_com(time[:len(time)-i].title())
            if len(sugestoes) > 0:
                print("Talvez você queira pesquisar:")
                for sugestao in sugestoes:
                    print(f"-{sugestao[0]}")
                print('')
                break;
        return False;
    else:
        return timeExiste[1]

def history():
    doFunction = "S"
    while doFunction.upper() == "S":
        print("Histórico entre dois times!");

        indices_times = None;
        with open("./indices_arquivos/indices_times_invertidos.bin", "rb") as arquivo:
            indices_times = pickle.load(arquivo)
            
            indice_time_1 = 0;
            while not indice_time_1:
                time_1 = input("\nPrimeiro time: ");
                indice_time_1 = indice_do_time(time_1, indices_times)

            indice_time_2 = 0;
            while not indice_time_2:
                time_2 = input("Segundo time: ");
                indice_time_2 = indice_do_time(time_2, indices_times)

        print("Escolha um período. Vão de 2003 até 2020.");

        periodoValido = False;
        ano_inicio= 0;
        ano_fim=0;
        inicio_definido = False;
        while not periodoValido:
            if (not inicio_definido):
                ano_inicio = int(input("Início: "));
                if (ano_inicio < 2003):
                    print("Dados do campeonato disponíveis a partir de 2003.")
                else:
                    inicio_definido = True;
                    continue
            else:
                ano_fim = int(input("Fim: "));
                if (ano_fim > 2020):
                    print("Dados do campeonato disponíveis até o de 2020.");
                elif(ano_fim < ano_inicio):
                    print("Período inválido. Escolha outro período válido.")
                else:
                    periodoValido = True

        inicio = time.time()

        temPartidas = True
        vitorias_1 = 0
        vitorias_2 = 0
        empates = 0
        mais_gols = [{"id": 0, "total_gols": 0}]
        maior_goleada = [{"id": 0, "diff": 0}]
        maior_publico_1 = {"id": 0, "publico": 0}
        maior_publico_2 = {"id": 0, "publico": 0}
        indices_partidas = []
        i=0
        indice_final_loop=0

        try:
            with open("./arquivos_invertidos/times_invertidos.bin", "rb") as times_invertidos:
                times_invertidos.seek(indice_time_1)
                registro_1 = pickle.load(times_invertidos)

                times_invertidos.seek(indice_time_2)
                registro_2 = pickle.load(times_invertidos)
            ids_time_1 = registro_1["ids"]
            ids_time_2 = registro_2["ids"]
            nome_time_1 = registro_1["nome"]
            nome_time_2 = registro_2["nome"]

            indices_partidas = [value for value in ids_time_1 if value in ids_time_2] ;
            for i in range(len(indices_partidas)):
                partida = fun.getPartida(indices_partidas[i]);
                if (partida["ano_campeonato"] >= int(ano_inicio)) and (partida["ano_campeonato"] <= int(ano_fim)):
                    if (partida["time_man"].title() == time_1.title()):
                        if(partida["gols_man"] > partida["gols_vis"]):
                            vitorias_1+=1
                        elif(partida["gols_man"] < partida["gols_vis"]):
                            vitorias_2+=1
                        else:
                            empates+=1

                        maior_publico = partida["publico"]
                        if maior_publico == None:
                            maior_publico = 0

                        if maior_publico >= maior_publico_1["publico"]:
                            maior_publico_1 = {"id": partida["id"], "publico": maior_publico}
                    elif (partida["time_vis"].title() == time_1.title()):
                        if(partida["gols_man"] > partida["gols_vis"]):
                            vitorias_2+=1
                        elif(partida["gols_man"] < partida["gols_vis"]):
                            vitorias_1+=1
                        else:
                            empates+=1 
                        
                        maior_publico = partida["publico"]
                        if maior_publico == None:
                            maior_publico = 0

                        if maior_publico >= maior_publico_2["publico"]:
                            maior_publico_2 = {"id": partida["id"], "publico": maior_publico}
                
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
                        break;  
                elif(partida["ano_campeonato"] > int(ano_fim)): 
                    print("Fim das partidas.");
                    break;
                i+=1
        except IndexError as e:
                print("Fim das partidas.");
                print(e);
                temPartidas = False;
        fim = time.time()

        tempo_exec = fim - inicio;

        print(f"{nome_time_1} x {nome_time_2}")
        print(f"Analisando entre {ano_inicio} e {ano_fim}")
        print(f"Tempo empregado: {tempo_exec}s")
        print(f"Vitórias do {nome_time_1}: {vitorias_1}")
        print(f"Vitórias do {nome_time_2}: {vitorias_2}")
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
        print(f"Partida com mais público para o {nome_time_1}:")
        partida_publico = fun.getPartida(maior_publico_1["id"]);
        print(f"------"+partida_publico["time_man"]+" "+str(partida_publico["gols_man"])+" x "+str(partida_publico["gols_vis"])+" "+partida_publico["time_vis"])
        print(f"------Data: " + partida_publico["data"].strftime('%d/%m/%Y'))
        print(f"------Estádio: " + partida_publico["estadio"]+"")
        print(f"------Publico: " + str(partida_publico["publico"]))
        print("__________________________________________")
        print(f"Partida com mais público para o {nome_time_2}:")
        partida_publico = fun.getPartida(maior_publico_2["id"]);
        print(f"------"+partida_publico["time_man"]+" "+str(partida_publico["gols_man"])+" x "+str(partida_publico["gols_vis"])+" "+partida_publico["time_vis"])
        print(f"------Data: " + partida_publico["data"].strftime('%d/%m/%Y'))
        print(f"------Estádio: " + partida_publico["estadio"]+"")
        print(f"------Publico: " + str(partida_publico["publico"]))
                
        print(f"Deseja ver as partidas de {nome_time_1} e {nome_time_2} no periodo?")
        option = input("S/N: ")
        if (option.upper() == "S"):
            qtde_partidas = int(input("Quantas partidas deseja ver por vez? "))
            modo = input("Do ultimo confronto até o primeiro (D) ou do primeiro confronto até o ultimo (C)? ")   
            
            while option.upper() == "S" and temPartidas:
                if modo.upper() == "C" or modo.upper() == "D":
                    if modo.upper() == "D":
                        sorted(indices_partidas, reverse=True)
                    i=0
                    for i in range(qtde_partidas):
                        if ((i+j) < len(indices_partidas)):
                            partida = fun.getPartida(indices_partidas[i+j])
                            printaPartida(partida)
                            print("------------------")
                        else: 
                            temPartidas = False;
                            break;
                else:
                    print("Saindo da função...")
                    break;
                
                if (temPartidas):
                    print("Deseja continuar?")
                    option = input("S/N: ")
                    if option.upper() == "S" : 
                        j+=qtde_partidas
                else:
                    print("Fim das partidas.")

        print("Deseja escolher outros times para analisar?")
        doFunction = input("S/N: ")

history()