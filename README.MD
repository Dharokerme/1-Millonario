El archivo Millonario.py es el archivo principal el cual corre el juego, el proyecto se trata del juego "Quien quiere ser millonario"
Se utilizo el paradigma de programacion POO para resolver una parte del proyecto y programacion estructurada para el resto
Los requisitos necesarios para el correcto funcionamiento del codigo es que todos los archivos esten en la misma carpeta de ejecucion, son:

-Millonario.py
-Pregunta.py
-Preguntas_Cargar.py
-Jugador.py
-Categoria1.txt
-Categoria2.txt
-Categoria3.txt
-Categoria4.txt
-Categoria5.txt
-Score.txt

Los archivos Pregunta.py, Preguntas_Cargar.py, Jugador.py pertenecen a las clases utilizadas por Millonario.py
Los archivos Categoria1.txt, Categoria2.txt, Categoria3.txt, Categoria4.txt, Categoria5.txt y Score.txt contiene la informacion utilizada para la persistencia de datos, ahi se almacenan las preguntas segun su categoria y el historial de jugadores y su respectivos scores.

Se utilizo la version de Python 3.10.0 que se encuentra en https://www.python.org/downloads/ y Visual Studio Code https://code.visualstudio.com/download.

BUGS a veces no funcionada la escritura de los datos pero esto era debido a la mala configuracion del Visual Studio Code:
    -> Ir a configuracion de Visual Studio Code ( Archivo -> Preferencias ->Configuracion -> Extensiones de Usuario -> Python -> Execute In File Dir  -> Activar.

