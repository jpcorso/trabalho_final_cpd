import getPartida as fun
import PySimpleGUI as sg
import functions as utils

def make_win2(ano_inicio, ano_fim, nome_time, qtde_partidas, indices_partidas, modo):
    sg.theme('LightBlue')
    
    layout = [
                [sg.Text(f"Mostrando {qtde_partidas} partidas de {nome_time} por vez")],
                [sg.Output(size = (100,30), key='output')],
                [sg.Button('<<', key='prev'), sg.Button('>>', key='next')],
                [sg.Text(f'De {ano_inicio} até {ano_fim}', key='periodo')],
                [sg.Text(f'', key='teste')],
            ]
    
   
    window = sg.Window('Ver Partidas', layout)

    j = -int(qtde_partidas)
    fim = False
    inicio = False
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == 'next':
            window['output'].update('')
            if (j + int(qtde_partidas) < len(indices_partidas)):
                j+=int(qtde_partidas)
                if modo.upper() == "D":
                    indices_partidas = sorted(indices_partidas, reverse=True)

                for i in range(int(qtde_partidas)):
                    if ((i+j) < len(indices_partidas)):
                        partida = fun.getPartida(indices_partidas[i+j])
                        utils.printaPartida(partida)
                        print("------------------")
                    else: 
                        j+=int(qtde_partidas)
                        print("Sem mais partidar para frente")
                        break;               
            window.Element('teste').update(j)
            window['output'].set_vscroll_position(0)

        if event == 'prev':
            window['output'].update('')
            if (j-int(qtde_partidas) >= 0):
                j-=int(qtde_partidas)
                if modo.upper() == "D":
                    indices_partidas = sorted(indices_partidas, reverse=True)
                for i in range(int(qtde_partidas)):
                    if ((i+j) < len(indices_partidas)):
                        partida = fun.getPartida(indices_partidas[i+j])
                        utils.printaPartida(partida)
                        print("------------------")
                    else: 
                        break;   
            else:
                print("Sem mais partidar para trás")
                j = 0
            window.Element('teste').update(j)
            window['output'].set_vscroll_position(0)

    window.close()