import pickle
class TrieNode:
    def __init__(self, ch = ''):
        self.key = ch
        self.children = {}

class Trie:
    def __init__(self,file):
        self.root = TrieNode()
        pickle.dump(self.root,file)

    def inserirTime(self,f_read, f_write, time):
        current = self.root;
        f_read.seek(0)
        current_f = pickle.load(f_read)
        for i,char in enumerate(time):
            # print("em memoria")
            # if char not in current.children:
            #     prefix = time[0:i+1]
            #     current.children[char] = TrieNode(prefix);
            print("no arquivo")
            if char not in current_f.children:
                prefix = time[0:i+1]
                current_f.children[char] = TrieNode(prefix);
            current_f = current_f.children[char]
            print(current_f.key);
            print(current_f.children);
        pickle.dump(current_f,f_write)

