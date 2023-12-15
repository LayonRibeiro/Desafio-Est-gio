class NumeroInvalido(Exception):
    def __init__(self):
        super().__init__("ATENÇÃO: número inválido")