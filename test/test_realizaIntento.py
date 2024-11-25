from juego.wordle import Wordle

def test_realizaIntento_1():
    Wordle.palabraJuego = "ANGEL"
    
    intentoJugador = "AMARO"
    
    wordle = Wordle()

    wordle.realizaIntento(intentoJugador)

    assert Wordle.pistas[0][0] == "AMARO" and Wordle.pistas[0][1] == "A----" 

def test_realizaIntento_2():
    Wordle.palabraJuego = "ANGEL"
    
    intentoJugador = "ANARO"
    
    wordle = Wordle()

    wordle.realizaIntento(intentoJugador)

    assert Wordle.pistas[0][0] == "ANARO" and Wordle.pistas[0][1] == "AN---" 

def test_realizaIntento_3():
    Wordle.palabraJuego = "ANGEL"
    
    intentoJugador = "ANARE"
    
    wordle = Wordle()

    wordle.realizaIntento(intentoJugador)

    assert Wordle.pistas[0][0] == "ANARE" and Wordle.pistas[0][1] == "AN*-*" 

def test_realizaIntento_4():
    Wordle.palabraJuego = "ANGEL"
    
    intentoJugador = "ANGER"
    
    wordle = Wordle()

    wordle.realizaIntento(intentoJugador)

    assert Wordle.pistas[0][0] == "ANGER" and Wordle.pistas[0][1] == "ANGE-" 

def test_realizaIntento_5():
    Wordle.palabraJuego = "ANGEL"
    
    intentoJugador = "ANGEA"
    
    wordle = Wordle()

    wordle.realizaIntento(intentoJugador)

    assert Wordle.pistas[0][0] == "ANGEA" and Wordle.pistas[0][1] == "ANGE*" 