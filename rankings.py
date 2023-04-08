import pickle
import getPartida as fun

def rankings():
    print("Rankings do Brasileirão do período de 2003 até 2020...\n")

    with open('./rankings/publico.bin', 'rb') as publico_file:
        # carrega o conteúdo do arquivo para a memória
        publicos = pickle.load(publico_file);
        print("\nRanking públicos:")
        print("*************************************")
        for publico in publicos:
            partida = fun.getPartida(publico)
            print(f'\n{partida["time_man"]} {partida["gols_man"]} x {partida["gols_vis"]} {partida["time_vis"]}')
            print(f'Público: {partida["publico"]}')
            print(f'Estádio: {partida["estadio"]}')
            print(f'Data: {partida["data"].strftime("%d/%m/%Y")}\n')
            print("-------------------------------------")

    with open('./rankings/gols.bin', 'rb') as gols_file:
        # carrega o conteúdo do arquivo para a memória
        gols = pickle.load(gols_file);
        print("\nRanking gols:")
        print("*************************************")
        count = 1 # inicializa a variável contadora
        for time, gol in gols:
            if count <= 10: # verifica se a contagem ainda não chegou a 10
                print(f'{count}º: {time}')
                print(f'{gol} gols\n')
                print("-------------------------------------")
                count += 1 # incrementa a contagem
            else:
                break # interrompe o loop quando a contagem chega a 10

    with open('./rankings/vitorias.bin', 'rb') as vitorias_file:
        # carrega o conteúdo do arquivo para a memória
        vitorias = pickle.load(vitorias_file);
        print("\nRanking vitorias:")
        print("*************************************")
        count = 1
        for time, vitoria in vitorias:
            if count <= 10:
                print(f'{count}º: {time}')
                print(f'{vitoria} vitórias')
                print("-------------------------------------")
                count += 1
            else:
                break

    with open('./rankings/derrotas.bin', 'rb') as derrotas_file:
        # carrega o conteúdo do arquivo para a memória
        derrotas = pickle.load(derrotas_file);
        print("\nRanking derrotas:")
        print("*************************************")
        count = 1
        for time, derrota in derrotas:
            if count <= 10:
                print(f'{count}º: {time}')
                print(f'{derrota} derrotas\n')
                print("-------------------------------------")
                count += 1
            else:
                break

    with open('./rankings/media_idade_maior.bin', 'rb') as media_idade_maior_file:
        # carrega o conteúdo do arquivo para a memória
        media_idade_maior = pickle.load(media_idade_maior_file);
        print("\nTimes mais velhos:")
        print("*************************************")
        count = 1
        for time, media, data in media_idade_maior:
            if count <= 10:
                print(f'{count}º: {time}')
                print(f'Data: {data.strftime("%d/%m/%Y")}')
                print(f'{media} anos\n')
                print("-------------------------------------")
                count += 1
            else:
                break

    with open('./rankings/media_idade_menor.bin', 'rb') as media_idade_menor_file:
        # carrega o conteúdo do arquivo para a memória
        media_idade_menor = pickle.load(media_idade_menor_file);
        print("\nTimes mais jovens:\n")
        print("*************************************")
        count = 1
        for time, media, data in media_idade_menor:
            if count <= 10:
                print(f'{count}º: {time}')
                print(f'Data: {data.strftime("%d/%m/%Y")}')
                print(f'{media} anos\n')
                print("-------------------------------------")
                count += 1
            else:
                break

    with open('./rankings/mais_caros.bin', 'rb') as mais_caros_file:
        # carrega o conteúdo do arquivo para a memória
        mais_caros = pickle.load(mais_caros_file);
        print("\nTimes mais caros:")
        count = 1
        for time, flag in mais_caros:
            if count <= 10:
                partida = fun.getPartida(time)
                if flag == "m":
                    time_caro = partida["time_man"]
                    valor = partida["valor_equipe_titular_man"]
                    valorAdversario = partida["valor_equipe_titular_vis"]
                if flag == "v":
                    time_caro = partida["time_vis"]
                    valor = partida["valor_equipe_titular_vis"]
                    valorAdversario = partida["valor_equipe_titular_man"]

                valor = "{:,d}".format(valor).replace(",", ".")
                valorAdversario = "{:,d}".format(valorAdversario).replace(",", ".")

                print(f'\n{count}º-Time: {time_caro}, Valor: R${valor}')
                print("-------------------------------------")
                print(f'{partida["time_man"]} {partida["gols_man"]} x {partida["gols_vis"]} {partida["time_vis"]}')
                print(f'Valor da equipe Adversária: R${valorAdversario}')
                print(f'Data: {partida["data"].strftime("%d/%m/%Y")}\n')
                count += 1
            else: 
                break

    with open('./rankings/mais_baratos.bin', 'rb') as mais_baratos_file:
        # carrega o conteúdo do arquivo para a memória
        mais_baratos = pickle.load(mais_baratos_file);
        print("\nTimes mais baratos:")
        count = 1
        for time, flag in mais_baratos:
            if count <= 10:
                partida = fun.getPartida(time)
                if flag == "m":
                    time_barato = partida["time_man"]
                    valor = partida["valor_equipe_titular_man"]
                    valorAdversario = partida["valor_equipe_titular_vis"]
                if flag == "v":
                    time_barato = partida["time_vis"]
                    valor = partida["valor_equipe_titular_vis"]
                    valorAdversario = partida["valor_equipe_titular_man"]

                valor = "{:,d}".format(valor).replace(",", ".")
                valorAdversario = "{:,d}".format(valorAdversario).replace(",", ".")

                print(f'\n{count}º-Time: {time_barato}, Valor: R${valor}')
                print("-------------------------------------")
                print(f'{partida["time_man"]} {partida["gols_man"]} x {partida["gols_vis"]} {partida["time_vis"]}')
                print(f'Valor da equipe Adversária: R${valorAdversario}')
                print(f'Data: {partida["data"].strftime("%d/%m/%Y")}\n')
                count += 1
            else:
                break


