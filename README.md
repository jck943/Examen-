# Examen
Esto es mi examen de 2ª EV
<br><br>

## Índice
1. [Datos que se han dado](#Datos)
2. [Primera función](#Primera)
3. [Segunda función](#Segunda)
4. [Función principal (Main)](#Main)

<br><br>
<div id="Datos"></div>

## Datos que se han dado
Los primeros datos que se han dado en el *classroom* han sido los siguientes: 
```py
def buscarPalabra(objetivo, palabras):


def imprimirListaInversa(lista):


nombres = ["Mengano", "Fulano", "Zutano", "Perantano"]
edades = {
    "Mengano": 0,
    "Fulano": 25,
    "Zutano": 50,
    "Perantano": 75
}
```
> Estos datos son necesarios para la realización del examen

### Explicación de los datos
- Se nos ha otorgado primero una función que se llama **`buscarPalabra`**, la cual se va a a utilizar para buscar una palabra dentro de una lista llamada _`nombres`_, que se muestra también en el programa. 

- Después también hay una función llamada **`imprimirListaInversa`**, la cual se va a utilizar para imprimir la lista en la parte superior del programa, cada vez que se inice el programa

- Por último se nos otorgan una lista y un diccionario llamados:
    - **`nombres`**: Que es la lista la cual guarda los nombres
    - **`edades`**: Diccionario que guarda los nombre como la _clave_ y las edades como el _valor_, se vería así en una tabla:

|         | Mengano | Fulano | Zutano | Perantano |
|---------|---------|--------|--------|-----------|
| Edades  |  0 años | 25 años| 50 años|  75 años  |

<br><br>
<div id="Primera"></div>

## Primera función
La primera función, `buscarPalabra`, se le pasan 2 parámetros:
- *objetivo*, que es la palabra que se va a tener que buscar    
- *palabras*, que es el array/lista de palabras donde se va a tener que buscar el objetivo.
Esta función devolverá un valor _`booleano`_, *verdadero* si la palabra *objetivo* se encuntra en el array/lista, y *falso* en caso contrario. En este caso es una función sencilla ya que solo hay que utilizar un bucle `if` `else` para verificar si la palabra ***objetivo*** se encontraba dentro de la lista, se ha realizado de la siguiente manera:
```py
def buscarPalabra(objetivo, palabras):
    if objetivo in palabras:
        return True
    else:
        return False
```

<br><br>
<div id="Segunda"></div>

## Segunda función
Para la segunda función, `imprimirListaInversa`, se le pasará un parámetro:
- *lista*: La lista la cual se invertirá
En este caso, se ha de invertir la lista, imprimir cada "objeto" que esté dentro de la lista y añadir un `"-"` antes de cada uno de ellos.
> Especifico que tienen que estar en líneas distintas cada nombre
Esto se ha hecho de la siguiente manera: 
```py
def imprimirListaInversa(lista):
    nueva_lista = []
    for i in range(len(lista) - 1, -1, -1):
        nueva_lista = lista[i]
        print("- " + nueva_lista)
```

### Pasos de razonamiento
1. Como se puede observar en la **función**, se crea una variable que inializa una `nueva_lista` vacía para que se vaya acumulando en esta.
2. Después se hace un bucle _for_, el cual empieza desde `len(lista) - 1` que es la longitud de la lista menos 1, termina en la posición de la lista `-1` y tiene un *step* (paso) de `-1`, cosa que hace que el bucle for se recorra hacia atrás.
3. Dentro del bucle `for` se asigna a la `nueva_lista` el valor de cada uno de los valores de la lista inicial.
4. Se imprime el resultado con el formato especificado

<br><br>
<div id="Main"></div>

## Función principal (Main)
Esta es la función en la cual se llama a todas las funciones, se tiene el bucle que hace que no termine de preguntar: `"Buscar nombre: "` y se tienen las listas almacenadas. El código es el siguiente: 
```py
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
```
### Explicación
- *`nombres y edades`*, son la lista y el diccionario.
- *`imprimirListaInversa(nombres)`*: es la lista que tiene que aparecer al principio
- *`while True`*: el bucle