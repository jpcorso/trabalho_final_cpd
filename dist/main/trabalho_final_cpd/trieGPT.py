class TrieNode:
    def __init__(self):
        self.filhos = {}
        self.eh_folha = False
        self.indice = 0

class Trie:
    def __init__(self):
        self.raiz = TrieNode()

    def inserir_time(self, time, indice):
        nodo = self.raiz
        for ch in time:
            if ch not in nodo.filhos:
                nodo.filhos[ch] = TrieNode()
            nodo = nodo.filhos[ch]
        nodo.eh_folha = True
        nodo.indice = indice

    def pesquisa_time(self, time):
        nodo = self.raiz
        for ch in time:
            if ch not in nodo.filhos:
                return False
            nodo = nodo.filhos[ch]
        if (nodo.eh_folha):
            return nodo.eh_folha, nodo.indice
        else:
            return False

    def todos_os_times_com(self, prefixo):
        nodo = self.raiz
        for ch in prefixo:
            if ch not in nodo.filhos:
                return []
            nodo = nodo.filhos[ch]
        return self._pega_times(nodo, prefixo)

    def _pega_times(self, nodo, prefixo):
        times = []
        if nodo.eh_folha:
            times.append((prefixo, nodo.indice))
        for ch in nodo.filhos:
            times.extend(self._pega_times(nodo.filhos[ch], prefixo + ch))
        return times