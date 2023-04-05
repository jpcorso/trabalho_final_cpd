import pickle

with open('./rankings/publico.bin', 'rb') as publico_file:
    # carrega o conteúdo do arquivo para a memória
    publico = pickle.load(publico_file);
    print("Ranking públicos:")
    print(publico)

with open('./rankings/gols.bin', 'rb') as gols_file:
    # carrega o conteúdo do arquivo para a memória
    gols = pickle.load(gols_file);
    print("\nRanking gols:")
    print(gols)

with open('./rankings/vitorias.bin', 'rb') as vitorias_file:
    # carrega o conteúdo do arquivo para a memória
    vitorias = pickle.load(vitorias_file);
    print("\nRanking vitorias:")
    print(vitorias)

with open('./rankings/derrotas.bin', 'rb') as derrotas_file:
    # carrega o conteúdo do arquivo para a memória
    derrotas = pickle.load(derrotas_file);
    print("\nRanking derrotas:")
    print(derrotas)

with open('./rankings/media_idade_maior.bin', 'rb') as media_idade_maior_file:
    # carrega o conteúdo do arquivo para a memória
    media_idade_maior = pickle.load(media_idade_maior_file);
    print("\nTimes mais velhos:")
    print(media_idade_maior)

with open('./rankings/media_idade_menor.bin', 'rb') as media_idade_menor_file:
    # carrega o conteúdo do arquivo para a memória
    media_idade_menor = pickle.load(media_idade_menor_file);
    print("\nTimes mais jovens:")
    print(media_idade_menor)

with open('./rankings/mais_caros.bin', 'rb') as mais_caros_file:
    # carrega o conteúdo do arquivo para a memória
    mais_caros = pickle.load(mais_caros_file);
    print("\nTimes mais caros:")
    print(mais_caros)

with open('./rankings/mais_baratos.bin', 'rb') as mais_baratos_file:
    # carrega o conteúdo do arquivo para a memória
    mais_baratos = pickle.load(mais_baratos_file);
    print("\nTimes mais baratos:")
    print(mais_baratos)


