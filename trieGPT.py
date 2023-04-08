import pickle

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.codigo = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_word(self, word, codigo):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.codigo = codigo

    def search_word(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word, node.codigo

    def get_words_with_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._collect_words(node, prefix)

    def _collect_words(self, node, prefix):
        words = []
        if node.is_end_of_word:
            words.append((prefix, node.codigo))
        for char in node.children:
            words.extend(self._collect_words(node.children[char], prefix + char))
        return words
    
# Cria uma nova árvore trie
trie = Trie()

# Insere cada mês e a quantidade de dias na árvore trie
trie.insert_word("janeiro", 31)
trie.insert_word("fevereiro", 28)
trie.insert_word("março", 31)
trie.insert_word("abril", 30)
trie.insert_word("maio", 31)
trie.insert_word("junho", 30)
trie.insert_word("julho", 31)
trie.insert_word("agosto", 31)
trie.insert_word("setembro", 30)
trie.insert_word("outubro", 31)
trie.insert_word("novembro", 30)
trie.insert_word("dezembro", 31)

with open("arvore_trie.bin", "wb") as f:
    pickle.dump(trie, f)

# Carrega a árvore trie de um arquivo binário
with open("arvore_trie.bin", "rb") as f:
    trie = pickle.load(f)

# Usa a árvore trie normalmente
mes = "março"
existe_mes, dias = trie.search_word(mes)

if existe_mes:
    print(f"O mês de {mes} tem {dias} dias.")
else:
    print(f"O mês de {mes} não está na árvore trie.")

prefixo = "j"
meses = trie.get_words_with_prefix(prefixo)

if len(meses) > 0:
    print(f"Os meses que começam com '{prefixo}' são:")
    for mes, dias in meses:
        print(f"{mes.capitalize()} tem {dias} dias.")
else:
    print(f"Nenhum mês começa com '{prefixo}' na árvore trie.")
