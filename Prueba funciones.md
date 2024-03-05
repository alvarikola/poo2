### Parámetro posicional 
def tipicaFuncion(unpar:int, dospar:int)->None:
#def tipicaFuncion(unpar:int, dospar:int, /)->None:              #Cuidado con el carácter /
    pass


tipicaFuncion(3, 6)
#unpar = 3
#dospar = 6


### Parámetro con valor por defecto
def tipicaFuncion(unpar: int, dospar = 6:int)->None:
    pass


tipicaFuncion(3)
#unpar = 3
#dospar = 6


### Parámetro arbitrario
def tipicaFuncion(unpar:int, *dospar:int, content:int)->None:
    pass


tipicaFuncion(3, 6, 6, 6, content = 3)


### Parámetro nominal
def tipicaFuncion(*,unpar:int, dospar:int)->None:          #El caracter * es para saber que es nominal seguro
    pass


tipicaFuncion(dospar = 6, unpar = 3)
#unpar = 3
#dospar = 6


### Ejercicio 3
def myDiv(id:str, *clas:str, content:str)->str:
    resultado = ''

    resultado += '<div id=""' + id + '"'

    if len(clas) != 0:
        resultado += 'class = "'

        for e in clas:
            resultado += e + ','

        resultado += '"'

    resultado += '>' + content + '</div>'
    return resultado


### Ejercicio 5
def myScript(*scr:str)->str:
Función que tiene como entrada un número indeterminado de cadenas de caracteres y como salida una cadena de caracteres. Probablemente transforma las entradas en la salida.