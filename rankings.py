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

with open('./rankings/media_idade.bin', 'rb') as media_idade_file:
    # carrega o conteúdo do arquivo para a memória
    media_idade = pickle.load(media_idade_file);
    print("\nRanking idade (mais velho):")
    print(media_idade)