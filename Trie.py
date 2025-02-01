from typing import Dict, List
from No import No

class Trie:
    def __init__(self) -> None:
        self.raiz: No = No()
        self.contador: Dict[str, int] = {}

    def insere(self, palavra: str) -> str:
        #print(self.consulta(palavra, False))
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
            temp: No | None = No()
            nova_primeira_letra: bool = False
            # posso colocar essa lógica em uma funcao e chamar ela toda vez que precisar!!
            # usar u i para possivelmente generalizar os seguintes loops
            for i in range(len(palavra)):
                if not nova_primeira_letra:
                    while atual.dir and ord(palavra[i]) > ord(atual.dir.chave):
                        atual = atual.dir
                    if atual.dir and ord(atual.dir.chave) != ord(palavra[i]):
                        nova_primeira_letra = True
                        temp = atual.dir
                        atual.dir = No(palavra[i])
                        if temp:
                            atual.dir.dir = temp
                    elif not atual.dir and ord(atual.chave) != ord(palavra[i]):
                        nova_primeira_letra = True
                        atual.dir = No(palavra[i])

                    if atual.dir:
                        atual = atual.dir

                    # if atual.esq:
                    #     atual = atual.esq
                elif not atual.esq:
                    atual.esq = No(palavra[i])
                    #atual = atual.esq
                    if i == len(palavra) - 1:
                        atual.esq.esq = No("*")
                if atual.esq:
                    atual = atual.esq

            # while atual.dir and ord(palavra[0]) > ord(atual.dir.chave):
            #     atual = atual.dir
            # if atual.dir and ord(atual.dir.chave) != ord(palavra[0]):
            #     temp = atual.dir
            #     atual.dir = No(palavra[0])
            #     if temp:
            #         atual.dir.dir = temp

            # if atual.dir:
            #     atual = atual.dir

            # if atual.esq:
            #     atual = atual.esq

            # while atual.dir and ord(palavra[1]) > ord(atual.dir.chave):
            #     atual = atual.dir
            # if atual.dir and ord(atual.dir.chave) != ord(palavra[1]):
            #     temp = atual.dir
            #     atual.dir = No(palavra[1])
            #     if temp:
            #         atual.dir.dir = temp
            # if atual.dir:
            #     atual = atual.dir
            # for ch in range(2, len(palavra)):
            #     atual.esq = No(palavra[ch])
            #     if ch == len(palavra) - 1:
            #         atual.esq.esq = No("*")
            #     atual = atual.esq

        return f"palavra inserida: {palavra}"

    def consulta(self, palavra: str, incrementaContador:bool = True) -> str:
        atual: No = self.raiz
        palavra += "*"
        for i,le in enumerate(palavra):
            # print(f"letra: {le}")
            while atual.dir and atual.chave != le:
                atual = atual.dir
            if not atual.dir and i != len(palavra) - 1 and atual.chave == "*":
                break
            # if atual.dir and atual.chave == "*" and i != len(palavra) - 1:
            #     atual = atual.dir
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
            # if atual.esq:
                # print(f"atual.chave: {atual.chave} atual.esq: {atual.esq.chave}")
            # if atual.dir:
                # print(f"atual.dir:{atual.dir.chave}")
            if atual.chave == le and atual.esq:
                # print("entrou")
                atual = atual.esq
                # if atual.chave == "o" or le == "i":
                    # print(f"indice: {i} letra: {le} atual.chave: {atual.chave} dps da mudanca")

            # elif atual.chave != le and atual.dir:
            #     # print("entrou aqui 22222")
            #     atual = atual.dir
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

    def imprimir(self, no: No, ehRaiz: bool = True) -> None:
        pass

    def imprimir_arvore(self) -> None:
        self.imprimir(self.raiz)

    def imprimir_(self) -> None:
        pass

    def prefixo(self, pre: str):
        pass
    def sufixo(self, su: str):
        pass
