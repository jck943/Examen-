def buscarPalabra(objetivo, palabras):
    if objetivo in palabras:
        print("True")
    else:
        print("False")

def imprimirListaInversa(lista):
    

nombres = ["Mengano", "Fulano", "Zutano", "Perantano"]
edades = {
    "Mengano": 0,
    "Fulano": 25,
    "Zutano": 50,
    "Perantano": 75
}

objetivo = input("Buscar nombre: ")
buscarPalabra(objetivo, nombres)