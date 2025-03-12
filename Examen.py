def buscarPalabra(objetivo, palabras):
    if objetivo in palabras:
        return True
    else:
        return False
 
def imprimirListaInversa(lista):
    nueva_lista = []
    for i in range(len(lista) - 1, -1, -1):
        nueva_lista = lista[i]
        print("- " + nueva_lista)

nombres = ["Mengano", "Fulano", "Zutano", "Perantano"]
edades = {
    "Mengano": 0,
    "Fulano": 25,
    "Zutano": 50,
    "Perantano": 75
}
imprimirListaInversa(nombres)
while True:
    print()
    objetivo = input("Buscar nombre: ")
    if objetivo == "exit":
        print("\nFIN DEL PROGRAMA")
        break
    elif buscarPalabra(objetivo, nombres) == True:
        print(objetivo + " tiene " + str(edades[objetivo]) + " años")
    else:
        print("El nombre no existe...")