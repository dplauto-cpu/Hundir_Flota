import random
import numpy as np
from utils import (
    crear_tablero,
    imprimir_tablero,
    colocar_barco,
    colocar_barcos_jugador,
    colocar_barcos_ordenador,
    disparar,
    juego_terminado,
    disparo_ordenador)

def main(): # Da la bienvenida y las instrucciones de juego
    print(":" * 60)
    print("     BIENVENIDO A HUNDIR LA FLOTA - VERSIÓN SIMPLE")
    print(":" * 60)
    print("\nINSTRUCCIONES:")
    print("- Tablero de 10x10 (coordenadas del 0 al 9), coordenada: fila/ columna")
    print("- 6 barcos por jugador: 1 de tamaño 4, 2 de tamaño 3, 3 de tamaño 2")
    print("- Un disparo por turno: empiezas disparando tú")
    print("- La batalla termina cuando un jugador hunde todos los barcos enemigos")
    input("\nPulsa ENTER para comenzar...")

    
    # Imprime los tableros
    print("\n" + ":" * 60)
    print("POR FAVOR, ESPERE, COLOCANDO BARCOS...")
    print(":" * 60)

    # Tableros jugador, registra disparos de jugador a ordenador
    tablero_barcos_jugador = colocar_barcos_jugador()
    tablero_disparos_jugador = crear_tablero()  
    
    # Tableros del ordenador, registra disparos de ordenador a jugador
    tablero_barcos_ordenador = colocar_barcos_ordenador()
    tablero_disparos_ordenador = crear_tablero()  
    
    print("Barcos colocados aleatoriamente para ambos jugadores")
    print("Leyenda: X = Tocado | o = Disparo al agua | B = Barco | ~ = Agua de mar") 

    # Estadistica, muy simple, cada disparo, van de 1 en 1
    disparos_jugador = 0
    disparos_ordenador = 0
    
    '''
    Bucle principal que controla el flujo del juego.
    Alterna turnos entre jugador y ordenador hasta que alguien gana.
    '''
    turno_jugador = True  # Empieza el jugador 
    
    while True:
        if turno_jugador:             # Turno del jugador
            print("\n" + ":" * 60)
            print("TABLERO DE DISPAROS (a la flota enemiga):")
            print("Leyenda: X = Tocado | o = Fallo enemigo | B = Barco activo | ~ = Agua")
            print(":" * 60)
            imprimir_tablero(tablero_disparos_jugador, ocultar_barcos=False) #xa ver \
            # disparos realizados
            
            #print("\n" + "-" * 60) # Xa ver barcos ordenador, no muy emocionante pero...
            #print("TABLERO DEL ORDENADOR:")  
            #print("Leyenda: X = Tocado | o = Fallo enemigo | B = Barco activo | ~ = Agua")
            #print("-" * 60)
            #imprimir_tablero(tablero_barcos_ordenador, ocultar_barcos=False) 

            print("\n" + "-" * 60)
            print("TUS BARCOS (disparos del ordenador a tu flota):")
            print("Leyenda: X = Tocado | o = Fallo enemigo | B = Barco activo | ~ = Agua")
            print("-" * 60)
            imprimir_tablero(tablero_barcos_jugador, ocultar_barcos=False)
            
            # Solicita coordenadas al jugador para disparar
            while True:
                try:
                    print("\n" + "-" * 60)
                    fila = int(input("Ingresa la fila (0-9): "))
                    col = int(input("Ingresa la columna (0-9): "))
                    
                    if fila < 0 or fila > 9 or col < 0 or col > 9:
                        print("Coordenadas invalidas. Deben estar entre 0 y 9.")
                        continue
                    
                    # Dispara
                    resultado = disparar(tablero_barcos_ordenador, tablero_disparos_jugador, fila, col)
                    
                    if resultado == "ya disparado":
                        print("¿Otra vez aquí?, ¡madre mía, ponte gafas!")
                        continue
                    elif resultado == "tocado":
                        print("\n¡Toma petardo, Ricardo!")
                    else:
                        print("\nAgüita para baldear la cubierta")
                    
                    disparos_jugador += 1
                    break
                    
                except ValueError:
                    print("Por favor, ingresa numeros validos.")
            
            # Para terminar el juego
            if juego_terminado(tablero_barcos_ordenador):
                print("\n" + ":" * 60)
                print("¡BRAVO TORPEDO! HAS DEJADO AL ORDENADOR SIN FLOTA!")
                print(f"Has disparado {disparos_jugador} torpedos.")
                print(f"El ordenador ha disparado {disparos_ordenador} torpedos.")
                print(":" * 60)
                
                # Tableros finales
                print("\nTABLERO FINAL DEL ORDENADOR (tus disparos):")
                imprimir_tablero(tablero_disparos_jugador, ocultar_barcos=False)
                print("\nTABLERO FINAL DEL JUGADOR (disparos del ordenador):")
                imprimir_tablero(tablero_disparos_ordenador, ocultar_barcos=False)
                break
            
            # Cambio de turno
            turno_jugador = False
            input("\nPulsa ENTER para el turno del ordenador...")
            
        else:
            # TURNO DEL ORDENADOR
            print("\n" + ":" * 60)
            print("TURNO DEL ORDENADOR")
            print(":" * 60)
            
            # tablero del jugador con disparos recibidos
            print("\nDisparos recibidos")
            print("X = Tocado | o = Disparo al agua | B = Barco activo | ~ = Agua de mar")
            print("-" * 60)
            imprimir_tablero(tablero_disparos_ordenador, ocultar_barcos=False)
            
            # Ordenador dispara
            fila, col, resultado = disparo_ordenador(tablero_barcos_jugador, tablero_disparos_ordenador)
            disparos_ordenador += 1
            
            print(f"\nEnemigo dispara en ({fila}, {col})...")
            if resultado == "tocado":
                print("¡Tocado, ay, ay, ay!")
            else:
                print("Buff, que alivio, ha malgastado un torpedo")
            
            # Para terminar el juego
            if juego_terminado(tablero_barcos_jugador):
                print("\n" + ":" * 60)
                print("¡SE ACABÓ LO QUE SE DABA! te has quedado sin flota.")
                print(f"Disparos del ordenador: {disparos_ordenador}")
                print(f"Tus disparos: {disparos_jugador}")
                print(":" * 60)
                
                # Tableros finales
                print("\nTABLERO FINAL DEL JUGADOR (tus barcos y disparos recibidos):")
                imprimir_tablero(tablero_disparos_ordenador, ocultar_barcos=False)
                break
            
            # Cambio turno
            turno_jugador = True
            input("\nPulsa ENTER para tu turno...")

if __name__ == "__main__":
    main()