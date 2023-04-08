import pickle
import getPartida as fun
import PySimpleGUI as sg

def arbitros():
    sg.theme('DarkGrey14')

    layout = [
        [sg.Text('Pesquise um árbitro:', font=('Helvetica', 14), size=(15,1)),
        sg.InputText(key='arbitro', size=(20,1)),
        sg.Button('Pesquisar', size=(10,1))],
        [sg.Text('Nome do time:', font=('Helvetica', 14), size=(15,1)),
        sg.InputText(key='time', size=(20,1), disabled=True),  # Define o estado inicial como desativado
        sg.Button('Ver Aproveitamento', size=(15,1), disabled=True)],  # Define o estado inicial como desativado
        [sg.Text('Média de faltas por jogo:', font=('Helvetica', 14), size=(30,1))],
        [sg.Text('', size=(20, 1), key='-MEDIA_FALTAS-')],
        [sg.Text('',font=('Helvetica', 14), size=(50,1), key='-TEXT_APROVEITAMENTO-')],
        [sg.Text('', size=(80, 1), key='-APROVEITAMENTO-')],  # Novo elemento para exibir o resultado do aproveitamento
        [sg.Text('', size=(40, 10))],
        [sg.Text('Partidas:', font=('Helvetica', 14), size=(35,1))],
        [sg.Listbox(values=[], size=(50, 10), key='-PARTIDAS-')],
    ]

    window = sg.Window('Aproveitamento de Árbitro', layout)

    window.read()

    indices_arbitros_f = open('./indices_arquivos/indices_arbitros_invertidos.bin', 'rb')
    indices_arbitros = pickle.load(indices_arbitros_f)

    arbitros_f = open('./arquivos_invertidos/arbitros_invertidos.bin', 'rb')
    arbitros = pickle.load(arbitros_f)

    numFaltas = noneTypeFaltas = 0
    window['Ver Aproveitamento'].update(disabled=True)
    window['time'].update(disabled=True)

    while True:
        numFaltas = noneTypeFaltas = 0  # Reinicialização das variáveis
        event, values = window.read()
        
        if event == sg.WIN_CLOSED:
            break

        if event == 'Pesquisar':
            nomeArbitro = values['arbitro']
            arbitros_f.seek(indices_arbitros[nomeArbitro])
            arbitro_ids = pickle.load(arbitros_f)["ids"]
            partidas = []

            for i in arbitro_ids:
                partida = fun.getPartida(i)

                if partida["faltas_man"] is not None and partida["faltas_vis"] is not None:
                    numFaltas += partida["faltas_man"] + partida["faltas_vis"]
                else:
                    noneTypeFaltas += 1

                partidas.append(f'{partida["time_man"]} vs {partida["time_vis"]}')

            if len(arbitro_ids) - noneTypeFaltas > 0:
                mediaFaltas = numFaltas / (len(arbitro_ids) - noneTypeFaltas)
            else:
                mediaFaltas = "Este árbitro não possui dados de faltas."

            window.Element('-PARTIDAS-').Update(values=partidas)
            window.Element('-MEDIA_FALTAS-').Update(f"{mediaFaltas}")
            
            # ativa a opção de pesquisa pelo time
            window['Ver Aproveitamento'].update(disabled=False)
            window['time'].update(disabled=False)


            
        if event == 'Ver Aproveitamento':
            nomeTime = values['time']
            pontosGanhos = pontosDisputados = 0

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

                    window.Element('-TEXT_APROVEITAMENTO-').Update(f"Aproveitamento do {nomeTime} com o árbitro {nomeArbitro}:")
                    window.Element('-APROVEITAMENTO-').Update(f"Aproveitamento do {nomeTime} com o árbitro {nomeArbitro}: {aproveitamento}%")
                else:
                    window.Element('-TEXT_APROVEITAMENTO-').Update(f"Sem dados de partidas do {nomeArbitro} com o {nomeTime}")
                    window.Element('-APROVEITAMENTO-').Update(f"Sem dados de partidas do {nomeArbitro} com o {nomeTime}")
                    pontosGanhos = pontosDisputados = noneTypeFaltas = 0
                                    

    
arbitros()
                            

                            
                            
                            
