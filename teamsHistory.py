import getPartida as fun
import pickle
import time
import PySimpleGUI as sg
import modalPartidas as MP
import functions as utils

def history():

    sg.theme('LightBlue')

    layout = [
        [sg.Text('Time 1: '), sg.InputText(key='time_1', default_text='')],
        [sg.Text('Time 2: '), sg.InputText(key='time_2', default_text='')],
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

    window = sg.Window('Histórico de confrontos entre times de futebol', layout, resizable=True)

    def mostrar_ver_partidas():
        window.Element('text').Update(visible = True)
        window.Element('modo_1').Update(visible = True)
        window.Element('modo_2').Update(visible = True)
        window.Element('qtde_partidas').Update(visible = True)
        window.Element('ver_partidas').Update(visible = True)
        window.Element('text').Update(f'Ver partidas de {nome_time_1} e {nome_time_2}')
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
            time_1 = values['time_1']
            time_2 = values['time_2']
            ano_inicio = values['ano_inicio']
            if ano_inicio == '':
                ano_inicio = 0
            ano_fim = values['ano_fim']
            if ano_fim == '':
                ano_fim = 0

            # interessante
            # if not time_1 or not time_2 or not ano_inicio or not ano_fim:
            #     sg.popup('Por favor, preencha todos os campos.')
            #     continue

            with open("./indices_arquivos/indices_times_invertidos.bin", "rb") as arquivo:
                indices_times = pickle.load(arquivo)

                indice_time_1 = utils.indice_do_item(time_1, indices_times)
                indice_time_2 = utils.indice_do_item(time_2, indices_times)
                if not indice_time_1 or not indice_time_2:
                    esconder_ver_partidas()
                    continue
            try:
                ano_inicio = int(ano_inicio)
                ano_fim = int(ano_fim)
            except ValueError:
                sg.popup('Os campos "Início" e "Fim" devem ser preenchidos com números.')
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

            time_1, time_2 = time_1.title(), time_2.title()

            inicio = time.time()

            with open('./indices_arquivos/indices_ano_campeonatos.bin', 'rb') as f:
                indices_campeonatos = pickle.load(f)

                indice_inicio = indices_campeonatos[ano_inicio][0]
                indice_fim = indices_campeonatos[ano_fim][1]
                temPartidas = True
                vitorias_1 = 0
                vitorias_2 = 0
                empates = 0
                mais_gols = [{"id": 0, "total_gols": 0}]
                maior_goleada = [{"id": 0, "diff": 0}]
                maior_publico_1 = {"id": 0, "publico": 0}
                maior_publico_2 = {"id": 0, "publico": 0}
                indices_partidas = []
                i=0
                indice_final_loop=0

                try:
                    with open("./arquivos_invertidos/times_invertidos.bin", "rb") as times_invertidos:
                        times_invertidos.seek(indice_time_1)
                        registro_1 = pickle.load(times_invertidos)

                        times_invertidos.seek(indice_time_2)
                        registro_2 = pickle.load(times_invertidos)
                    ids_time_1 = registro_1["ids"]
                    ids_time_2 = registro_2["ids"]
                    nome_time_1 = registro_1["nome"]
                    nome_time_2 = registro_2["nome"]

                    indices_partidas = [value for value in ids_time_1 if value in ids_time_2]; 
                    indices_partidas_final = [];
                    for i in indices_partidas:
                        if i >= indice_inicio and i <= indice_fim:
                            indices_partidas_final.append(i)
                    for i in range(len(indices_partidas_final)):
                        partida = fun.getPartida(indices_partidas_final[i]);
                        if (partida["ano_campeonato"] >= int(ano_inicio)) and (partida["ano_campeonato"] <= int(ano_fim)):
                            if (partida["time_man"].title() == time_1.title()):
                                if(partida["gols_man"] > partida["gols_vis"]):
                                    vitorias_1+=1
                                elif(partida["gols_man"] < partida["gols_vis"]):
                                    vitorias_2+=1
                                else:
                                    empates+=1

                                maior_publico = partida["publico"]
                                if maior_publico == None:
                                    maior_publico = 0

                                if maior_publico >= maior_publico_1["publico"]:
                                    maior_publico_1 = {"id": partida["id"], "publico": maior_publico}
                            elif (partida["time_vis"].title() == time_1.title()):
                                if(partida["gols_man"] > partida["gols_vis"]):
                                    vitorias_2+=1
                                elif(partida["gols_man"] < partida["gols_vis"]):
                                    vitorias_1+=1
                                else:
                                    empates+=1 
                                
                                maior_publico = partida["publico"]
                                if maior_publico == None:
                                    maior_publico = 0

                                if maior_publico >= maior_publico_2["publico"]:
                                    maior_publico_2 = {"id": partida["id"], "publico": maior_publico}
                        
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
                            print("Fim das partidas.");
                            break;
                        i+=1
                except IndexError as e:
                        print("Fim das partidas.");
                        print(e);
                        temPartidas = False;
            
                fim = time.time()
                tempo_exec = fim - inicio;

                print(f"{nome_time_1} x {nome_time_2}")
                print(f"Analisando entre {ano_inicio} e {ano_fim}")
                print(f"Tempo empregado: {tempo_exec}s")
                print(f"Vitórias do {nome_time_1}: {vitorias_1}")
                print(f"Vitórias do {nome_time_2}: {vitorias_2}")
                print(f"Empates: {empates}")
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
                print(f"Partida com mais público para o {nome_time_1}:")
                partida_publico = fun.getPartida(maior_publico_1["id"]);
                print(f"------"+partida_publico["time_man"]+" "+str(partida_publico["gols_man"])+" x "+str(partida_publico["gols_vis"])+" "+partida_publico["time_vis"])
                print(f"------Data: " + partida_publico["data"].strftime('%d/%m/%Y'))
                print(f"------Estádio: " + partida_publico["estadio"]+"")
                print(f"------Publico: " + str(partida_publico["publico"]))
                print("__________________________________________")
                print(f"Partida com mais público para o {nome_time_2}:")
                partida_publico = fun.getPartida(maior_publico_2["id"]);
                print(f"------"+partida_publico["time_man"]+" "+str(partida_publico["gols_man"])+" x "+str(partida_publico["gols_vis"])+" "+partida_publico["time_vis"])
                print(f"------Data: " + partida_publico["data"].strftime('%d/%m/%Y'))
                print(f"------Estádio: " + partida_publico["estadio"]+"")
                print(f"------Publico: " + str(partida_publico["publico"]))
                
                mostrar_ver_partidas()
                window['output'].set_vscroll_position(0)

        
        elif event == 'ver_partidas':
            modo = None;
            if values['modo_1']:
                modo = 'C'
            else: 
                modo = 'D'
                aux = ano_fim
                ano_fim = ano_inicio
                ano_inicio = aux
            MP.make_win2(int(ano_inicio), int(ano_fim), nome_time_1, values['qtde_partidas'],indices_partidas,modo)
