import getPartida as fun
import pickle
import time
import PySimpleGUI as sg
import contextlib
import io

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
                        printaPartida(partida)
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
                        printaPartida(partida)
                        print("------------------")
                    else: 
                        break;                
            else:
                j-=int(qtde_partidas)
                print("Sem mais partidar para trás")
            window['output'].set_vscroll_position(0)

    window.close()