class Transporte:
    def __init__(self, *, ruedas:int, asientos:int):
        self.ruedas = ruedas
        self.asientos = asientos
        # self.x = 0
        # self.y = 0


    def desplazar(x:int, y:int = 0):
        print(f"El transporte se mueve {x} en horizontal y {y} en vertical")
        


    def informacion(self):
        print(f"El transporte tiene {self.ruedas} ruedas y {self.asientos} asientos")



def  main():
    coche = Transporte(4, 5)
    coche.desplazar(10, 34)
    coche.informacion(4, 5)
    


main()