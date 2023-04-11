import getPartida as fun
import pickle
import time
import PySimpleGUI as sg
import modalPartidas as MP
import functions as utils

def history():
    sg.theme('LightBlue')

    layout = [
        [sg.Text('Time: '), sg.InputText(key='time', default_text='CSA')],
        [sg.Text('Ano Início: '), sg.InputText(key='ano_inicio', default_text='2003')],
        [sg.Text('Ano Fim: '), sg.InputText(key='ano_fim', default_text='2020')],
        [sg.Button('Buscar')],
        [sg.Text('', key='text', visible=False)],
        [sg.Radio("Crescente", 'faculty', key='modo_1', enable_events=True, default=True, visible=False)],
        [sg.Radio("Decrescente", 'faculty', key='modo_2', enable_events=True, visible=False)],
        [sg.Text('Quantidade: ',visible=False), sg.InputText(key='qtde_partidas', default_text='38', visible=False)],
        [sg.Button('Ver', key="ver_partidas", visible=False)],
        [sg.Text('Resultado:')],
        [sg.Output(size=(60, 20), key='output')]
    ]

    window = sg.Window('Histórico de um Time', layout)

    def mostrar_ver_partidas():
        window.Element('text').Update(visible = True)
        window.Element('modo_1').Update(visible = True)
        window.Element('modo_2').Update(visible = True)
        window.Element('qtde_partidas').Update(visible = True)
        window.Element('ver_partidas').Update(visible = True)
        window.Element('text').Update(f'Ver partidas do {nome_time}')
        window.Element('text').Update(visible = True)

    def esconder_ver_partidas():
        window.Element('text').Update(visible = False)
        window.Element('modo_1').Update(visible = False)
        window.Element('modo_2').Update(visible = False)
        window.Element('ver_partidas').Update(visible = False)
        window.Element('qtde_partidas').Update(visible = False)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            window.close()
            break

        if event == 'Buscar':
            window['output'].update("")
            time_1 = values['time']
            ano_inicio = values['ano_inicio']
            if ano_inicio == '':
                ano_inicio = 0
            ano_fim = values['ano_fim']
            if ano_fim == '':
                ano_fim = 0
            with open("./indices_arquivos/indices_times_invertidos.bin", "rb") as arquivo:
                indices_times = pickle.load(arquivo)
                indice_time = utils.indice_do_item(time_1, indices_times)
                if not indice_time:
                    esconder_ver_partidas()
                    continue

            if int(ano_inicio) < 2003:
                print("Dados do campeonato disponíveis a partir de 2003.")
                esconder_ver_partidas()
                continue
            elif int(ano_fim) > 2020:
                print("Dados do campeonato disponíveis até o de 2020.")
                esconder_ver_partidas()
                continue
            elif int(ano_fim) < int(ano_inicio):
                print("Período inválido. Escolha outro período válido.")
                esconder_ver_partidas()
                continue
                
            inicio = time.time()

            with open('./indices_arquivos/indices_ano_campeonatos.bin', 'rb') as f:
                indices_campeonatos = pickle.load(f)
                indice_inicio = indices_campeonatos[int(ano_inicio)][0]
                indice_fim = indices_campeonatos[int(ano_fim)][1]
                temPartidas = True
                vitorias_1 = 0
                empates = 0
                derrotas_1 = 0
                gols_pro = 0
                gols_contra = 0
                mais_gols = [{"id": 0, "total_gols": 0}]
                maior_goleada = [{"id": 0, "diff": 0}]
                maior_publico_1 = {"id": 0, "publico": 0}

                try:
                    with open("./arquivos_invertidos/times_invertidos.bin", "rb") as times_invertidos:
                        times_invertidos.seek(indice_time)
                        registro = pickle.load(times_invertidos)
                    ids_time_1 = registro["ids"]
                    nome_time = registro["nome"]

                    indices_partidas = []            
                    for i in ids_time_1:
                        if i >= indice_inicio and i <= indice_fim:
                            indices_partidas.append(i)
                    primeiraPartida = False
                    for i in range(len(indices_partidas)):
                        partida = fun.getPartida(indices_partidas[i]);
                        if (partida["ano_campeonato"] >= int(ano_inicio)) and (partida["ano_campeonato"] <= int(ano_fim)):
                            if (primeiraPartida == False):
                                indice_inicial_arq = i
                                primeiraPartida = True

                            if (partida["time_man"].title() == time_1.title()):
                                if(partida["gols_man"] > partida["gols_vis"]):
                                    vitorias_1+=1
                                elif(partida["gols_man"] < partida["gols_vis"]):
                                    derrotas_1+=1
                                else:
                                    empates+=1

                                gols_pro+=partida["gols_man"]
                                gols_contra+=partida["gols_vis"]

                                maior_publico = partida["publico"]
                                if maior_publico == None:
                                    maior_publico = 0

                                if maior_publico >= maior_publico_1["publico"]:
                                    maior_publico_1 = {"id": partida["id"], "publico": maior_publico}
                            elif (partida["time_vis"].title() == time_1.title()):
                                if(partida["gols_man"] > partida["gols_vis"]):
                                    derrotas_1+=1
                                elif(partida["gols_man"] < partida["gols_vis"]):
                                    vitorias_1+=1
                                else:
                                    empates+=1 

                                gols_pro+=partida["gols_vis"]
                                gols_contra+=partida["gols_man"] 
                        
                            total_gols = partida["gols_man"]+partida["gols_vis"]
                            if total_gols > mais_gols[0]["total_gols"]:
                                mais_gols = [{
                                    "id": partida["id"], 
                                    "total_gols": total_gols, 
                                }]
                            elif total_gols == mais_gols[0]["total_gols"]:
                                mais_gols.append({
                                    "id": partida["id"], 
                                    "total_gols": total_gols, 
                                })  
                            
                            diff = abs(partida["gols_man"]-partida["gols_vis"])
                            if diff > maior_goleada[0]["diff"]:
                                maior_goleada = [{
                                    "id": partida["id"],
                                    "diff": diff,
                                }]
                            elif diff == maior_goleada[0]["diff"]:
                                maior_goleada.append({
                                    "id": partida["id"],
                                    "diff": diff,
                                })
                                
                            if (partida["ano_campeonato"] == 2020 and partida["rodada"] == 38):
                                print("Fim das partidas.");
                                break;  
                        elif(partida["ano_campeonato"] > int(ano_fim)): 
                            break;
                        i+=1
                except IndexError as e:
                        print(e);
                        temPartidas = False;
                fim = time.time()

                tempo_exec = fim - inicio;

                print(f"_____________{nome_time}_____________")
                print(f"Analisando entre {ano_inicio} e {ano_fim}")
                print(f"Tempo empregado: {tempo_exec}s")
                print(f"Vitórias: {vitorias_1}")
                print(f"Empates: {empates}")
                print(f"Derrotas: {empates}")
                print(f"Gols feitos: {gols_pro}")
                print(f"Gols sofridos: {gols_contra}")
                print("__________________________________________")
                print("Partida com mais gols:")
                print(f"-------------Qtde Gols: {mais_gols[0]['total_gols']}-------------")
                for partida in mais_gols:
                    partida_mais_gols = fun.getPartida(partida["id"]);
                    print(f"------Data: {partida_mais_gols['data'].strftime('%d/%m/%Y')}")
                    print(f"------Placar: {partida_mais_gols['time_man']} {str(partida_mais_gols['gols_man'])} x {str(partida_mais_gols['gols_vis'])} {partida_mais_gols['time_vis']}")
                    print(f"---")
                print("__________________________________________")
                print("Partida com a maior goleada (maior diferença de gols):")
                for partida in maior_goleada:
                    partida_goleada = fun.getPartida(partida["id"]);
                    print(f"------Data: {partida_goleada['data'].strftime('%d/%m/%Y')}")
                    print(f"------Placar: {partida_goleada['time_man']} {str(partida_goleada['gols_man'])} x {str(partida_goleada['gols_vis'])} {partida_goleada['time_vis']}")
                    print(f"---")
                print("__________________________________________")
                print(f"Partida com mais público para o {nome_time}:")
                partida_publico = fun.getPartida(maior_publico_1["id"]);
                print(f"------"+partida_publico["time_man"]+" "+str(partida_publico["gols_man"])+" x "+str(partida_publico["gols_vis"])+" "+partida_publico["time_vis"])
                print(f"------Data: " + partida_publico["data"].strftime('%d/%m/%Y'))
                print(f"------Estádio: " + partida_publico["estadio"]+"")
                print(f"------Publico: " + str(partida_publico["publico"]))
                print("__________________________________________")   

                mostrar_ver_partidas()
                window['output'].set_vscroll_position(0);

        elif event == 'ver_partidas':
            modo = None;
            if values['modo_1']:
                modo = 'C'
            else: 
                modo = 'D'
                aux = ano_fim
                ano_fim = ano_inicio
                ano_inicio = aux
            MP.make_win2(int(ano_inicio), int(ano_fim), nome_time, values['qtde_partidas'],indices_partidas,modo)
