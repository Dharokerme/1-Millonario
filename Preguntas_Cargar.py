import Pregunta as pg

class Preguntas_Cargar(pg.Pregunta): # Se heredan los metodos de Pregunta
    def __init__(self,pregunta,resp_correcta,resp_incorrecta1,resp_incorrecta2,resp_incorrecta3): # Se cambia el init con el fin de cargarlos
        self.pregunta = pregunta
        self.resp_correcta = resp_correcta
        self.resp_incorrecta1 = resp_incorrecta1
        self.resp_incorrecta2 = resp_incorrecta2
        self.resp_incorrecta3 = resp_incorrecta3
    
