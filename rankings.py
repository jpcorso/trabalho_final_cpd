import pickle
import getPartida as fun

with open('./rankings/publico.bin', 'rb') as publico_file:
    # carrega o conteúdo do arquivo para a memória
    publicos = pickle.load(publico_file);
    print("Ranking públicos:")
    for publico in publicos:
        partida = fun.getPartida(publico)
        print(f'\n{partida["time_man"]} {partida["gols_man"]} x {partida["gols_vis"]} {partida["time_vis"]}')
        print(f'Público: {partida["publico"]}')
        print(f'Estádio: {partida["estadio"]}')
        print(f'Data: {partida["data"].strftime("%d/%m/%Y")}\n')

with open('./rankings/gols.bin', 'rb') as gols_file:
    # carrega o conteúdo do arquivo para a memória
    gols = pickle.load(gols_file);
    print("\nRanking gols:")
    print(gols)

with open('./rankings/vitorias.bin', 'rb') as vitorias_file:
    # carrega o conteúdo do arquivo para a memória
    vitorias = pickle.load(vitorias_file);
    print("\nRanking vitorias:")
    print(vitorias)

with open('./rankings/derrotas.bin', 'rb') as derrotas_file:
    # carrega o conteúdo do arquivo para a memória
    derrotas = pickle.load(derrotas_file);
    print("\nRanking derrotas:")
    print(derrotas)

with open('./rankings/media_idade_maior.bin', 'rb') as media_idade_maior_file:
    # carrega o conteúdo do arquivo para a memória
    media_idade_maior = pickle.load(media_idade_maior_file);
    print("\nTimes mais velhos:")
    print(media_idade_maior)

with open('./rankings/media_idade_menor.bin', 'rb') as media_idade_menor_file:
    # carrega o conteúdo do arquivo para a memória
    media_idade_menor = pickle.load(media_idade_menor_file);
    print("\nTimes mais jovens:")
    print(media_idade_menor)

with open('./rankings/mais_caros.bin', 'rb') as mais_caros_file:
    # carrega o conteúdo do arquivo para a memória
    mais_caros = pickle.load(mais_caros_file);
    print("\nTimes mais caros:")
    i = 0
    for time, flag in mais_caros:
        partida = fun.getPartida(time)
        if flag == "m":
            time_caro = partida["time_man"]
            valor = partida["valor_equipe_titular_man"]
            valorAdversario = partida["valor_equipe_titular_vis"]
        if flag == "v":
            time_caro = partida["time_vis"]
            valor = partida["valor_equipe_titular_vis"]
            valorAdversario = partida["valor_equipe_titular_man"]
        i+=1

        valor = "{:,d}".format(valor).replace(",", ".")
        valorAdversario = "{:,d}".format(valorAdversario).replace(",", ".")

        print(f'\nTime: {time_caro}, Valor: R${valor}')
        print("-------------------------------------")
        print(f'{partida["time_man"]} {partida["gols_man"]} x {partida["gols_vis"]} {partida["time_vis"]}')
        print(f'Valor da equipe Adversária: R${valorAdversario}')
        print(f'Data: {partida["data"].strftime("%d/%m/%Y")}\n')

with open('./rankings/mais_baratos.bin', 'rb') as mais_baratos_file:
    # carrega o conteúdo do arquivo para a memória
    mais_baratos = pickle.load(mais_baratos_file);
    print("\nTimes mais baratos:")
    i = 0
    for time, flag in mais_baratos:
        partida = fun.getPartida(time)
        if flag == "m":
            time_barato = partida["time_man"]
            valor = partida["valor_equipe_titular_man"]
            valorAdversario = partida["valor_equipe_titular_vis"]
        if flag == "v":
            time_barato = partida["time_vis"]
            valor = partida["valor_equipe_titular_vis"]
            valorAdversario = partida["valor_equipe_titular_man"]
        i+=1

        valor = "{:,d}".format(valor).replace(",", ".")
        valorAdversario = "{:,d}".format(valorAdversario).replace(",", ".")

        print(f'\nTime: {time_barato}, Valor: R${valor}')
        print("-------------------------------------")
        print(f'{partida["time_man"]} {partida["gols_man"]} x {partida["gols_vis"]} {partida["time_vis"]}')
        print(f'Valor da equipe Adversária: R${valorAdversario}')
        print(f'Data: {partida["data"].strftime("%d/%m/%Y")}\n')


