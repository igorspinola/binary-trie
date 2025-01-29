# Versao do Python: 3.10.12
from typing import List
from Trie import Trie

tr: Trie = Trie()

entrada: str = input()

while entrada != 'e':

    if entrada == 'i':
        arg: str = input()
        result_i: str = tr.insere(arg)
        print(result_i)
    elif entrada == 'c':
        arg: str = input()
        result_c: str = tr.consulta(arg)
        print(result_c)
    elif entrada == 'f':
        result_f: List = tr.rankear()
        if len(result_f[0]) == 0:
            print("trie vazia")
        else:
            print("palavras mais consultadas:")
            for e in result_f[0]:
                print(e)
            print("numero de acessos: " + str(result_f[1]))
    elif entrada == 'p':
        tr.imprimir_arvore()
    else:
        pass

    entrada = input()
