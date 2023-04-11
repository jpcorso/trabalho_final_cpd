import rankings as RK
import arbitros_page as ARB
import teamsHistory as CONF
import teamHistory as TH
import PySimpleGUI as sg

#Define as configurações da janela
sg.theme('LightBlue')

layout = [    
        [sg.Text('A.J - Brasileirão  | Saiba tudo sobre o mundo da bola', font=('Helvetica', 20), justification='center')],
        [sg.Text('', font=('Helvetica', 5), justification='center')],
        [sg.Column([ 
            [sg.Image('./public/Campeonato_Brasileiro_Série_A_logo1.png',)]
        ],element_justification='center', vertical_alignment='center'),
        sg.Column([
            [sg.Text('Escolha uma das opções abaixo:', font=('Helvetica', 16), justification='center')],
            [sg.Text('', font=('Helvetica', 5), justification='center')],
            [sg.Button('Histórico', size=(30, 5))],
            [sg.Button('Confrontos', size=(30, 5))],
            [sg.Button('Árbitros', size=(30, 5))],
            [sg.Button('Rankings', size=(30, 5))]
        ], element_justification='center', vertical_alignment='center'),
        sg.Column([
            [sg.Image('./public/img_times.png')]
        ], element_justification='center', vertical_alignment='center')
    ]
]


# Cria a janela
window = sg.Window('futeTUDO', layout, size=(690, 500))

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