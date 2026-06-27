## Descripción

Juego de Sudoku desarrollado en Python para la materia de Lógica de Programación. Permite seleccionar un nivel de dificultad, jugar en consola y valida automáticamente las jugadas hasta completar el tablero.

---

## Tabla de Contenidos

- [Requisitos] (#️-requisitos--prerrequisitos)
- [Estructura del Proyecto] (#-estructura-del-proyecto)
- [Cómo Jugar] (#-cómo-jugar)
- [Versiones del Código] (#-versiones-del-código)
- [Documentación Adicional] (#-documentación-adicional)

---

## Requisitos / Prerrequisitos

Antes de ejecutar el proyecto, necesitas tener instalado:

- Python 3.10 o superior → [Descargar Python](https://www.python.org/downloads/)
- Un editor de código (recomendado: [Visual Studio Code](https://code.visualstudio.com/))
- No se requieren librerías externas — el proyecto usa únicamente librerías estándar de Python (`random`)

---

## Estructura del Proyecto

Sudoku v1.py              # Versión 1: validación con funciones
Sudoku v2.py              # Versión 2: validación contra solución
README.md                 # Este archivo
diagrama_flujo.png        # Diagrama de flujo del juego
diagrama_casos_uso.png    # Diagrama de casos de uso
glosario_variables.docx   # Biblioteca/glosario de variables

---

## Cómo Jugar

1. Al iniciar, selecciona el nivel de dificultad: **Fácil**, **Medio** o **Difícil**.
2. Confirma tu elección.
3. El tablero se mostrará en consola, donde los espacios vacíos se representan con un punto (`.`).
4. Ingresa la fila (1-9), la columna (1-9) y el número (1-9) que deseas colocar.
5. El programa validará automáticamente la jugada:
   - Si la celda ya está ocupada, te lo indicará.
   - Si el número es incorrecto para esa posición, te lo indicará.
   - Si es correcto, se actualizará el tablero.
6. El juego termina cuando completas todas las celdas correctamente. 

---

## Versiones del Código

El proyecto contiene dos versiones con distintos enfoques de validación, desarrolladas como parte del proceso de aprendizaje:

### Sudoku v1.py

Valida la jugada del usuario mediante funciones independientes que revisan las reglas del Sudoku:
- validar_fila — verifica que el número no se repita en la fila
- validar_columna — verifica que el número no se repita en la columna
- validar_cuadrante — verifica que el número no se repita en el cuadro 3x3


### Sudoku v2.py

Valida la jugada comparando directamente contra la solución precargada de cada tablero:
- Cada tablero incluye un "puzzle" (lo que ve el jugador) y una "solución" (la respuesta correcta, oculta al usuario).
- Se compara "numero_seleccionado" contra "solucion[fila][columna]".

---

##  Documentación Adicional

En el repositorio también se incluyen:

- Diagrama de flujo
- Diagrama de casos de uso
- Diagrama de arquitectura
- Biblioteca de variables 

---
