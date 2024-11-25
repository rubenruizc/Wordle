from random import *

class Wordle:

    #Array que almacena todas las palabras con la que podemos jugar
    palabras = ["ANGEL","JAMON","LENTO","VERDE","PLAYA","HIELO","FUEGO","MANGO","BANCO","SALTO"]

    #Almacena la palabra con la que se va a jugar
    palabraJuego = ""

    #Array que almacena los distintos intentos realizados
    pistas = [["-----"] * 2] * 6

    #Almacena el número de intento que llevamos
    numIntento = 0

    #MÉTODOS
    def seleccionaJuego():
        index = randint(0,9)
        Wordle.palabraJuego = Wordle.palabras [index]
        


    def realizaIntento(self,intentoJugador):
        
        arrayIntentoJugador = list(intentoJugador)
        arrayPalabraJuego = list(Wordle.palabraJuego)
        letrasPista = ""

        for i in range(len(arrayIntentoJugador)):
            if arrayIntentoJugador[i] in arrayPalabraJuego:
                if(arrayIntentoJugador[i] == arrayPalabraJuego[i]):
                    letrasPista += arrayPalabraJuego[i]
                else:
                    letrasPista+= "*"
            else:
                letrasPista += "-"

        
        
        Wordle.pistas[Wordle.numIntento][0] = intentoJugador
        Wordle.pistas[Wordle.numIntento][1] = letrasPista

        Wordle.numIntento += 1
    
        

    def acertado(self,intentoJugador):
        acertado = False

        if(intentoJugador == Wordle.palabraJuego):
            acertado = True

        return acertado

    
