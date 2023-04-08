import pickle
import getPartida as fun
import PySimpleGUI as sg

def exibir_rankings():
    sg.theme('DarkGrey14')
    layout = [
        [sg.Text('Rankings do Brasileirão do período de 2003 até 2020...')],
        [sg.Button('Ranking de público', key='publico')],
        [sg.Button('Ranking de gols', key='gols')],
        [sg.Button('Ranking de maiores vencedores', key='vitorias')],
        [sg.Button('Ranking de maiores derrotados', key='derrotas')],
        [sg.Button('Times mais velhos', key='idade_maior')],
        [sg.Button('Times mais jovens', key='idade_menor')],
        [sg.Button('Times mais caros', key='mais_caros')],
        [sg.Button('Times mais baratos', key='mais_baratos')],
        [sg.Button('Sair', key='sair')],
        [sg.Output(size=(80,20), key='output')]
    ]

    window = sg.Window('Rankings do Brasileirão', layout)

    while True:
        event, _ = window.read()

        if event == sg.WIN_CLOSED or event == 'sair':
            window.close() # fechar a janela
            print("Saindo...")
            break

        elif event == 'publico':
            with open('./rankings/publico.bin', 'rb') as publico_file:
                publicos = pickle.load(publico_file)
                window['output'].update('')
                print("Ranking de público:\n")
                for publico in publicos:
                    partida = fun.getPartida(publico)
                    print(f'{partida["time_man"]} {partida["gols_man"]} x {partida["gols_vis"]} {partida["time_vis"]}')
                    print(f'Público: {partida["publico"]}')
                    print(f'Estádio: {partida["estadio"]}')
                    print(f'Data: {partida["data"].strftime("%d/%m/%Y")}')
                    print("-------------------------------------")

        elif event == 'gols':
            with open('./rankings/gols.bin', 'rb') as gols_file:
                gols = pickle.load(gols_file)
                window['output'].update('')
                print("Ranking de gols:\n")
                count = 1 # inicializa a variável contadora
                for time, gol in gols:
                    if count <= 10: # verifica se a contagem ainda não chegou a 10
                        print(f'{count}º: {time}')
                        print(f'{gol} gols')
                        print("-------------------------------------")
                        count += 1 # incrementa a contagem
                    else:
                        break # interrompe o loop quando a contagem chega a 10

        elif event == 'vitorias':
            with open('./rankings/vitorias.bin', 'rb') as vitorias_file:
                vitorias = pickle.load(vitorias_file)
                window['output'].update('')
                print("Ranking de maiores vencedores:\n")
                count = 1
                for time, vitoria in vitorias:
                    if count <= 10:
                        print(f'{count}º: {time}')
                        print(f'{vitoria} vitórias')
                        print("-------------------------------------")
                        count += 1
                    else:
                        break

        elif event == "derrotas":
            with open('./rankings/derrotas.bin', 'rb') as derrotas_file:
                derrotas = pickle.load(derrotas_file)
                window['output'].update('')
                print("Ranking de maiores derrotados:\n")
                count = 1
                for time, derrota in derrotas:
                    if count <= 10:
                        print(f'{count}º: {time}')
                        print(f'{derrota} derrotas')
                        print("-------------------------------------")
                        count += 1
                    else:
                        break

        elif event == "idade_maior":
               with open('./rankings/media_idade_maior.bin', 'rb') as media_idade_maior_file:
                # carrega o conteúdo do arquivo para a memória
                media_idade_maior = pickle.load(media_idade_maior_file);
                window['output'].update('')
                print("Times mais velhos:\n")
                count = 1
                for time, media, data in media_idade_maior:
                    if count <= 10:
                        print(f'{count}º: {time}')
                        print(f'Data: {data.strftime("%d/%m/%Y")}')
                        print(f'{media} anos')
                        print("-------------------------------------")
                        count += 1
                    else:
                        break

        elif event == "idade_menor":
            with open('./rankings/media_idade_menor.bin', 'rb') as media_idade_menor_file:
                # carrega o conteúdo do arquivo para a memória
                media_idade_menor = pickle.load(media_idade_menor_file);
                window['output'].update('')
                print("Times mais jovens:\n")
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

        elif event == "mais_caros":
            with open('./rankings/mais_caros.bin', 'rb') as mais_caros_file:
                # carrega o conteúdo do arquivo para a memória
                mais_caros = pickle.load(mais_caros_file);
                window['output'].update('')
                print("Times mais caros:\n")
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

                        print(f'{count}º-Time: {time_caro}, Valor: R${valor}')
                        print("-------------------------------------")
                        print(f'{partida["time_man"]} {partida["gols_man"]} x {partida["gols_vis"]} {partida["time_vis"]}')
                        print(f'Valor da equipe Adversária: R${valorAdversario}')
                        print(f'Data: {partida["data"].strftime("%d/%m/%Y")}\n')
                        count += 1
                    else: 
                        break
            
        elif event == "mais_baratos":
            with open('./rankings/mais_baratos.bin', 'rb') as mais_baratos_file:
                # carrega o conteúdo do arquivo para a memória
                mais_baratos = pickle.load(mais_baratos_file);
                window['output'].update('')
                print("Times mais baratos:\n")
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

                        print(f'{count}º-Time: {time_barato}, Valor: R${valor}')
                        print("-------------------------------------")
                        print(f'{partida["time_man"]} {partida["gols_man"]} x {partida["gols_vis"]} {partida["time_vis"]}')
                        print(f'Valor da equipe Adversária: R${valorAdversario}')
                        print(f'Data: {partida["data"].strftime("%d/%m/%Y")}\n')
                        count += 1
                    else:
                        break