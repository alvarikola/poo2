ERRORNUMBITS = 1
ERRORNUMBITSMSJ = "Número de bits incorrecto"

ERRORBITS = 2
ERRORBITSMSJ = "El string contiene caracteres distintos al 0 o 1"


BINVALUES = [128, 64, 32, 16, 8, 4, 2, 1]


def verifyDec8bit(theInput:str)->bool:
    if theInput >= 0 and theInput <= 255:
        return True
    return False

def verifyBinaryString(theInput:str)->int:
    if len(theInput) != 8:
        return ERRORNUMBITS
        
    
    for car in theInput:
        if car != "0" and car != "1":
            return ERRORBITS
        return False



def convertirBinDec(theInput:str)->int:  #int between 0-255
    result = 0

    for i in range(len(theInput)):
        if theInput[i] == "1":
            result += BINVALUES[i]

    return result

entrada = int(input("Introducir "))
# verifyResult = verifyBinaryString(entrada)

# if verifyResult == ERRORNUMBITS:
#     print(ERRORNUMBITSMSJ)
#     exit(-1)
# elif verifyResult == ERRORBITS:
#     print(ERRORBITSMSJ)
#     exit(-2)


# print(convertirBinDec(entrada))


# print(entrada)