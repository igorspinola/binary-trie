
class No:
    def __init__(self,  chave: str= "") -> None:
        self.dir: No | None = None
        self.esq: No | None = None
        self.chave: str = chave
