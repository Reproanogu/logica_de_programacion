#Biblioteca de tableros
import random
tableros_facil = [
    {
        "puzzle": [
            [5, 3, 0, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ],
        "solucion": [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ]
    },
    {
        "puzzle": [
            [0, 0, 3, 0, 2, 0, 6, 0, 0],
            [9, 0, 0, 3, 0, 5, 0, 0, 1],
            [0, 0, 1, 8, 0, 6, 4, 0, 0],
            [0, 0, 8, 1, 0, 2, 9, 0, 0],
            [7, 0, 0, 0, 0, 0, 0, 0, 8],
            [0, 0, 6, 7, 0, 8, 2, 0, 0],
            [0, 0, 2, 6, 0, 9, 5, 0, 0],
            [8, 0, 0, 2, 0, 3, 0, 0, 9],
            [0, 0, 5, 0, 1, 0, 3, 0, 0]
        ],
        "solucion": [
            [4, 8, 3, 9, 2, 1, 6, 5, 7],
            [9, 6, 7, 3, 4, 5, 8, 2, 1],
            [2, 5, 1, 8, 7, 6, 4, 9, 3],
            [5, 4, 8, 1, 3, 2, 9, 7, 6],
            [7, 2, 9, 5, 6, 4, 1, 3, 8],
            [1, 3, 6, 7, 9, 8, 2, 4, 5],
            [3, 7, 2, 6, 8, 9, 5, 1, 4],
            [8, 1, 4, 2, 5, 3, 7, 6, 9],
            [6, 9, 5, 4, 1, 7, 3, 8, 2]
        ]
    }
]

tableros_medio = [
    {
        "puzzle": [
            [0, 2, 0, 6, 0, 8, 0, 0, 0],
            [5, 8, 0, 0, 0, 9, 7, 0, 0],
            [0, 0, 0, 0, 4, 0, 0, 0, 0],
            [3, 7, 0, 0, 0, 0, 5, 0, 0],
            [6, 0, 0, 0, 0, 0, 0, 0, 4],
            [0, 0, 8, 0, 0, 0, 0, 1, 3],
            [0, 0, 0, 0, 2, 0, 0, 0, 0],
            [0, 0, 9, 8, 0, 0, 0, 3, 6],
            [0, 0, 0, 3, 0, 6, 0, 9, 0]
        ],
        "solucion": [
            [1, 2, 3, 6, 7, 8, 9, 4, 5],
            [5, 8, 4, 2, 3, 9, 7, 6, 1],
            [9, 6, 7, 1, 4, 5, 3, 2, 8],
            [3, 7, 2, 4, 6, 1, 5, 8, 9],
            [6, 9, 1, 5, 8, 3, 2, 7, 4],
            [4, 5, 8, 7, 9, 2, 6, 1, 3],
            [7, 1, 5, 9, 2, 4, 8, 6, 3],  
            [2, 4, 9, 8, 5, 7, 1, 3, 6],
            [8, 3, 6, 3, 1, 6, 4, 9, 7]
        ]
    },
    {
        "puzzle": [
            [0, 0, 0, 2, 6, 0, 7, 0, 1],
            [6, 8, 0, 0, 7, 0, 0, 9, 0],
            [1, 9, 0, 0, 0, 4, 5, 0, 0],
            [8, 2, 0, 1, 0, 0, 0, 4, 0],
            [0, 0, 4, 6, 0, 2, 9, 0, 0],
            [0, 5, 0, 0, 0, 3, 0, 2, 8],
            [0, 0, 9, 3, 0, 0, 0, 7, 4],
            [0, 4, 0, 0, 5, 0, 0, 3, 6],
            [7, 0, 3, 0, 1, 8, 0, 0, 0]
        ],
        "solucion": [
            [4, 3, 5, 2, 6, 9, 7, 8, 1],
            [6, 8, 2, 5, 7, 1, 4, 9, 3],
            [1, 9, 7, 8, 3, 4, 5, 6, 2],
            [8, 2, 6, 1, 9, 5, 3, 4, 7],
            [3, 7, 4, 6, 8, 2, 9, 1, 5],
            [9, 5, 1, 7, 4, 3, 6, 2, 8],
            [5, 1, 9, 3, 2, 6, 8, 7, 4],
            [2, 4, 8, 9, 5, 7, 1, 3, 6],
            [7, 6, 3, 4, 1, 8, 2, 5, 9]
        ]
    }
]

tableros_dificil = [
    {
        "puzzle": [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 3, 0, 8, 5],
            [0, 0, 1, 0, 2, 0, 0, 0, 0],
            [0, 0, 0, 5, 0, 7, 0, 0, 0],
            [0, 0, 4, 0, 0, 0, 1, 0, 0],
            [0, 9, 0, 0, 0, 0, 0, 0, 0],
            [5, 0, 0, 0, 0, 0, 0, 7, 3],
            [0, 0, 2, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 4, 0, 0, 0, 9]
        ],
        "solucion": [
            [9, 8, 7, 6, 5, 4, 3, 2, 1],
            [2, 4, 6, 1, 7, 3, 9, 8, 5],
            [3, 5, 1, 9, 2, 8, 7, 4, 6],
            [1, 2, 8, 5, 3, 7, 6, 9, 4],
            [6, 3, 4, 8, 9, 2, 1, 5, 7],
            [7, 9, 5, 4, 6, 1, 8, 3, 2],
            [5, 1, 9, 2, 8, 6, 4, 7, 3],
            [4, 7, 2, 3, 1, 9, 5, 6, 8],
            [8, 6, 3, 7, 4, 5, 2, 1, 9]
        ]
    },
    {
        "puzzle": [
            [0, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 6, 0, 0, 0, 0, 3],
            [0, 7, 4, 0, 8, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 3, 0, 0, 2],
            [0, 8, 0, 0, 4, 0, 0, 1, 0],
            [6, 0, 0, 5, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 7, 8, 0],
            [5, 0, 0, 0, 0, 9, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 4, 0]
        ],
        "solucion": [
            [1, 2, 6, 4, 3, 7, 9, 5, 8],
            [8, 9, 5, 6, 2, 1, 4, 7, 3],
            [3, 7, 4, 9, 8, 5, 1, 2, 6],
            [4, 5, 7, 1, 9, 3, 8, 6, 2],
            [9, 8, 3, 2, 4, 6, 5, 1, 7],
            [6, 1, 2, 5, 7, 8, 3, 9, 4],
            [2, 6, 9, 3, 1, 4, 7, 8, 5],
            [5, 4, 8, 7, 6, 9, 2, 3, 1],
            [7, 3, 1, 8, 5, 2, 6, 4, 9]
        ]
    }
]

#Configuración
##Menú
print("Bienvenido")
print("Escribe el número del nivel que quieres jugar")
print("1. Fácil")
print("2. Medio")
print("3. Difícil")

##Selección
nivel_de_juego = 0
confirmacion_de_nivel = "no"

while confirmacion_de_nivel == "no":
    #Pedir nivel válido
    while nivel_de_juego not in [1, 2, 3]:
        nivel_de_juego = int(input("Ingresa 1, 2 o 3: "))
    
    #Mostrar dificultad seleccionada
    if nivel_de_juego == 1:
        dificultad = "Fácil"
    elif nivel_de_juego == 2:
        dificultad = "Medio"
    elif nivel_de_juego == 3:
        dificultad = "Difícil"
    print("Seleccionaste:", dificultad)

    #Confirmar
    confirmacion_de_nivel = input("¿Quieres continuar en ese nivel? (si/no): ")
    
    if confirmacion_de_nivel == "no":
        nivel_de_juego = 0  # resetear para volver a pedir
    elif confirmacion_de_nivel != "si":
        print(input("No válido, escribe si o no "))



#Generación de tablero
if nivel_de_juego == 1:
    seleccion = random.choice(tableros_facil)
elif nivel_de_juego == 2:
    seleccion = random.choice(tableros_medio)
elif nivel_de_juego == 3:
    seleccion = random.choice(tableros_dificil)

tablero = seleccion["puzzle"]
solucion = seleccion["solucion"]

def mostrar_tablero(tablero):
    for i in range(9):  #evalúa las 9 filas
        if i % 3 == 0 and i != 0:
            print("------+-------+------")
        for j in range(9):  #evalúa las 9 colúmnas
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if tablero[i][j] == 0:
                print(".", end=" ")  # los ceros se muestran como punto
            else:
                print(tablero[i][j], end=" ")
        print() 

mostrar_tablero(tablero)

#Detectar vitoria
def detectar_victoria(tablero):
    for fila in range(9):
        for columna in range(9):
            if tablero[fila][columna] == 0:
                return False
            
    return True    
    
while not detectar_victoria(tablero):
##Ingresar números
#Seleccionar fila
 fila = 0
 while fila not in range(1, 10):
    fila = int(input("Selecciona la fila (1-9): "))
    if fila not in range(1, 10):
        print("Opción no válida, intenta de nuevo")
 fila = fila - 1  # convertir a índice 0-8

# Seleccionar columna
 columna = 0
 while columna not in range(1, 10):
    columna = int(input("Selecciona la columna (1-9): "))
    if columna not in range(1, 10):
        print("Opción no válida, intenta de nuevo")
 columna = columna - 1  # convertir a índice 0-8

# Seleccionar número
 numero_seleccionado = 0
 while numero_seleccionado not in range(1, 10):
    numero_seleccionado = int(input("Escribe un número (1-9): "))
    if numero_seleccionado not in range(1, 10):
        print("Opción no válida, intenta de nuevo")

#Validación
 if tablero[fila][columna] != 0:
    print("Esa celda ya tiene un número, elige otra")
 elif numero_seleccionado == solucion[fila][columna]:
    tablero[fila][columna] = numero_seleccionado
    print("¡Jugada correcta!")
    mostrar_tablero(tablero)
 else:
    print("¡Número incorrecto, intenta de nuevo!")

if detectar_victoria(tablero):
    print("¡Felicidades, ganaste!")
