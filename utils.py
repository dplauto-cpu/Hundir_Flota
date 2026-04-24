#PASO 0,  
import numpy as np
import random

def crear_tablero(): 
        return np.full((10, 10), "~", dtype=str) 
'''
    PASO 1
    Crea un tablero de 10x10, todas las casillas son str.
'''

def imprimir_tablero(tablero, ocultar_barcos=True):
    print("   " + " ".join(str(i) for i in range(10)))  # Numeros de columnas
    for i in range(10):
        if ocultar_barcos:# xa el tablero de disparos
            fila_mostrar = []
            for j in range(10):
                if tablero[i][j] == 'B':
                    fila_mostrar.append('~')  # Oculta posición barco, muestra '~'
                else:
                    fila_mostrar.append(tablero[i][j])  # Muestra 'X'/'o' al disparar
            print(f"{i:2} | " + " ".join(fila_mostrar))
        else:
            print(f"{i:2} | " + " ".join(tablero[i]))  # Esto debería mostrar todo

'''
   PASO 2
   Imprime un tablero con los elementos básicos agua, barcos y disparos (dos tipos).
   Ocultar barcos es booleano: False es la posición real, True el jugador ve agua.
'''

def colocar_barco(tablero, tamano):
    while True:
        orientacion = random.choice(['H', 'V'])  # H: Horizontal, V: Vertical
        if orientacion == 'H': # H, la fila fija y la columna variable
            fila = random.randint(0, 9)
            col = random.randint(0, 9 - tamano)  # xa que quepa
            if all(tablero[fila][col + i] == '~' for i in range(tamano)):#sólo en casilla vacía
                for i in range(tamano):
                    tablero[fila][col + i] = 'B'  
                return
        else:  # V, columna fija y fila variable
            fila = random.randint(0, 9 - tamano)
            col = random.randint(0, 9)
            if all(tablero[fila + i][col] == '~' for i in range(tamano)):
                for i in range(tamano):
                    tablero[fila + i][col] = 'B'
                return
'''
    PASO 3
    Coloca un barco de forma aleatoria.
    Define tamaño y tablero.
'''

def colocar_barcos_jugador():
    tablero = crear_tablero()
    barcos = [4, 3, 3, 2, 2, 2]  
    for tamano in barcos:
        colocar_barco(tablero, tamano)
    return tablero
'''
    PASO 4
    Coloca los 6 barcos en tablero del jugador aleatoriamente.
    Permite posiciones contiguas.
    Define el tamaño de los barcos: 1 de 4 casillas, 2 de 3 casillas, 3 de 2 casillas.
'''

def colocar_barcos_ordenador():
    tablero = crear_tablero()
    barcos = [4, 3, 3, 2, 2, 2]
    for tamano in barcos:
        colocar_barco(tablero, tamano)
    return tablero
'''
   PASO 5
    Coloca los 6 barcos en tablero del ordenador.
    Es igual que colocar_barcos_jugador.
'''

def disparar(tablero_barcos, tablero_disparos, fila, col):
    if tablero_disparos[fila][col] in ['X', 'o']: # marca los impactos y las aguas
        return "ya disparado"
    if tablero_barcos[fila][col] == 'B': # # si hay barco en el tablero oculto
        tablero_disparos[fila][col] = 'X'  # tocado, marca X en tablero disparos
        return "tocado"
    else:
        tablero_disparos[fila][col] = 'o'  # xa diferenciar agua donde ya se ha disparado
        return "agua"

'''
    PASO 6
    Turno de disparo del jugador.
    Dispara en las coordenadas introducidas [fila] [columna].
    No permite disparar dos veces en el mismo sitio.
    Refleja el resultado del disparo en tablero del jugador:
    'X' indica barco tocado, 'H' barco hundido, 'o' agua (cambia por '~').
'''

def disparo_ordenador(tablero_barcos_jugador, tablero_disparos_ordenador):
    while True:
        fila = random.randint(0, 9)
        col = random.randint(0, 9)
        if tablero_disparos_ordenador[fila][col] == '~': # ~ = nunca disparó aquí
            resultado = disparar(tablero_barcos_jugador, tablero_disparos_ordenador, fila, col)
            return fila, col, resultado
'''
    PASO 7
    Turno de disparo del ordenador.
    El ordenador elige coordenadas aleatorias, también usa la función disparar.
'''

def juego_terminado(tablero_barcos):
    for i in range(10):
        for j in range(10):
            if tablero_barcos[i][j] == 'B':
                return False  # Todavia quedan barcos
    return True  # Todos los barcos hundidos
'''
    PASO 8
    La batalla termina cuando todos los barcos han sido hundidos, 
    no quedan 'B's en el tablero.
'''