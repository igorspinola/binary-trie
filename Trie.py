from typing import Dict, List
from No import No

class Trie:
    def __init__(self) -> None:
        self.raiz: No = No()
        self.contador: Dict[str, int] = {}

    def insere(self, palavra: str) -> str:
        if self.consulta(palavra, False) != f"palavra inexistente: {palavra}":
            return f"palavra ja existente: {palavra}"
        if self.raiz.chave == "":
            self.raiz.chave = palavra[0]
            atual = self.raiz
            for le in palavra[1:len(palavra)]:
                atual.esq = No(le)
                atual = atual.esq
            atual.esq = No("*")
        else:
            atual: No = self.raiz
            anterior: No = self.raiz
            temp: No | None = No()
            nova_primeira_letra: bool = False
            for i in range(len(palavra)):
                if atual.esq and atual.chave == palavra[i] and i != len(palavra) - 1:
                    anterior = atual
                    atual = atual.esq
                    continue
                elif atual.esq and i == len(palavra) - 1 and atual.chave == palavra[i]:
                    temp = atual.esq
                    atual.esq = No("*")
                    atual.esq.dir = temp
                elif not atual.esq and i == len(palavra) - 1 and atual.chave == palavra[i]:
                    atual.esq = No("*")
                elif not nova_primeira_letra:
                    if ord(atual.chave) > ord(palavra[i]) and anterior != atual:
                        nova_primeira_letra = True
                        temp = atual
                        anterior.esq = No(palavra[i])
                        anterior.esq.dir = temp
                        atual = anterior.esq
                        if i == len(palavra) - 1:
                            atual.esq = No("*")
                    elif ord(atual.chave) < ord(palavra[i]) and anterior != atual:
                        nova_primeira_letra = True
                        while atual.dir and ord(atual.dir.chave) < ord(palavra[i]):
                            anterior = atual
                            atual = atual.dir
                        if atual.dir and atual.dir.chave != palavra[i]:
                            temp = atual.dir
                            atual.dir = No(palavra[i])
                            atual.dir.dir = temp
                            anterior = atual
                            atual = atual.dir
                        elif atual.dir and atual.dir.chave == palavra[i]:
                            nova_primeira_letra = False
                            anterior = atual
                            atual = atual.dir
                            if atual.esq:
                                anterior = atual
                                atual = atual.esq
                        else:
                            atual.dir = No(palavra[i])
                            anterior = atual
                            atual = atual.dir
                        if i == len(palavra) - 1:
                            if atual.esq:
                                temp = anterior.esq
                                anterior.esq = No("*")
                                anterior.esq.dir = temp
                            elif not atual.esq:
                                atual.esq = No("*")
                    elif ord(atual.chave) < ord(palavra[i]) and anterior == atual:
                        nova_primeira_letra = True
                        while atual.dir and ord(atual.dir.chave) < ord(palavra[i]):
                            anterior = atual
                            atual = atual.dir
                        if atual.dir and atual.dir.chave != palavra[i]:
                            temp = atual.dir
                            atual.dir = No(palavra[i])
                            atual.dir.dir = temp
                            anterior = atual
                            atual = atual.dir
                        elif atual.dir and atual.dir.chave == palavra[i]:
                            nova_primeira_letra = False
                            anterior = atual
                            atual = atual.dir
                            if atual.esq:
                                anterior = atual
                                atual = atual.esq
                            continue
                        else:
                            atual.dir = No(palavra[i])
                            anterior = atual
                            atual = atual.dir
                        if i == len(palavra) - 1:
                            atual.esq = No("*")
                    elif ord(atual.chave) > ord(palavra[i]) and anterior == atual:
                        nova_primeira_letra = True
                        nova_raiz = No(palavra[i])
                        self.raiz = nova_raiz
                        self.raiz.dir = atual
                        atual = self.raiz
                        anterior = self.raiz
                        if i == len(palavra) - 1:
                            atual.esq = No("*")
                elif not atual.esq:
                    atual.esq = No(palavra[i])
                    if i == len(palavra) - 1:
                        atual.esq.esq = No("*")
                    anterior = atual
                    atual = atual.esq


        return f"palavra inserida: {palavra}"

    def consulta(self, palavra: str, incrementaContador:bool = True) -> str:
        atual: No = self.raiz
        palavra += "*"
        for i,le in enumerate(palavra):
            while atual.dir and atual.chave != le:
                atual = atual.dir
            if not atual.dir and i != len(palavra) - 1 and atual.chave == "*":
                break
            if i == len(palavra) - 1 and atual.chave == "*":
                palavra = palavra[0:-1]
                if incrementaContador:
                    if self.contador.get(palavra):
                        self.contador[palavra] += 1
                    else:
                        self.contador[palavra] = 1
                    return f"palavra existente: {palavra} {self.contador[palavra]}"
                else:
                    return "palavra ja existente"
            if atual.chave == le and atual.esq:
                atual = atual.esq
            elif not atual.dir:
                break
        return f"palavra inexistente: {palavra[0:-1]}"

    def rankear(self) -> List:
        max: int = 0
        chaves: List[str] = []
        for e in self.contador:
            valor = self.contador[e]
            if max < valor:
                max = valor
        for e in self.contador:
            if self.contador[e] == max:
                chaves.append(e)
        chaves.sort()
        return [chaves, max]

    def imprimir_no(self, no: No) -> None:
        d: str = ""
        e: str = ""
        if no.dir:
            d = no.dir.chave
        else:
            d = "nil"
        if no.esq:
            e = no.esq.chave
        else:
            e = "nil"
        print(f"letra: {no.chave} fesq: {e} fdir: {d}")

    def pre_ordem(self, no: No | None) -> None:
        if not no:
            return
        self.imprimir_no(no)
        self.pre_ordem(no.esq)
        self.pre_ordem(no.dir)

    def imprimir_arvore(self) -> None:
        if self.raiz.chave == "":
            print("trie vazia")
            return
        self.pre_ordem(self.raiz)


    def prefixo(self, pre: str) -> List[str]:
        atual: No = self.raiz
        resultado: List[str] = []
        for i,le in enumerate(pre):
            while atual.dir and atual.chave != le:
                atual = atual.dir
            if atual.chave == le and atual.esq:
                atual = atual.esq
        while True:
            ponteiro_esq: No = atual
            anterior: No = atual
            palav: str = ""
            palav += pre
            while ponteiro_esq.esq:
                if ord(ponteiro_esq.esq.chave) == 42:
                    palav += ponteiro_esq.chave
                    resultado.append(palav)
                    if ponteiro_esq.dir:
                        anterior = ponteiro_esq
                        ponteiro_esq = ponteiro_esq.dir
                        palav = palav[0:-1]
                        continue
                else:
                    palav += ponteiro_esq.chave
                anterior = ponteiro_esq
                ponteiro_esq = ponteiro_esq.esq
            if not atual.dir:
                break
            atual = atual.dir

        resultado.sort()
        return resultado

    def sufixo(self, su: str) -> List[str]:
        atual: No = self.raiz
        resultado: List[str] = []
        while True:
            ponteiro_esq: No = atual
            anterior: No = atual
            palav: str = ""
            while ponteiro_esq.esq:
                if ord(ponteiro_esq.esq.chave) == 42:
                    palav += ponteiro_esq.chave
                    resultado.append(palav)
                    if ponteiro_esq.dir:
                        anterior = ponteiro_esq
                        ponteiro_esq = ponteiro_esq.dir
                        palav = palav[0:-1]
                        continue
                else:
                    palav += ponteiro_esq.chave
                anterior = ponteiro_esq
                ponteiro_esq = ponteiro_esq.esq
            if not atual.dir:
                break
            atual = atual.dir
        resultado.sort()
        result: List[str] = []
        for p in resultado:
            if p.endswith(su):
                result.append(p)
        result.sort()
        return result
