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
        if tr.raiz.chave == "":
            print("trie vazia")
        else:
            print("palavras mais consultadas:")
            for e in result_f[0]:
                print(e)
            print("numero de acessos: " + str(result_f[1]))
    elif entrada == 'p':
        tr.imprimir_arvore()
    elif entrada == 'r':
        arg: str = input()
        if tr.raiz.chave == "":
            print("trie vazia")
        result_r = tr.prefixo(arg)
        print(f"palavras com prefixo: {arg}")
        # print("result_r:")
        # print(*result_r)
        for e in result_r:
            print(e)
    elif entrada == 's':
        arg: str = input()
        if tr.raiz.chave == "":
            print("trie vazia")
        result_s = tr.sufixo(arg)
        print(f"palavras com sufixo: {arg}")
        # print("result_r:")
        # print(*result_r)
        for e in result_s:
            print(e)
    else:
        pass

    entrada = input()
