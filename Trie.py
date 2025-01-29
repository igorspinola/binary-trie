from typing import Dict, List
from No import No

class Trie:
    def __init__(self) -> None:
        self.raiz: No = No()
        self.contador: Dict[str, int] = {}

    def insere(self, palavra: str) -> str:
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
