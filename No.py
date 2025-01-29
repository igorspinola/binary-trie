from typing import List

class No:
    def __init__(self,  chave: str= "") -> None:
        self.ref: List[No] = []
        self.chave: str = chave
