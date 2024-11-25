from juego.wordle import Wordle

def test_seleccionaJuego_1():
    Wordle.seleccionaJuego()

    assert Wordle.palabraJuego != "" and Wordle.palabraJuego in Wordle.palabras
    
