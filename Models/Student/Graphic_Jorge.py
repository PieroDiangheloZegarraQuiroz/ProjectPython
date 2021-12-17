import random
import time
import pygame
import sys

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QLabel, QDialog, QApplication
class Juego:



    # -------------------- Inicializador de la clase. Crea la cuadricula, las minas y los valores de cada cuadro -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def __init__(self, ancho, alto,counter):
        # juego1 = ejt.Juego1()
        self.counter=counter
        # print(counter,'Este es el counter del def')
        self.size = self.counter
        # self.size=juego1.counter()
        # self.size=self.counter
        # -------------------- Tamaño de cuadricula entre 4 y 20 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # self.size = int(input("Ingrese el tamaño de la cuadricula, debe ser mayor que 3 y menor que 21:"))

        # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        self.width = 400 // self.size  # Ancho de la cuadricula

        # ---------------------- Atributos propios de pygame ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.fuente = pygame.font.SysFont('newyorkitalicttf', self.width, True)  # Numeros
        self.temp = pygame.font.SysFont('newyorkitalicttf', 20, True)  # Tiempo
        self.msg = pygame.font.SysFont('newyorkitalicttf', 30, True)  # Mensaje de victoria y derrota
        self.p_ancho = ancho
        self.p_alto = alto
        self.ventana = pygame.display.set_mode((self.p_ancho, self.p_alto))  # Ventana y dimensiones
        pygame.display.set_caption("Buscaminas")
        self.centro = self.ventana.get_rect().center  # Centro de la ventana
        mina = pygame.image.load('../../Images/Others/Mina.png')
        self.mina = pygame.transform.scale(mina, (self.width, self.width))  # Imagen de la mina
        bandera = pygame.image.load('../../Images/Others/Bandera.png')
        self.bandera = pygame.transform.scale(bandera, (self.width, self.width))  # Imagen de la bandera
        pygame.mixer.init()
        pygame.mixer.music.load('../../Images/Others/Sounds/explosion.mp3')  # Sonido de la explosion
        pygame.mixer.music.set_volume(0.02)
        # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        # ------------------- Atributos propios del buscaminas -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.coord = {}  # Diccionario con coordenadas y color del cuadro
        self.cont_band = 0  # Contador de banderas bien colocadas
        self.banderas_restantes = 0  # Banderas que tiene el jugador
        self.banderas_max = 0  # Banderas maximas que puede tener el jugador
        self.estado = {}  # Diccionario con coordenadas y valores booleanos que indican la presencia de banderas
        self.est = True  # Indica con un booleano si se esta en juego o no
        self.cuadricula = []  # Lista de coordenadas del tablero
        self.HacerCuadricula()
        self.minas_d = {}  # Diccionario que indica si hay minas o no en una coorenada
        self.ColocarMinas()
        self.minasA_dt = {}  # Diccionario con el valor del nimero de minas aledañas a un cuadro
        self.ContarCuadros()

        # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # -------------------- Metodo que llena la cuadricula y el diccionario de coordenadas ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def HacerCuadricula(self):
        x = self.centro[0] - (self.size * (self.width + 5) / 2)  # Obitiene la coordenada x para iniciar la cuadricula
        y = self.centro[1] - (self.size * (self.width + 5) / 2)  # Obtiene la coordenada y para iniciar la cuadricula
        for i in range(self.size):
            for j in range(self.size):
                self.coord[(x, y)] = self.coord.get((x, y),
                                                    (192, 192, 192))  # Crea los cuadros con  su respectivo color
                self.estado[(x, y)] = False  # Inicializa los cuadros sin banderas
                self.cuadricula.append((x, y))

                x += self.width + 5
            x -= (self.width + 5) * self.size
            y += self.width + 5

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # --------------------- Metodo que imprime el mapa en pantalla ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def MostrarCuadricula(self):
        for i in self.cuadricula:
            color = self.coord.get(i)
            x = i[0]
            y = i[1]
            pygame.draw.polygon(self.ventana, (224, 224, 224),
                                [(x + self.width, y), (x + self.width + 2.5, y - 2.5), (x - 2.5, y - 2.5),
                                 (x - 2.5, y + self.width + 2.5), (x, y + self.width),
                                 (x, y)])  # Borde superior e izquierdo de cada cuadro
            pygame.draw.polygon(self.ventana, (96, 96, 96), [(x, y + self.width), (x - 2.5, y + self.width + 2.5),
                                                             (x + self.width + 2.5, y + self.width + 2.5),
                                                             (x + self.width + 2.5, y - 2.5), (x + self.width, y), (
                                                             x + self.width,
                                                             y + self.width)])  # Borde inferior y derecho de cada cuadro
            pygame.draw.rect(self.ventana, (color), (x, y, self.width, self.width))  # Cuadros

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # ---------------------- Metodo que asigna minas a una parte de las coordenadas de la cuadricula -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def ColocarMinas(self):
        self.minas_d = {}  # Vacia el diccionario para reasignar en la primera jugada
        self.banderas_restantes = 0  # Reinicia el numero de banderas restantes
        self.banderas_max = 0  # Reinicia el numero de banderas maximas
        for i in self.cuadricula:
            self.minas_d[i] = self.minas_d.get(i, False)  # False indica que no hay mina
        rng = random.Random()
        while self.banderas_restantes < len(self.minas_d) // 5:
            M = rng.randrange(0, len(self.cuadricula))
            if self.minas_d.get(self.cuadricula[M]) == False:
                self.minas_d[self.cuadricula[M]] = True  # True indica que hay una mina en la posicion M
                self.banderas_restantes += 1  # Cada que asigna una mina aumenta en 1 el numero de banderas restantes
                self.banderas_max += 1  # Cada que asigna una mina aumenta en 1 el numero de banderas maximas

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # ----------------------- Metodo que mezcla las minas para que el jugador no pierda en el primer turno -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def safe(self, pos):
        for i in self.coord:
            if pos[0] >= i[0] and pos[0] <= i[0] + self.width and pos[1] >= i[1] and pos[1] <= i[
                1] + self.width:  # Revisa si la posicion en la que se dio click es un cuadro de la cuadricula o no
                while self.minasA_dt[
                    i] != 0:  # Vuelve a asignar las minas y a contar los cuadros hasta que el cuadro en que se presiono no tenga minas alrededor
                    self.ColocarMinas()
                    self.ContarCuadros()


                return 1  # Retorna 1 si se presiono en un cuadro
        return 0  # Retorna 0 si no se presiono un cuadro


    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # ----------------------- Metodo que cuenta las minas que estan alrededor de algun cuadro ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def ContarCuadros(self):
        self.minasA_dt = {}  # Reinicia el diccionario para reasignar en la primera jugada
        counter = 0  # Contador que avanza por la cuadricula
        for i in self.minas_d:
            minasC = 0  # Contador de minas aledañas
            y = self.cuadricula[counter]  # Posicion que se esta evaluando actualmente
            if self.minas_d[i] == True:
                self.minasA_dt[i] = True  # Usa la misma convencion de minas_d para indicar si hay minas
            # ----------------------- Si el cuadro evaluado no tiene mina revisa alrededor desde la derecha en sentido antihorario -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            else:
                if (y[0] + self.width + 5, y[1]) in self.minas_d:
                    if self.minas_d[(y[0] + self.width + 5, y[1])] == True:
                        minasC += 1
                if (y[0] + self.width + 5, y[1] + self.width + 5) in self.minas_d:
                    if self.minas_d[(y[0] + self.width + 5, y[1] + self.width + 5)] == True:
                        minasC += 1
                if (y[0], y[1] + self.width + 5) in self.minas_d:
                    if self.minas_d[(y[0], y[1] + self.width + 5)] == True:
                        minasC += 1
                if (y[0] - self.width - 5, y[1] + self.width + 5) in self.minas_d:
                    if self.minas_d[(y[0] - self.width - 5, y[1] + self.width + 5)] == True:
                        minasC += 1
                if (y[0] - self.width - 5, y[1]) in self.minas_d:
                    if self.minas_d[(y[0] - self.width - 5, y[1])] == True:
                        minasC += 1
                if (y[0] - self.width - 5, y[1] - self.width - 5) in self.minas_d:
                    if self.minas_d[(y[0] - self.width - 5, y[1] - self.width - 5)] == True:
                        minasC += 1
                if (y[0], y[1] - self.width - 5) in self.minas_d:
                    if self.minas_d[(y[0], y[1] - self.width - 5)] == True:
                        minasC += 1
                if (y[0] + self.width + 5, y[1] - self.width - 5) in self.minas_d:
                    if self.minas_d[(y[0] + self.width + 5, y[1] - self.width - 5)] == True:
                        minasC += 1
                self.minasA_dt[i] = self.minasA_dt.get(i, minasC)
            # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            counter += 1  # Avanza al siguiente cuadro



    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # ----------------------- Metodo que destapa una casilla del mapa ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def uncover(self, i):
        val = self.minasA_dt.get(i)  # Obtiene el numero del cuadro
        pos = [i[0] + (self.width // 5), i[1]]  # Obtine ela posicion para colocar el numero
        self.coord[i] = (96, 96, 96)  # Cambia el color de fondo del cuadro que se descubre
        self.MostrarCuadricula()  # Actualiza la cuadricula para que cambie el fondo
        # ---------------------- Evalua los numeros de los cuadros, les asigna distintos colores y los imprime en pantalla ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        if str(val) == "1":  # Se debe convertir el 1 a str o si no va a contar el True de las minas como 1
            val = self.fuente.render(str(val), 1, (0, 128, 255))
            self.ventana.blit(val, pos)
        if val == 2:
            val = self.fuente.render(str(val), 1, (0, 204, 0))
            self.ventana.blit(val, pos)
        if val == 3:
            val = self.fuente.render(str(val), 1, (255, 0, 0))
            self.ventana.blit(val, pos)
        if val == 4:
            val = self.fuente.render(str(val), 1, (0, 0, 204))
            self.ventana.blit(val, pos)
        if val == 5:
            val = self.fuente.render(str(val), 1, (102, 51, 0))
            self.ventana.blit(val, pos)
        if val == 6:
            val = self.fuente.render(str(val), 1, (0, 255, 255))
            self.ventana.blit(val, pos)
        if val == 7:
            val = self.fuente.render(str(val), 1, (51, 0, 0))
            self.ventana.blit(val, pos)
        if val == 8:
            val = self.fuente.render(str(val), 1, (64, 64, 64))
            self.ventana.blit(val, pos)
        if val == 9:
            val = self.fuente.render(str(val), 1, (0, 0, 0))
            self.ventana.blit(val, pos)
            # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        if i in self.cuadricula:
            self.cuadricula.remove(
                i)  # Finalmente elimina los cuadros destapados de la cuadricula debido a que ya no se usaran

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # ------------------------- Metodo que coloca o quita banderas en el mapa ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def PonerOQuitarBandera(self, pos):
        for i in self.coord:
            if pos[0] >= i[0] and pos[0] <= i[0] + self.width and pos[1] >= i[1] and pos[1] <= i[1] + self.width:
                pos = [i[0], i[1]]  # Obtiene la posicion sobre la que se pondra la bandera
                # ----------------------------- Si el cuadro no tiene bandera ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                if self.estado[i] == False:
                    if self.banderas_restantes != 0:  # No hace nada si no quedan banderas
                        if i in self.cuadricula:  # Si no se ha descubierto el cuadro se ejecuta
                            self.cuadricula.remove(
                                i)  # Elimina la posicion de la cuadricula para que no se pueda destapar
                            self.ventana.blit(self.bandera, pos)  # Muestra la bandera
                            self.banderas_restantes -= 1  # Resta 1 a las banderas del usuario
                            self.estado[i] = True  # Actualiza el estado a tener una bandera
                        if self.minasA_dt[i] == True:
                            self.cont_band += 1  # Si habia una mina en el lugar le suma 1 al contador final
                        break
                # ----------------------------- Si el cuadro tiene bandera ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                else:
                    self.cuadricula.append(i)  # Vuelve a incluir el cuadro en la lista de cuadricula
                    self.banderas_restantes += 1  # Le suma 1 a las banderas restantes
                    self.estado[i] = False  # Actualiza el estado a no tener bandera
                    if str(self.minasA_dt[
                               i]) == "True":  # Compara con el valor de la mina, se debe convertir a str para que no cuente los 1 como true
                        self.cont_band -= 1
                    break
                # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # ------------------------- Metodo que lleva a cabo la accion principal ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def ejecucion(self, pos):
        for i in self.coord:
            if pos[0] >= i[0] and pos[0] <= i[0] + self.width and pos[1] >= i[1] and pos[1] <= i[1] + self.width:
                if self.estado[i] != True:  # Solo abre si en el cuadro no hay bandera
                    if self.minas_d[i] == True:  # Si se oprimio una mina
                        pos = [i[0], i[1]]  # Obtiene la posicion para poner la mina
                        self.ventana.blit(self.mina, pos)  # Pone la mina en laventana
                        pygame.mixer.music.play()
                        self.est = False  # Hace que el juego se deje de ejecutar
                    else:
                        self.uncover(i)  # Destapa el cuadro
                        if self.minasA_dt[i] == 0:  # Si no hay minas aledañas
                            self.minasA_dt[i] = "0"  # Convierte el 0 a str para que no lo vuelva a leer como 0

                            # --------------------------------- Revisa los valores alrededor en el mismo orden que la funcion contar cuadros, los destapa y revisa su valor para expandir como el buscaminas clasico -----------------------------------------------------------------------------------------------
                            if (i[0] + self.width + 5, i[1]) in self.minasA_dt:
                                a = self.minasA_dt[(i[0] + self.width + 5, i[1])]
                                self.uncover((i[0] + self.width + 5, i[1]))
                                if a == 0:
                                    self.ejecucion((i[0] + self.width + 5, i[
                                        1]))  # Si el valor de la casilla es 0 repite la ejecucion con esa casilla
                            if (i[0] + self.width + 5, i[1] + self.width + 5) in self.minas_d:
                                a = self.minasA_dt[(i[0] + self.width + 5, i[1] + self.width + 5)]
                                self.uncover((i[0] + self.width + 5, i[1] + self.width + 5))
                                if a == 0:
                                    self.ejecucion((i[0] + self.width + 5, i[
                                        1] + self.width + 5))  # Si el valor de la casilla es 0 repite la ejecucion con esa casilla
                            if (i[0], i[1] + self.width + 5) in self.minasA_dt:
                                a = self.minasA_dt[(i[0], i[1] + self.width + 5)]
                                self.uncover((i[0], i[1] + self.width + 5))
                                if a == 0:
                                    self.ejecucion((i[0], i[
                                        1] + self.width + 5))  # Si el valor de la casilla es 0 repite la ejecucion con esa casilla
                            if (i[0] - self.width - 5, i[1] + self.width + 5) in self.minas_d:
                                a = self.minasA_dt[(i[0] - self.width - 5, i[1] + self.width + 5)]
                                self.uncover((i[0] - self.width - 5, i[1] + self.width + 5))
                                if a == 0:
                                    self.ejecucion((i[0] - self.width - 5, i[
                                        1] + self.width + 5))  # Si el valor de la casilla es 0 repite la ejecucion con esa casilla
                            if (i[0] - self.width - 5, i[1]) in self.minasA_dt:
                                a = self.minasA_dt[(i[0] - self.width - 5, i[1])]
                                self.uncover((i[0] - self.width - 5, i[1]))
                                if a == 0:
                                    self.ejecucion((i[0] - self.width - 5, i[
                                        1]))  # Si el valor de la casilla es 0 repite la ejecucion con esa casilla
                            if (i[0] - self.width - 5, i[1] - self.width - 5) in self.minas_d:
                                a = self.minasA_dt[(i[0] - self.width - 5, i[1] - self.width - 5)]
                                self.uncover((i[0] - self.width - 5, i[1] - self.width - 5))
                                if a == 0:
                                    self.ejecucion((i[0] - self.width - 5, i[
                                        1] - self.width - 5))  # Si el valor de la casilla es 0 repite la ejecucion con esa casilla
                            if (i[0], i[1] - self.width - 5) in self.minasA_dt:
                                a = self.minasA_dt[(i[0], i[1] - self.width - 5)]
                                self.uncover((i[0], i[1] - self.width - 5))
                                if a == 0:
                                    self.ejecucion((i[0], i[
                                        1] - self.width - 5))  # Si el valor de la casilla es 0 repite la ejecucion con esa casilla
                            if (i[0] + self.width + 5, i[1] - self.width - 5) in self.minas_d:
                                a = self.minasA_dt[(i[0] + self.width + 5, i[1] - self.width - 5)]
                                self.uncover((i[0] + self.width + 5, i[1] - self.width - 5))
                                if a == 0:
                                    self.ejecucion((i[0] + self.width + 5, i[
                                        1] - self.width - 5))  # Si el valor de la casilla es 0 repite la ejecucion con esa casilla
                    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                break

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # ---------------------- Metodo que muestra el tiempo que lleva el usuario ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def ImpTiempo(self, t1):

        pos = (self.centro[0] - 200,
               self.centro[1] + (self.width + 5) * (self.size / 2) + 15)  # Posicion del tiempo: Abajo en el centro
        self.t2 = time.perf_counter()
        self.t = str(int(self.t2 - t1))
        self.t = self.temp.render("Tiempo : {0} sec".format(self.t), 1, (255, 255, 0))
        self.a = (int(self.t2 - t1))
        pygame.draw.rect(self.ventana, (0, 0, 0),
                         (pos[0], pos[1], 200, self.width))  # Dibuja un fondo negro para que no se sobreponga
        self.ventana.blit(self.t, (pos))  # Dibuja el mensaje


    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # ---------------------- Metodo que muestra la solucion si el jugador pierde -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def MostrarRespuesta(self):
        for i in self.minas_d:
            if self.minas_d[i] == True and self.estado[
                i] == False:  # Dibuja una mina si el cuadro tiene y si no hay bandera en el lugar
                pos = [i[0], i[1]]
                self.ventana.blit(self.mina, pos)
            if self.estado[i] == True and self.minas_d[i] == False:
                pygame.draw.line(self.ventana, (0, 0, 0), (i[0], i[1]), (i[0] + self.width, i[1] + self.width),
                                 (5))  # Dibuja una x sobre una bandera mal puesta
                pygame.draw.line(self.ventana, (0, 0, 0), (i[0] + self.width, i[1]), (i[0], i[1] + self.width), (5))

class graf(QDialog):
    def __init__(self):
        super(graf, self).__init__()
        self.resize(600, 600)
        self.setWindowTitle("Resultado probabilistico")
        self.setStyleSheet("background: white")

        self.label = QLabel('Resultado probabilístico', self)
        self.label.setFont(QFont("Comic Sans MS", 14))
        self.label.move(180, 0)
        self.label1 = QLabel('<b>Espacio muestral:</b> S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ,15 ,16}', self)
        self.label1.setFont(QFont("Comic Sans MS", 10))
        self.label1.move(30, 30)

        self.label3 = QLabel('<b>Formula:</b>', self)

        self.label3.setFont(QFont("Comic Sans MS", 10))
        self.label3.move(30, 110)

        self.label66 = QLabel('<b>Solución:</b>', self)

        self.label66.setFont(QFont("Comic Sans MS", 10))
        self.label66.move(280, 110)

        self.label35 = QLabel(f'<b>Evento (A1): ¿Cual es la probabilidad de que un cuadro sea una mina en el nivel 5?</b>', self)

        self.label35.setFont(QFont("Comic Sans MS", 10))
        self.label35.move(30, 60)

        self.label4 = QLabel('Nºcasos favorables A1', self)
        self.label4.setFont(QFont("Comic Sans MS", 8, QFont.Bold))
        self.label4.move(100, 130)

        self.label5 = QLabel('Nºtotal casos posibles', self)
        self.label5.setFont(QFont("Comic Sans MS", 8, QFont.Bold))
        self.label5.move(100, 170)

        self.label14 = QLabel('1', self)
        self.label14.setFont(QFont("Comic Sans MS", 10, QFont.Bold))
        self.label14.move(410, 135)

        self.label15 = QLabel('25', self)
        self.label15.setFont(QFont("Comic Sans MS", 10, QFont.Bold))
        self.label15.move(410, 170)

        self.label7 = QLabel('•A1:', self)
        self.label7.setFont(QFont("Comic Sans MS", 10, QFont.Bold))
        self.label7.move(1, 150)

        self.label6 = QLabel('•Interpretación: el resultado de la operación es 0.04, por tanto si lo multiplicamos por el  ', self)
        self.label6.setFont(QFont("Comic Sans MS", 10, QFont.Bold))
        self.label6.move(1, 210)

        self.label1313 = QLabel(
            '100% obtenemos el valor de 4%, que representa la probabilidad de ', self)
        self.label1313.setFont(QFont("Comic Sans MS", 10, QFont.Bold))
        self.label1313.move(110, 230)

        self.label99 = QLabel(
            'que al destapar un cuadro sea una mina.', self)
        self.label99.setFont(QFont("Comic Sans MS", 10, QFont.Bold))
        self.label99.move(110, 250)
#-----------------------------------------------------------------------------------------
        user_png = r"../../Images/Others/Formula2.png"
        try:
            with open(user_png):
                imageLogin = QLabel(self)
                pixmap = QPixmap(user_png)
                imageLogin.setPixmap(pixmap)
                imageLogin.move(35, 150)
                imageLogin.resize(600, 20)
        except FileNotFoundError:
            print("A1Izquierda")
# -----------------------------------------------------------------------------------------
        user_png1 = r"../../Images/Others/Formula1.png"
        try:
            with open(user_png1):
                imageLogin1 = QLabel(self)
                pixmap = QPixmap(user_png1)
                imageLogin1.setPixmap(pixmap)
                imageLogin1.move(280, 150)
                imageLogin1.resize(500, 20)
        except FileNotFoundError:
            print("A1 derecha")
#------------------------------------------------------------------------------------------------------
        self.label5 = QLabel('Representación gráfica:', self)
        self.label5.setFont(QFont("Comic Sans MS", 10, QFont.Bold))
        self.label5.move(1, 285)
        chart = Canvas(self)
        chart.move(100, 315)
        chart.resize(380, 280)

        self.labelresult1 = QLabel('0.04', self)
        self.labelresult1.setFont(QFont("Comic Sans MS", 12, QFont.Bold))
        self.labelresult1.move(500, 150)


class Canvas(FigureCanvas):
    def __init__(self, parent):
        self.fig, self.ax = plt.subplots(figsize=(5, 4), dpi=80)
        super(Canvas, self).__init__(self.fig)
        self.setParent(parent)

        x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
        y = np.array([1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 10, 1 / 10])
        self.ax.plot(x, y)
        plt.xlabel("Resultados")
        plt.ylabel("Probabilidades")
        plt.bar(x, y, color="blue", align="center")
        plt.xlabel("Resultados")
        plt.ylabel("Probabilidades")
        self.ax.grid()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = graf()
    window.show()
    sys.exit(app.exec_())

# -------------------------------------------------------------------------------------------------------------------------------