from juego.wordle import Wordle

def test_acertado_Winner():
    Wordle.seleccionaJuego()
    
    wordle = Wordle()

    palabraJugador = Wordle.palabraJuego

    assert wordle.acertado(palabraJugador) == True

def test_acertado_Loser():
    Wordle.seleccionaJuego()

    wordle = Wordle()
    
    palabraJugador = "AMARU"

    assert wordle.acertado(palabraJugador) == False
    