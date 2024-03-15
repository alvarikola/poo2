class FileWriter:
    def __init__(self, filename:str):
        self.filename = filename
        self.i = open(self.filename, "w+r")

    def write(self, mensaje:str):
        self.i.write(mensaje)


    def read(self)->str:
        return self.i.readlines()

    
    def close(self):
        self.i.close()



def main():
    prueba = FileWriter("hola.txt")
    prueba.write("hola buenos dias")
    prueba.close()
    prueba = FileWriter("hola.txt")
    prueba.read()
    prueba.close()



main()