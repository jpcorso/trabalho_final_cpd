import minhaTrie
import pickle
import sys
from dataclasses import dataclass
@dataclass
class Nodo:
    ehFolha: bool
    chave: str
    filhos: list
    pos: int


def criaTrie():
    f = open("teste.pkl","wb")
    raiz = Nodo(None,'*',[],0)
    pickle.dump(raiz,f)
    f.close()

def insereTrie(raiz,time):
    with open("teste.pkl","wb") as f:
        nodo = raiz;
        prox_pos = 0
        pos_raiz = 0
        pos_pai = 0;
        for i,ch in enumerate(time):
            if ch in nodo.filhos:
                nodo = nodo.filhos[ch]
            else:
                nodo.filhos.append(f.tell()+3)
                f.seek(nodo.pos)
                pickle.dump(nodo,f)
                ehFolha = False
                if (i == len(time)-1):
                    ehFolha = True
                novo_nodo = Nodo(ehFolha,ch,[],f.tell())
                pickle.dump(novo_nodo,f);
                nodo = novo_nodo

            # print(f.tell())
            # nova_raiz.filhos[time]=Nodo(False,time,[],f.tell())
            # f.seek(0)
            # pickle.dump(nova_raiz,f)
            # return nova_raiz;
            # with open("teste.pkl","wb") as f:
            #     f.seek(0)
            #     pickle.dump(raiz,f)

criaTrie()
with open("teste.pkl","rb") as f:
    raiz = pickle.load(f)



insereTrie(raiz,"Gago")

with open("teste.pkl","rb") as f:
    f.seek(0)
    print(pickle.load(f))
    # print(pickle.load(f))
    # print(pickle.load(f))
    # print(pickle.load(f))
    # print(pickle.load(f))

# insereTrie(raiz,"Galinha")
# with open("teste.pkl","rb") as f:
#     raiz = pickle.load(f)
#     print(raiz)
#     print(pickle.load(f))
#     print(pickle.load(f))
#     print(pickle.load(f))
#     print(pickle.load(f))
#     print(pickle.load(f))
#     print(pickle.load(f))
#     print(pickle.load(f))
    
    

# insereTrie(raiz,"Galinha")
# with open("teste.pkl","rb") as f:
#     print(pickle.load(f))
#     print(pickle.load(f))
#     print(pickle.load(f))
#     print(pickle.load(f))
# p1 = Nodo(False, 'c', [])
# p2 = Nodo(False, 'g', [])
# p3 = Nodo(False, 'o', [])
# f = open("teste.pkl","wb")
# inicio = f.tell()
# pickle.dump(p1,f)
# p1.filhos.append({'teste': p2, 'testinho': f.tell()})
# f.seek(inicio)
# pickle.dump(p1,f)
# f.close()

# f = open("teste.pkl","wb")
# inicio = f.tell()
# pickle.dump(p1,f)
# p1.filhos.append({'teste': p3, 'testinho': f.tell()})
# f.seek(inicio)
# pickle.dump(p1,f)
# f.close()

# f = open("teste.pkl",'rb')
# f.seek(0)
# print(pickle.load(f))
# f.close()