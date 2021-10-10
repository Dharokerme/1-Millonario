import random    # Importo Random para generar numeros o elecciones aleatorias
import Jugador as jg # Importo la clase Jugador como jg
import Pregunta as pg # Importo la clase Pregunta como pg
import Preguntas_Cargar as pc # Importo la Clase Preguntas Cargar ( heredada de pg )

jugador = jg.Jugador()  # Se crea el nombre del jugador al instanciar el objeto

centinela = None  # Variable para inicializar el menu

Categoria_1 = []
Categoria_2 = []
Categoria_3 = []
Categoria_4 = []
Categoria_5 = []  # Listas vacias donde contendran las preguntas del juego donde categoria 1 es facil y 5 dificil

#------------- Cargando las preguntas en sus respectivas categorias ------------------

datos = open('Categoria1.txt','r',encoding='utf-8')  # Crea una variable donde se carga el archivo Categoria 1
archivo = datos.readlines()  # archivo se vuelve un archivo tipo lista conteniendo cada linea de dato como un array
datos.close() # Cierra el archivo.

another = []  # Se crea una lista vacia para cagar las preguntas que ya estan en los archivos categorias
for i in archivo:
    preguntashhhh = i.split("_")    # Se separan por medio de un "_" para despues crear los objetos preguntas con cada valor
    another.append(preguntashhhh)   # Se agrega cada valor a another para un posterior tratamiento
    for i in another:
        Nueva_pregunta = pc.Preguntas_Cargar(i[0],i[1],i[2],i[3],i[4])  # Se instancia el objeto pregunta cargar
        Categoria_1.append(Nueva_pregunta)  # Agrego a la categoria el objeto pregunta instanceado.

datos = open('Categoria2.txt','r',encoding='utf-8')  # Se repite el proceso para cargar las preguntas de categoria 1.
archivo = datos.readlines()
datos.close()

another = []
for i in archivo:
    preguntashhhh = i.split("_")
    another.append(preguntashhhh)
    for i in another:
        Nueva_pregunta = pc.Preguntas_Cargar(i[0],i[1],i[2],i[3],i[4])
        Categoria_2.append(Nueva_pregunta)

datos = open('Categoria3.txt','r',encoding='utf-8')# Se repite el proceso para cargar las preguntas de categoria 1.
archivo = datos.readlines()
datos.close()

another = []
for i in archivo:
    preguntashhhh = i.split("_")
    another.append(preguntashhhh)
    for i in another:
        Nueva_pregunta = pc.Preguntas_Cargar(i[0],i[1],i[2],i[3],i[4])
        Categoria_3.append(Nueva_pregunta)

datos = open('Categoria4.txt','r',encoding='utf-8')# Se repite el proceso para cargar las preguntas de categoria 1.
archivo = datos.readlines()
datos.close()

another = []
for i in archivo:
    preguntashhhh = i.split("_")
    another.append(preguntashhhh)
    for i in another:
        Nueva_pregunta = pc.Preguntas_Cargar(i[0],i[1],i[2],i[3],i[4])
        Categoria_4.append(Nueva_pregunta)


datos = open('Categoria5.txt','r',encoding='utf-8')# Se repite el proceso para cargar las preguntas de categoria 1.
archivo = datos.readlines()
datos.close()

another = []
for i in archivo:
    preguntashhhh = i.split("_")
    another.append(preguntashhhh)
    for i in another:
        Nueva_pregunta = pc.Preguntas_Cargar(i[0],i[1],i[2],i[3],i[4])
        Categoria_5.append(Nueva_pregunta)


# Se inicializa el menu del juego
while centinela != 5:
    print('- MENU QUIEN QUIERE SER MILLONARIO -')
    print('-------------Hola',jugador.nombre,'---------')
    print('- 1) -------- Jugar ------------')
    print('- 2) ------ Crear pregunta------- ')
    print('- 3) -- Historico de Jugadores --')
    print('- 4) ---------- Salir ---------  ')

    centinela = int(input('Ingrese una opcion:'))
    if centinela ==1:   #-------------------- Jugar ----------------------------
        seleccion = random.choice(Categoria_1)   # Selecciona una pregunta al azar
        print(seleccion) # Imprime su contenido
        respuestacorrecta= int(input('Escoge una opcion:')) # Valor para comparar con la respuesta correcta.
        print('Acumulado:',jugador.score)
        retirarse = int(input('Te deseas retirar? (Te llevaras el acumulado)\n 1)Si\n 2)No\n')) # Se le da la opcion de abandonar el juego con el acumulado
        if retirarse == 1:
            print('Felicidades',jugador.nombre,'Tu score fue:',jugador.score) # Se guarda en el archivo score los datos del jugador y el score obtenido hasta el momento
            datos = open('Score.txt','a',encoding='utf-8')
            puntuacion_final = 'Jugador:'+str(jugador.nombre)+'-Score:'+str(jugador.score)+'\n'
            datos.write(puntuacion_final)
            datos.close()
            break
        else:
            respuesta = seleccion.escoger() # Se utiliza el metodo de la clase preguntas.escoger()
            if respuesta == respuestacorrecta: # Si la respuesta es correcta se cambia el valor del atributo del objeto jugador.
                print('Es...CORRECTO! Ahora tienes 1000 puntos')
                jugador.score = 1000
                print('Bienvenido a la siguiente ronda 2:') # Continua el juego de igual manera que en el anterior con unos if anidados.
                seleccion = random.choice(Categoria_2)
                print(seleccion)
                respuestacorrecta= int(input('Escoge una opcion:'))
                print('Acumulado:',jugador.score)
                retirarse = int(input('Te deseas retirar? (Te llevaras el acumulado)\n 1)Si\n 2)No\n'))
                if retirarse == 1:
                    print('Felicidades',jugador.nombre,'Tu score fue:',jugador.score)
                    datos = open('Score.txt','a',encoding='utf-8')
                    puntuacion_final = 'Jugador:'+str(jugador.nombre)+'-Score:'+str(jugador.score)+'\n'
                    datos.write(puntuacion_final)
                    datos.close()
                    break
                else:
                    respuesta = seleccion.escoger()
                    if respuesta == respuestacorrecta:
                        print('Es...CORRECTO! Ahora tienes 3000 puntos')
                        jugador.score = 3000
                        print('Bienvenido a la siguiente ronda 4:')
                        seleccion = random.choice(Categoria_3)
                        print(seleccion)
                        respuestacorrecta= int(input('Escoge una opcion:'))
                        print('Acumulado:',jugador.score)
                        retirarse = int(input('Te deseas retirar? (Te llevaras el acumulado)\n 1)Si\n 2)No\n'))
                        if retirarse == 1:
                            print('Felicidades',jugador.nombre,'Tu score fue:',jugador.score)
                            datos = open('Score.txt','a',encoding='utf-8')
                            puntuacion_final = 'Jugador:'+str(jugador.nombre)+'-Score:'+str(jugador.score)+'\n'
                            datos.write(puntuacion_final)
                            datos.close()
                            break
                        else:
                            respuesta = seleccion.escoger()
                            if respuesta == respuestacorrecta:
                                print('Es...CORRECTO! Ahora tienes 8000 puntos')
                                jugador.score = 8000
                                print('Bienvenido a la siguiente ronda 4:')
                                seleccion = random.choice(Categoria_4)
                                print(seleccion)
                                respuestacorrecta= int(input('Escoge una opcion:'))
                                print('Acumulado:',jugador.score)
                                retirarse = int(input('Te deseas retirar? (Te llevaras el acumulado)\n 1)Si\n 2)No\n'))
                                if retirarse == 1:
                                    print('Felicidades',jugador.nombre,'Tu score fue:',jugador.score)
                                    datos = open('Score.txt','a',encoding='utf-8')
                                    puntuacion_final = 'Jugador:'+str(jugador.nombre)+'-Score:'+str(jugador.score)+'\n'
                                    datos.write(puntuacion_final)
                                    datos.close()
                                    break
                                else:
                                    respuesta = seleccion.escoger()
                                    if respuesta == respuestacorrecta:
                                        print('Es...CORRECTO! Ahora tienes 20000 puntos')
                                        jugador.score = 20000
                                        print('Bienvenido a la siguiente ronda 5:')
                                        seleccion = random.choice(Categoria_5)
                                        print(seleccion)
                                        respuestacorrecta= int(input('Escoge una opcion:'))
                                        print('Acumulado:',jugador.score)
                                        retirarse = int(input('Te deseas retirar? (Te llevaras el acumulado)\n 1)Si\n 2)No\n'))
                                        if retirarse == 1:
                                            print('Felicidades',jugador.nombre,'Tu score fue:',jugador.score)
                                            datos = open('Score.txt','a',encoding='utf-8')
                                            puntuacion_final = 'Jugador:'+str(jugador.nombre)+'-Score:'+str(jugador.score)+'\n'
                                            datos.write(puntuacion_final)
                                            datos.close()
                                            break
                                        else:
                                            respuesta = seleccion.escoger()
                                            if respuesta == respuestacorrecta:
                                                print('Es...CORRECTO! GANASTE EL JUEGO 100000 PUNTOS!') # Termina el juego y se le asocia la mayor puntuacion
                                                jugador.score = 100000
                                                datos = open('Score.txt','a',encoding='utf-8')
                                                puntuacion_final = 'Jugador:'+str(jugador.nombre)+'-Score:'+str(jugador.score)+'\n'
                                                datos.write(puntuacion_final)
                                                datos.close()
                                                print('Gracias por jugar.')
                
            else:
                print('Gracias por participar',jugador.nombre,'Te llevas: 0 puntos')
                break

    elif centinela == 2:   #------ Crea la pregunta y la almacena ---------------

        pregunta = pg.Pregunta()  #Se instancia la pregunta a manera de pedirla al usuario
        categoria_pregunta  = pregunta.mostrar_categoria() # Se utiliza el metodo mostrar categoria del objeto pregunta
        informacion_pregunta = str(pregunta.guardar())
        if categoria_pregunta == 1: # Si la categoria de la pregunta es 1 se agrega el objeto a Categoria1.txt
            Categoria_1.append(pregunta)
            archivo = open('Categoria1.txt','a')
            archivo.write(informacion_pregunta)
            archivo.close

        elif pregunta.mostrar_categoria() == 2: # Si la categoria es distinta se le asocia a la respectiva categoria.
            Categoria_2.append(pregunta)
            archivo = open('Categoria2.txt','a')
            archivo.write(informacion_pregunta)
            archivo.close

        elif pregunta.mostrar_categoria() == 3:
            Categoria_3.append(pregunta)
            archivo = open('Categoria3.txt','a')
            archivo.write(informacion_pregunta)
            archivo.close

        elif pregunta.mostrar_categoria() == 4:
            Categoria_4.append(pregunta)
            archivo = open('Categoria4.txt','a')
            archivo.write(informacion_pregunta)
            archivo.close

        elif pregunta.mostrar_categoria() == 5:
            Categoria_5.append(pregunta)
            archivo = open('Categoria5.txt','a')
            archivo.write(informacion_pregunta)
            archivo.close
    elif centinela == 3:  # ------------ Listado de Scores ----------------------
        print('----------- Historial de Partidas ------------')
        datos = open('Score.txt','r',encoding='utf-8')
        puntuaciones = datos.read()    # Se leen los datos que se guardan en el archivo score.txt y se imprime en pantalla
        datos.close()

        print(puntuaciones)

    elif centinela == 4:  # ------------ Salir del juego ------------------------
        print('Gracias por jugar') # Sale del Ciclo y del Juego
        break


