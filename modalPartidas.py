import getPartida as fun
import pickle
import time
import PySimpleGUI as sg
import contextlib
import io
import functions as utils
def make_win2(ano_inicio, ano_fim, nome_time, qtde_partidas, indices_partidas, modo):
    sg.theme('DarkGrey14')
    
    layout = [
                [sg.Text(f"Mostrando {qtde_partidas} partidas de {nome_time} por vez")],
                [sg.Output(size = (100,30), key='output')],
                [sg.Button('<<', key='prev'), sg.Button('>>',key='next')],
                [sg.Text(f'De {ano_inicio} até {ano_fim}')],
            ]
    
   
    window = sg.Window('Ver Partidas', layout)

    j= -int(qtde_partidas)
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
                        break;                
            else:
                j+=int(qtde_partidas)
                print("Sem mais partidar para frente")
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
                j-=int(qtde_partidas)
                print("Sem mais partidar para trás")
            window['output'].set_vscroll_position(0)

    window.close()