import pygame
import time
import Models.Student.Graphic_Jorge as Df
from pygame.locals import *
import subprocess
import sys

# ----------------------------- Bloque de ejecucion -------------------------------------------------------------------------------------------------------------------------------------------------------
pygame.init()

screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)

pygame.display.set_caption('Button Demo')

font = pygame.font.SysFont('Constantia', 30)

# define colours
bg = (0, 0, 0)
red = ("#878382")
black = (0, 0, 0)
white = (255, 255, 255)

# define global variable
clicked = False


class button():
    # colours for button and text
    button_col = ("#878382")
    hover_col = (75, 225, 255)
    click_col = (50, 150, 255)
    text_col = black
    width = 180
    height = 70

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def draw_button(self):

        global clicked
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # create pygame Rect object for the button
        button_rect = Rect(self.x, self.y, self.width, self.height)

        # check mouseover and clicked conditions
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(screen, self.click_col, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(screen, self.hover_col, button_rect)
        else:
            pygame.draw.rect(screen, self.button_col, button_rect)

        # add shading to button
        pygame.draw.line(screen, white, (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(screen, white, (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(screen, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(screen, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

        # add text to button
        text_img = font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
        return action


counter = 4
iniciar = button(200, 350, 'Iniciar Juego!')
bajarnivel = button(75, 200, 'Bajar')
subirnivel = button(325, 200, 'Subir')

run = True
while run:

    screen.fill(bg)

    if iniciar.draw_button():
        if counter < 4:
            print('No se puedo iniciar')
        else:
            print("Iniciando")
            run = False

            pygame.init()

    if subirnivel.draw_button():
        counter += 1
        if counter == 0 or counter <= 4:
            print('Ingrese un nivel correcto por favor!')
    if bajarnivel.draw_button():
        counter -= 1
        if counter <= 4:
            print('Ingrese un nivel correcto por favor!')

    counter_img = font.render(str(counter), True, red)
    screen.blit(counter_img, (280, 450))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
if counter > 4:
    pass

pygame.init()

m = 0  # Variable que regula el metodo safe
juego = Df.Juego(700, 600, counter)  # Inicializa el juego
t1 = time.perf_counter()  # Obtiene el momento en que se inicio el juegot
# t1=0

juega = True  # Permite leer o no las acciones sobre el mapa
pos_arriba = (juego.centro[0] - 75, juego.centro[1] - (juego.width + 5) * (
        juego.size / 2) - 40)  # Posicion de los mensajes arriba de la cuadricula
pos_abajo = (juego.centro[0], juego.centro[1] + (juego.width + 5) * (
        juego.size / 2) + 15)  # Posicion de los mensajes abajo de la cuadricula

screen_width = 700
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Button Demo')

font = pygame.font.SysFont('Constantia', 16)

# define colours
bg = (204, 102, 0)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

# define global variable
clicked = False


# boton para refinar

class button():
    # colours for button and text
    button_col = (150, 0, 0)
    hover_col = (50, 200, 200)
    click_col = (50, 150, 255)

    text_col = black
    width = 120
    height = 40

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def draw_button(self):

        global clicked
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # create pygame Rect object for the button
        button_rect = Rect(self.x, self.y, self.width, self.height)

        # check mouseover and clicked conditions
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(screen, self.click_col, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(screen, self.hover_col, button_rect)
        else:
            pygame.draw.rect(screen, self.button_col, button_rect)

        # add shading to button
        pygame.draw.line(screen, white, (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(screen, white, (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(screen, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(screen, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

        # add text to button
        text_img = font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
        return action


run = True  # Regula el ciclo
# ----------------------------- Mainloop ------------------------------------------------------------------------------------------------------------------------------------------------------------------
while run:
    juego.MostrarCuadricula()
    event = pygame.event.poll()  # Lee los eventos
    if event.type == pygame.QUIT:
        run = False  # Termina el ciclo
    if event.type == pygame.MOUSEBUTTONDOWN and juega:
        pos = event.dict['pos']  # Lee la posicion del mouse
        if event.button == 1:
            if m == 0:
                m = juego.safe(
                    pos)  # Ejecuta el metodo safe, si se ejecuta adecuadamente retorna 1 y no se vuelve a hacer
            juego.ejecucion(pos)
        if event.button == 3:
            juego.PonerOQuitarBandera(pos)

    msg_banderas = juego.temp.render("Banderas: {0}".format(juego.banderas_restantes), 1,
                                     (255, 255, 0))  # Mensaje de las banderas restantes
    pygame.draw.rect(juego.ventana, (0, 0, 0),
                     (pos_abajo[0] + 100, pos_abajo[1], juego.width * 20, 30))  # Fondo del mensaje
    juego.ventana.blit(msg_banderas, (pos_abajo[0] + 100, pos_abajo[1]))  # Imprime el mensaje

    if juego.cont_band == juego.banderas_max:  # Si todas las banderas estan bien colodadas
        msg = juego.msg.render("Victoria", 1, (255, 255, 0))  # Mensaje de victoria
        pygame.draw.rect(juego.ventana, (0, 0, 0),
                         (pos_arriba[0], pos_arriba[1], juego.width * 10, 30))  # Imprime el fondo del mensaje
        juego.ventana.blit(msg, pos_arriba)  # Imprime el mensaje
        pygame.display.update()  # Actualiza por ultima vez
        juega = False  # Hace que deje de leer clicks en la cuadricula
        quit = button(150, 560, 'Ver resultados?')
        quit1 = button(440, 560, 'Jugar de nuevo')
        quit2 = button(300, 560, 'Elegir Nivel')

        if quit2.draw_button():
            pygame.quit()
            Jorge = subprocess.run([sys.executable, '../Student/GameJorge.py'])

        if quit1.draw_button():
            pygame.init()

            m = 0  # Variable que regula el metodo safe
            juego = Df.Juego(700, 600, counter)  # Inicializa el juego
            t1 = time.perf_counter()  # Obtiene el momento en que se inicio el juego
            juega = True  # Permite leer o no las acciones sobre el mapa
            pos_arriba = (juego.centro[0] - 75, juego.centro[1] - (juego.width + 5) * (
                    juego.size / 2) - 40)  # Posicion de los mensajes arriba de la cuadricula
            pos_abajo = (juego.centro[0], juego.centro[1] + (juego.width + 5) * (
                    juego.size / 2) + 15)  # Posicion de los mensajes abajo de la cuadricula
            # counter = 5

        counter_img = font.render(str(counter), True, red)
        screen.blit(counter_img, (280, 450))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

        if quit.draw_button():
            juego.graf()
            # La leyenda en la esquina superior izquierda es aleatoria, puede cambiar la posicion nosotros mismos

        counter_img = font.render(str(counter), True, red)
        screen.blit(counter_img, (280, 450))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    elif not juego.est:  # Si clickeo una mina
        msg = juego.msg.render("Perdiste", 1, (255, 255, 0))  # Mensaje de derrota
        pygame.draw.rect(juego.ventana, (0, 0, 0),
                         (pos_arriba[0], pos_arriba[1], juego.width * 10, 30))  # Imprime el fondo del mensaje
        juego.ventana.blit(msg, pos_arriba)  # Imprime el mensaje
        juego.MostrarRespuesta()
        pygame.display.update()  # Actualiza por ultima vez
        juega = False  # Hace que deje de leer clicks en la cuadricula

        again = button(440, 560, 'Jugar de nuevo')
        quit1 = button(150, 560, 'Ver resultados?')
        quit2 = button(300, 560, 'Elegir Nivel')

        if quit2.draw_button():
            pygame.quit()
            Jorge = subprocess.run([sys.executable, '../Student/GameJorge.py'])

        if quit1.draw_button():
            juego.graf()
            # La leyenda en la esquina superior izquierda es aleatoria, puede cambiar la posicion nosotros mismos

        counter_img = font.render(str(counter), True, red)
        screen.blit(counter_img, (280, 450))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

        if again.draw_button():
            pygame.init()

            m = 0  # Variable que regula el metodo safe
            juego = Df.Juego(700, 600, counter)  # Inicializa el juego
            t1 = time.perf_counter()  # Obtiene el momento en que se inicio el juego
            juega = True  # Permite leer o no las acciones sobre el mapa
            pos_arriba = (juego.centro[0] - 75, juego.centro[1] - (juego.width + 5) * (
                    juego.size / 2) - 40)  # Posicion de los mensajes arriba de la cuadricula
            pos_abajo = (juego.centro[0], juego.centro[1] + (juego.width + 5) * (
                    juego.size / 2) + 15)  # Posicion de los mensajes abajo de la cuadricula
            # counter = 5

        counter_img = font.render(str(counter), True, red)
        screen.blit(counter_img, (280, 450))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()



    else:
        juego.ImpTiempo(t1)
        pygame.display.update()
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
pygame.quit()
