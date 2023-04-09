import teamHistory as TH
import rankings as RK
import arbitros_page as ARB
import teamsHistory as CONF
import PySimpleGUI as sg

#Define as configurações da janela
sg.theme('DarkGrey14')
layout = [
    [sg.Text('futeTUDO - Saiba tudo sobre o mundo da bola', font=('Helvetica', 20), justification='center')],
    [sg.Text('Escolha uma das opções abaixo:', font=('Helvetica', 16), justification='center')],
    [sg.Button('Histórico', size=(15, 2)), sg.Button('Confrontos', size=(15, 2)), sg.Button('Árbitros', size=(15, 2)), sg.Button('Rankings', size=(15, 2))],
    [sg.Text('', size=(40, 10))] # Adiciona um espaço em branco abaixo das opções
]

# Cria a janela
window = sg.Window('futeTUDO', layout, size=(800, 600))

while True:
    # Lê os eventos da janela
    event, values = window.read()

    # Executa a opção selecionada pelo usuário
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Histórico':
        TH.history()
    elif event == 'Confrontos':
        CONF.history()
    elif event == 'Árbitros':
        ARB.arbitros()
    elif event == 'Rankings':
        RK.exibir_rankings()

# Fecha a janela
window.close()
