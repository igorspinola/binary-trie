from typing import Dict, List
from No import No

class Trie:
    def __init__(self) -> None:
        self.raiz: No = No()
        self.contador: Dict[str, int] = {}

    def insere(self, palavra: str) -> str:
        if self.raiz.chave == "":
            self.raiz.chave = palavra[0]
        else:
            atual: No = self.raiz
            temp: No | None = No()
            # posso colocar essa lógica em uma funcao e chamar ela toda vez que precisar!!
            # usar u i para possivelmente generalizar os seguintes loops
            # while atual.dir:
                # i: int = 0
                # while atual.dir and ord(palavra[i]) > ord(atual.dir.chave):
                #     atual = atual.dir
                # if atual.dir and ord(atual.dir.chave) != ord(palavra[i]):
                #     temp = atual.dir
                #     atual.dir = No(palavra[i])
                #     if temp:
                #         atual.dir.dir = temp

                # if atual.dir:
                #     atual = atual.dir

                # if atual.esq:
                #     atual = atual.esq
                # i += 1
            #
            while atual.dir and ord(palavra[0]) > ord(atual.dir.chave):
                atual = atual.dir
            if atual.dir and ord(atual.dir.chave) != ord(palavra[0]):
                temp = atual.dir
                atual.dir = No(palavra[0])
                if temp:
                    atual.dir.dir = temp

            if atual.dir:
                atual = atual.dir

            if atual.esq:
                atual = atual.esq

            while atual.dir and ord(palavra[1]) > ord(atual.dir.chave):
                atual = atual.dir
            if atual.dir and ord(atual.dir.chave) != ord(palavra[1]):
                temp = atual.dir
                atual.dir = No(palavra[1])
                if temp:
                    atual.dir.dir = temp
            if atual.dir:
                atual = atual.dir
            for ch in range(2, len(palavra)):
                atual.esq = No(palavra[ch])
                if ch == len(palavra) - 1:
                    atual.esq.esq = No("*")
                atual = atual.esq

        output: str = ""
        return output

    def consulta(self, palavra: str) -> str:
        output: str = ""
        return output

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
