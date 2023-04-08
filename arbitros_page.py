
import pickle 
import getPartida as fun

indices_arbitros_f = open('./indices_arquivos/indices_arbitros_invertidos.bin', 'rb')
indices_arbitros = pickle.load(indices_arbitros_f)

arbitros_f = open('./arquivos_invertidos/arbitros_invertidos.bin', 'rb')
arbitros = pickle.load(arbitros_f)

nomeArbitro = input("Pesquise um árbitro... ")

arbitros_f.seek(indices_arbitros[nomeArbitro])
arbitro_ids = pickle.load(arbitros_f)["ids"]
#print(arbitro_ids)

partidas = numFaltas = noneTypeFaltas = 0

print("\nPartidas apitadas:")

for i in arbitro_ids:
    
    partida = fun.getPartida(i)

    if partida["faltas_man"] or partida["faltas_vis"] is not None:
        numFaltas += partida["faltas_man"]
        numFaltas += partida["faltas_vis"]
    else:
        del partida["faltas_man"]
        del partida["faltas_vis"]
        noneTypeFaltas += 1

    print(f'{partida["time_man"]} vs {partida["time_vis"]}')

if len(arbitro_ids) - noneTypeFaltas > 0:
    mediaFaltas = numFaltas/(len(arbitro_ids) - noneTypeFaltas)
else:
    mediaFaltas = str("Este árbitro não possue dados de faltas.")

print(f"\nNúmero de partidas: {len(arbitro_ids)}")
print(f"Média de faltas por jogo: {mediaFaltas}")

numPartidas = 0
pontosGanhos = pontosDisputados = 0
while True:
    continuar = input("Você deseja ver o aproveitamento desse árbitro com algum time? (s/n): ")
    if continuar == 'n' or continuar == 'N':
        break
    elif continuar == 's' or continuar =='S':
        # continuar com o loop
        nomeTime = input("Nome do time: ")
        for i in arbitro_ids:

            partida = fun.getPartida(i)
            if partida["time_vis"] == nomeTime:
                pontosDisputados += 3
                if partida["gols_vis"] > partida["gols_man"]:
                    pontosGanhos += 3
                elif partida["gols_vis"] == partida["gols_man"]:
                    pontosGanhos += 1
            
            if partida["time_man"] == nomeTime:
                pontosDisputados += 3
                if partida["gols_man"] > partida["gols_vis"]:
                    pontosGanhos += 3
                elif partida["gols_man"] == partida["gols_vis"]:
                    pontosGanhos += 1

        if pontosDisputados != 0:
            aproveitamento = (pontosGanhos/pontosDisputados)*100
            aproveitamento = round(aproveitamento,2)

            print(f"Aproveitamento do {nomeTime} com o árbitro {nomeArbitro}: {aproveitamento}%")
        else:
            print(f"Sem dados de partidas do {nomeArbitro} com o {nomeTime}")
        pontosGanhos = pontosDisputados = 0
        
        continue
    else:
        print("Opção inválida. Tente novamente.")


    

    
    
    
