import random

class Pregunta(): # Se instancian los metodos y atributos necesarios para el correcto funcionamiento
    lista = []

    def __init__(self):

        self.categoria = int(input('Ingresa la categoria:'))
        self.pregunta = input('Ingresa la pregunta:')
        self.resp_correcta = input('Ingresa la respuesta correcta:')
        self.resp_incorrecta1 = input('Ingresa la respuesta incorrecta:')
        self.resp_incorrecta2 = input('Ingresa la respuesta incorrecta:')
        self.resp_incorrecta3 = input('Ingresa la respuesta incorrecta:')

    def __str__(self) -> str:
        self.lista = [self.resp_correcta,self.resp_incorrecta1,self.resp_incorrecta2,self.resp_incorrecta3]
        random.shuffle(self.lista)
        return self.pregunta +'\n 1)'+ str(self.lista[0]) + '\n 2)'+ str(self.lista[1]) +'\n 3)'+ str(self.lista[2]) +'\n 4)'+ str(self.lista[3])
    
    def escoger(self):
        opcion = int(input('Ultima palabra?(Vuelve a escoger la opcion de las 4 posibles):'))

        for i in range(0,4):
            variable = self.resp_correcta
            if variable == self.lista[i]:
                variable2 = i+1
                
        if opcion == variable2:
            print('Correcto')
        else:
            print('No es correcto')
        return variable2

    def mostrar_categoria(self):
        return self.categoria

    def guardar(self) -> str:
        return self.pregunta + "_" + self.resp_correcta+"_" + self.resp_incorrecta1 + "_" + self.resp_incorrecta2 + "_"+self.resp_incorrecta3+"_"+str(self.categoria)+"\n"
