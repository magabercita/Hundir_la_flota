## PARA EJECUTARLO EN LA TERMINAL una vez estemos dentro de la carpeta:
# python "HUNDIR LA FOTA - Dani Fernández y Bea Mínguez_2023-10-13.py"

from PIL import Image
import numpy as np
import random

battleship = Image.open('C:\\Users\\Usuario\\Documents\\THE BRIDGE\\TRABAJOS\\Bea_trabajo\\Hundir la Flota - Dani,Bea\\imagenes\\Battleship_Dani y Bea.jpg')
battleship.show()


########### FUNCIÓN DE CREAR TABLERO CON SEPARACIONES POR AGUA Y DENTRO DEL TABLERO ###########

def crea_tablero():
    '''
    Función para crear coordenadas aleatorias de barcos para el juego Hundir La Flota.
    Pensado para un tablero de 10x10.
        VARIABLES:
            tablero = 10x10
            barcos = variable para llevar la cuenta de barcos puestos en el tablero.
            tamanos = eslora de los barcos(ocuparán casillas seguidas en horizontal o vertical no en diagonal)
            hv = aleatoriamente nos dará la orientación del barco que será en vertical u horizontal.
            coord_fila = dara un número aleatorio entre la fila 0 y la fila 9 del tablero.
            coord_col = dara un número aleatorio entre la columna 0 y la columna 9 del tablero.    
            longitud_x = es el resultado de la coordenada de columna (+ el tamaño del barco en el caso de que salga horizontal).
            longitud_y = es el resultado de la coordenada de fila ( + tamano en el caso de que salga vertical).    
            choque = variable que nos dará el resultado de si los barcos se chocan o no cumplen el espacio de separación entre ellos (tiene que haber agua alrededor de ellos).
                    Esta variable se apoya en otras para definirse: fila_inicio, fila_fin, columna_inicio, columna_fin.
            tablero_vacio = tablero sin marcas con el que el jugador irá anotando los disparos que realice para averiguar los barcos de la IA.
            tablero_barcos_j = tablero del jugador donde se marcan sus barcos con la letra 'B'.
            tablero_adivinar = tablero de la IA con sus barcos marcados con la letra 'B'.
    '''

    tablero = np.full((10, 10), " ")

    barcos = 0
    tamanos = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

    while barcos < len(tamanos) :
        tamano = tamanos[barcos]
        hv = np.random.choice(["v", "h"])
        coord_fila = np.random.randint(0, 10)
        coord_col = np.random.randint(0, 10)

        #### INICIALIZA VALORES BARCO ####
        if hv == "h":
            longitud_x = coord_col + tamano
            longitud_y = coord_fila 

        if hv == "v":
            longitud_x = coord_col
            longitud_y = coord_fila + tamano
        

        #### COMPRUEBA SI EL BARCO ENTRA EN EL TABLERO HORIZONTAL ####
        if (longitud_x > 9 or longitud_y > 9):
            continue

        #### COMPRUEBA SI CHOCA ####
        fila_inicio = 0 if coord_fila - 1 < 0 else coord_fila-1
        columna_inicio = 0 if coord_col - 1 < 0 else coord_col-1

        fila_fin = 9 if longitud_y + 1 > 9 else longitud_y + 1
        columna_fin = 9 if longitud_x + 1 > 9 else longitud_x + 1

        choque = np.any(tablero[fila_inicio:fila_fin+1, columna_inicio:columna_fin+1] == 'B')

        if choque:  # choque == 1  (True)
            pass
        else:
            # Inserta el barco
            if hv == "h":
                tablero[coord_fila, coord_col:longitud_x] = 'B'
            elif hv== "v" :
                tablero[coord_fila:longitud_y, coord_col] = 'B'

            barcos += 1
    
    return(tablero)


########### CREAMOS TABLERO VACIO PARA JUGAR ###########
tablero_vacio=np.full((10,10), " ")

########### GENERAMOS LOS DOS TABLEROS CON LOS BARCOS ALEATORIOS ###########
tablero_barcos_j = crea_tablero()
tablero_adivinar = crea_tablero()  

print("\n\nVAMOS A HACER TRAMPAS... OS ENSEÑAMOS LAS POSICIONES DE LOS BARCOS QUE TENEMOS QUE HUNDIR :)\n\n")
print(tablero_adivinar)


###############################
########### A JUGAR ###########
###############################

print("\n¡Empieza la partida!\n")
print("Durante el juego tendrás que escribir las coordenadas a donde quieres disparar.")

while ("B" in tablero_adivinar) and ("B" in tablero_barcos_j):

    #### TURNO JUGADOR #### 

    print("¡¡DISPARAAA!!")
    disparo_fil = int(input("¿A qué fila quieres disparar? (introduce un número de 0 a 9)"))
    disparo_col = int(input("¿A qué columna quieres disparar? (introduce un número de 0 a 9)"))

    while (tablero_adivinar[disparo_fil, disparo_col] == "B") or (tablero_adivinar[disparo_fil, disparo_col] == "X"):
        
        if tablero_adivinar[disparo_fil, disparo_col] == "X":
            print("Aquí ya has disparado...")

        else:
            print("¡TOCADO!")
            tablero_adivinar[disparo_fil, disparo_col] = "X"
            tablero_vacio[disparo_fil, disparo_col] = "X"
            contador_de_b = 0  
            print("\n", tablero_vacio, "\n")
        
            # Comprobamos si hay más casillas de B al lado   
            checkeo_fil = disparo_fil - 1
            checkeo_col = disparo_col - 1

            for i in range(checkeo_fil, disparo_fil + 2):
                i = 0 if i < 0 else i
                i = 9 if i > 9 else i
                for j in range(checkeo_col, disparo_col + 2):
                    j = 0 if j < 0 else j
                    j = 9 if j > 9 else j
                    if tablero_adivinar[i, j] == "B":
                        contador_de_b += 1
        
            if contador_de_b >= 1:
                print("Aún no está hundido...")
                       
            else:
                print("¡¡¡Y HUNDIDO!!!")  
            
            
        
        disparo_fil = int(input("¿A qué fila quieres disparar?"))
        disparo_col = int(input("¿A qué columna quieres disparar?"))
        
        if tablero_vacio[disparo_fil,disparo_col] == "~":
            print("¡Aquí ya has disparado! Es agua.")
            continue
        
    if tablero_vacio[disparo_fil,disparo_col] == "~":
        print("¡Aquí ya has disparado! Es agua.")
        continue

    
    #### TURNO DE LA IA ####
   
    if tablero_adivinar[disparo_fil,disparo_col] != "B": 
        tablero_vacio[disparo_fil,disparo_col] = "~"
        print("¡Fallaste! Turno de la IA")
        print("\n", tablero_vacio, "\n")
        disparo_fil_ia = random.randint(0, 9)
        disparo_col_ia = random.randint(0, 9)

    while tablero_barcos_j[disparo_fil_ia, disparo_col_ia] == "B":
        print("La IA ha acertado")
        print("ESTE ES EL TABLERO QUE TIENE QUE ADIVINAR LA IA")
        tablero_barcos_j[disparo_fil_ia, disparo_col_ia] = "X"
        print("\n", tablero_barcos_j, "\n")
        # Repite el disparo
        disparo_fil_ia = random.randint(0, 9)
        disparo_col_ia = random.randint(0, 9)
    
    if tablero_barcos_j[disparo_fil_ia, disparo_col_ia] != "B":
        print("La IA ha fallado")
        print("ESTE ES EL TABLERO QUE TIENE QUE ADIVINAR LA IA")
        tablero_barcos_j[disparo_fil_ia, disparo_col_ia] = "~"
        print("\n", tablero_barcos_j, "\n")

        
### FINAL ###

if "B" not in tablero_adivinar:
    print("¡¡¡HAS GANADO!!!")

else:
    print("¡¡¡HA GANADO LA IA!!!")

print("Fin de la partida")