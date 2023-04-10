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
                [sg.Button('<<', key='prev'), sg.Button('>>', key='next')],
                [sg.Text(f'De {ano_inicio} até {ano_fim}', key='periodo')],
                [sg.Text(f'', key='teste')],
            ]
    
   
    window = sg.Window('Ver Partidas', layout)

    j = -int(qtde_partidas)+1
    fim = False
    inicio = False
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == 'next':
            window['output'].update('')
            if not fim:
                j+=int(qtde_partidas)-1
                for i in range(len(qtde_partidas)-1):
                    if (i+j) < len(indices_partidas)-1:
                        inicio = False
                        fim = False
                        partida = fun.getPartida(indices_partidas[i+j])
                        utils.printaPartida(partida)
                    else:
                        fim = True
                        break
            else:
                print("Sem mais partidas à frente.")
            window.Element('teste').update(j)
            window['output'].set_vscroll_position(0)

        if event == 'prev':
            window['output'].update('')
            if not inicio:
                j -= int(qtde_partidas) - 1
                if j >= 0:
                    for i in range(len(qtde_partidas) - 1):
                        if (i+j) < len(indices_partidas) - 1:
                            inicio = False
                            fim = False
                            partida = fun.getPartida(indices_partidas[i + j])
                            utils.printaPartida(partida)
                        else:
                            inicio = True
                            break

            else:
                print("Sem mais partidas para trás.")
                j = 0
            window.Element('teste').update(j)
            window['output'].set_vscroll_position(0)

    window.close()