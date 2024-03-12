class Vehiculo:
    def __init__(self, ruedas:int, color:str) -> None:
        self.ruedas = ruedas
        self.color = color

    def info(self):
        print(f"El vehículo tiene {self.ruedas} ruedas y es de color {self.color}")



