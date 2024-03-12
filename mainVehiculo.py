from automovil import Automovil
from bicicleta import Bicicleta
from camion import Camion
from moto import Moto


def main():
    automovil = Automovil(ruedas=4, color="rojo")
    bicicleta = Bicicleta(ruedas=2, color="verde")
    camion = Camion(ruedas=6, color="rojo y azul")
    moto = Moto(ruedas=2, color="naranja")

    automovil.info()
    bicicleta.info()
    camion.info()
    moto.info()



main()