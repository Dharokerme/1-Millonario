class Jugador:
    score = 0  # Se crea una clase con el fin de que cada jugador sea un objeto
    def __init__(self):
        self.nombre = input('Jugador, escriba su nombre:') 

    def imprimir_score(self):
        print('El nombre del jugador es:',self.nombre)
        print('Empieza el juego con un score de',self.score)

