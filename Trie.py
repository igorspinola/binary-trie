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
            anterior: No = self.raiz
            temp: No | None = No()
            nova_primeira_letra: bool = False
            # posso colocar essa lógica em uma funcao e chamar ela toda vez que precisar!!
            # usar u i para possivelmente generalizar os seguintes loops
            for i in range(len(palavra)):
                if(palavra == "casam"):
                    print(f"atual.chave: {atual.chave} palavra[i]: {palavra[i]} teste")
                if atual.esq and atual.chave == palavra[i] and i != len(palavra) - 1:
                    anterior = atual
                    atual = atual.esq
                    continue
                # elif not atual.esq and atual.chave == palavra[i] and i != len(palavra) - 1:
                #     continue
                elif atual.esq and i == len(palavra) - 1 and atual.chave == palavra[i]:
                    temp = atual.esq
                    atual.esq = No("*")
                    atual.esq.dir = temp
                # elif atual.esq and i == len(palavra) - 1 and atual.chave != palavra[i]:
                #     temp = atual.esq
                #     atual.esq = No("*")
                #     atual.esq.dir = temp
                elif not atual.esq and i == len(palavra) - 1 and atual.chave == palavra[i]:
                    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    # checar esse elif aqui achei estranho
                    atual.esq = No("*")
                    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    # checar esse elif aqui achei estranho
                elif not nova_primeira_letra:
                    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    #checar se essa mudança nao quebrou nada
                    # while atual.dir and ord(atual.dir.chave) <= ord(palavra[i]):
                    #     anterior = atual
                    #     atual = atual.dir
                    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    # while atual.dir and ord(palavra[i]) > ord(atual.dir.chave):
                    #     anterior = atual
                    #     atual = atual.dir
                    # while atual.esq and atual.chave == palavra[i]:
                    #     anterior = atual
                    #     atual = atual.esq
                    if ord(atual.chave) > ord(palavra[i]) and anterior != atual:
                        if(palavra == "casam"):
                            print(f"atual.chave: {atual.chave} palavra[i]: {palavra[i]} entrou aqui 111")
                        nova_primeira_letra = True
                        temp = atual
                        anterior.esq = No(palavra[i])
                        anterior.esq.dir = temp
                        atual = anterior.esq
                        if i == len(palavra) - 1:
                            atual.esq = No("*")
                    elif ord(atual.chave) < ord(palavra[i]) and anterior != atual:
                        if(palavra == "casam"):
                            print(f"atual.chave: {atual.chave} palavra[i]: {palavra[i]} entrou aqui 222")
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
                            #!!!!!!!!!!!!!!!!!!!!!!!!!!!
                            #checar se nao quebrou nada
                            #!!!!!!!!!!!!!!!!!!!!!!!!!!!
                            if atual.esq:
                                temp = anterior.esq
                                anterior.esq = No("*")
                                anterior.esq.dir = temp
                            elif not atual.esq:
                                atual.esq = No("*")
                    elif ord(atual.chave) < ord(palavra[i]) and anterior == atual:
                        nova_primeira_letra = True
                        if(palavra == "casam"):
                            print(f"atual.chave: {atual.chave} palavra[i]: {palavra[i]} entrou aqui 333")
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
                        if(palavra == "casam"):
                            print(f"atual.chave: {atual.chave} palavra[i]: {palavra[i]} entrou aqui 444")
                        nova_primeira_letra = True
                        nova_raiz = No(palavra[i])
                        self.raiz = nova_raiz
                        self.raiz.dir = atual
                        atual = self.raiz
                        anterior = self.raiz
                        if i == len(palavra) - 1:
                            atual.esq = No("*")
                    #/////// abaixo errado
                    # elif atual.dir and ord(atual.dir.chave) == ord(palavra[i]):
                    #     nova_primeira_letra = True
                    #     temp = atual.dir
                    #     atual.dir = No(palavra[i])
                    #     if temp:
                    #         atual.dir.dir = temp
                    #//////////
                    #
                    # elif not atual.dir and ord(atual.dir.chave) == ord(palavra[i]):
                    #     nova_primeira_letra = True
                    #     temp = atual.dir
                    #     atual.dir = No(palavra[i])
                    #     if temp:
                    #         atual.dir.dir = temp
                    # elif not atual.dir and ord(atual.chave) != ord(palavra[i]):
                    #     nova_primeira_letra = True
                    #     atual.dir = No(palavra[i])

                    # if atual.dir:
                    #     atual = atual.dir

                    # if atual.esq and ord(atual.esq.chave) < ord(palavra[i]):
                    #     atual = atual.esq
                    # if atual.esq:
                    #     atual = atual.esq
                elif not atual.esq:
                    if(palavra == "casam"):
                        print(f"atual.chave: {atual.chave} palavra[i]: {palavra[i]} entrou aqui 555")
                    atual.esq = No(palavra[i])
                    #atual = atual.esq
                    if i == len(palavra) - 1:
                        atual.esq.esq = No("*")
                    anterior = atual
                    atual = atual.esq
                # tava alterando aqui
                # melhor juntar tudo em elif pra ficar mais previsivel o comportamento:
                # if caso1:
                # elif caso 2:
                # elif caso 3:
                # if atual.esq and ord(atual.esq.chave) < ord(palavra[i]):
                #     atual = atual.esq

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
            # print("antes")
            # if atual.esq:
            #     print(f"atual.chave: {atual.chave} atual.esq: {atual.esq.chave} letra:{le}")
            # if atual.dir:
            #     print(f"atual.dir:{atual.dir.chave}")
            # print("/////////////////")
            while atual.dir and atual.chave != le:
                atual = atual.dir
            # print("depois")
            # if atual.esq:
            #     print(f"atual.chave: {atual.chave} atual.esq: {atual.esq.chave} letra:{le}")
            # if atual.dir:
            #     print(f"atual.dir:{atual.dir.chave}")
            # print("/////////////////")
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
            print(le)
            while atual.dir and atual.chave != le:
                atual = atual.dir
            print(f"atual.chave {atual.chave}")
            if atual.chave == le and atual.esq:
                atual = atual.esq
            print(f"atual.chave {atual.chave}")
        while True:
            ponteiro_esq: No = atual
            palav: str = ""
            palav += pre
            while ponteiro_esq.esq:
                print(f"ponteiro_esq.chave {ponteiro_esq.chave}")
                if ponteiro_esq.chave == "*":
                    resultado.append(palav)
                else:
                    palav += ponteiro_esq.chave
                ponteiro_esq = ponteiro_esq.esq
            if not atual.dir:
                break
            atual = atual.dir

        resultado.sort()
        return resultado

    def sufixo(self, su: str) -> List[str]:
        return []
