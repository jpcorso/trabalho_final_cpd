
def colocaTupla(matBrasileirao, listaDados):
    for j in range(1, len(matBrasileirao)): #percorre a coluna, começamos do 1 porque não queremos a primeira linha
        linha = []  #armazena uma linha, que será posteriormente um elemento da nossa lista, criando uma tupla
        for i in range(len(matBrasileirao[j])): #percorre a linha dentro de um elemento j da coluna
            linha.append(matBrasileirao[j][i].value)    #coloca cada elemento que tem na linha em uma lista
        listaDados.append(tuple(linha)) #coloca todos os elementos da linha em uma posicao do nosso array final
        
    print(listaDados)