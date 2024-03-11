class Transporte:
    def __init__(self, *, ruedas:int, asientos:int):
        self.ruedas = ruedas
        self.asientos = asientos


    def desplazar(self, x:int, y:int = 0):
        print(f"El transporte se mueve {x} en horizontal y {y} en vertical")
        


    def informacion(self):
        print(f"El transporte tiene {self.ruedas} ruedas y {self.asientos} asientos")

