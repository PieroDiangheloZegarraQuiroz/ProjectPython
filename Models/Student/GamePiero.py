import pygame
import sys
from Models.Student import GraphicPiero
import matplotlib.pyplot as plt

pygame.init()

width = 400
height = 500
display = pygame.display.set_mode((width, height), pygame.NOFRAME)
clock = pygame.time.Clock()

background = (23, 32, 42)
white = (236, 240, 241)

# Color Codes
color = [(120, 40, 31), (148, 49, 38), (176, 58, 46), (203, 67, 53), (231, 76, 60), (236, 112, 99), (241, 148, 138),
         (245, 183, 177), (250, 219, 216), (253, 237, 236),
         (254, 249, 231), (252, 243, 207), (249, 231, 159), (247, 220, 111), (244, 208, 63), (241, 196, 15),
         (212, 172, 13), (183, 149, 11), (154, 125, 10), (125, 102, 8),
         (126, 81, 9), (156, 100, 12), (185, 119, 14), (202, 111, 30), (214, 137, 16), (243, 156, 18), (245, 176, 65),
         (248, 196, 113), (250, 215, 160), (253, 235, 208), (254, 245, 231),
         (232, 246, 243), (162, 217, 206), (162, 217, 206),
         (115, 198, 182), (69, 179, 157), (22, 160, 133),
         (19, 141, 117), (17, 122, 101), (14, 102, 85),
         (11, 83, 69),
         (21, 67, 96), (26, 82, 118), (31, 97, 141),
         (36, 113, 163), (41, 128, 185), (84, 153, 199),
         (127, 179, 213), (169, 204, 227), (212, 230, 241),
         (234, 242, 248),
         (251, 238, 230), (246, 221, 204), (237, 187, 153),
         (229, 152, 102), (220, 118, 51), (211, 84, 0),
         (186, 74, 0), (160, 64, 0), (135, 54, 0),
         (110, 44, 0)
         ]

colorIndex = 0

brickH = 10
brickW = 100

score = 0
speed = 3

espiral = False


# Button Principal frame
class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('roboto', 56)

            text = font.render(self.text, True, (255, 255, 255))
            win.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

class button2():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('Forte', 20)

            text = font.render(self.text, True, (255, 255, 255))
            win.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

# Single Brick Class
class Brick:
    def __init__(self, x, y, color, speed):
        self.x = x
        self.y = y
        self.w = brickW
        self.h = brickH
        self.color = color
        self.speed = speed

    def draw(self):
        pygame.draw.rect(display, self.color, (self.x, self.y, self.w, self.h))

    def move(self):
        self.x += self.speed
        if self.x > width:
            self.speed *= -1
        if self.x + self.w < 1:
            self.speed *= -1


# Complete Stack
class Stack:
    def __init__(self):
        global colorIndex
        self.stack = []
        self.initSize = 25
        for i in range(self.initSize):
            newBrick = Brick(width / 2 - brickW / 2, height - (i + 1) * brickH, color[colorIndex], 0)
            colorIndex += 1
            self.stack.append(newBrick)

    def show(self):
        for i in range(self.initSize):
            self.stack[i].draw()

    def move(self):
        for i in range(self.initSize):
            self.stack[i].move()

    def addNewBrick(self):
        global colorIndex, speed

        if colorIndex >= len(color):
            colorIndex = 0

        y = self.peek().y
        if score > 50:
            speed += 0
        elif score % 5 == 0:
            speed += 1

        newBrick = Brick(width, y - brickH, color[colorIndex], speed)
        colorIndex += 1
        self.initSize += 1
        self.stack.append(newBrick)

    def peek(self):
        return self.stack[self.initSize - 1]

    def pushToStack(self):
        global brickW, score
        b = self.stack[self.initSize - 2]
        b2 = self.stack[self.initSize - 1]
        if b2.x <= b.x and not (b2.x + b2.w < b.x):
            self.stack[self.initSize - 1].w = self.stack[self.initSize - 1].x + self.stack[self.initSize - 1].w - b.x
            self.stack[self.initSize - 1].x = b.x
            if self.stack[self.initSize - 1].w > b.w:
                self.stack[self.initSize - 1].w = b.w
            self.stack[self.initSize - 1].speed = 0
            score += 1
        elif b.x <= b2.x <= b.x + b.w:
            self.stack[self.initSize - 1].w = b.x + b.w - b2.x
            self.stack[self.initSize - 1].speed = 0
            score += 1
        else:
            gameOver()
        for i in range(self.initSize):
            self.stack[i].y += brickH

        brickW = self.stack[self.initSize - 1].w


# Game Over
def gameOver():
    redButton = button((41, 128, 185), 100, 150, 210, 80, "Play Again")
    blueButton = button((41, 128, 185), 100, 250, 210, 80, "Statistics")
    CloseButton = button((41, 128, 185), 100, 350, 210, 80, "Close")
    # crear nuevo frame
    def redrawWindow():
        display.fill((23, 32, 42))

        fontG = pygame.font.SysFont("Agency FB", 50)
        textG = fontG.render("Game Over!", True, (255, 255, 255))
        display.blit(textG, (110, 50))

        redButton.draw(display, (0, 0, 0))
        blueButton.draw(display, (0, 0, 0))
        CloseButton.draw(display, (0, 0, 0))

    loop = True

    # connect = False
    while loop:
        redrawWindow()
        pygame.display.update()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    gameLoop()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if redButton.isOver(pos):
                    print("Return Game")
                    gameLoop()
                if blueButton.isOver(pos):
                    Statistics = "Statistics"
                    print(Statistics)
                    g = GraphicPiero.graph()
                    plt.show()

                if CloseButton.isOver(pos):
                    print("press quit")
                    pygame.quit()
                    exit()

            if event.type == pygame.MOUSEMOTION:
                if redButton.isOver(pos):
                    redButton.color = (0, 212, 138)
                else:
                    redButton.color = (41, 128, 185)

                if blueButton.isOver(pos):
                    blueButton.color = (0, 212, 138)
                else:
                    blueButton.color = (41, 128, 185)

                if CloseButton.isOver(pos):
                    CloseButton.color = (0, 212, 138)
                else:
                    CloseButton.color = (41, 128, 185)

        pygame.display.update()
        clock.tick()


# Displaying the Score on Screen
def showScore():
    font = pygame.font.SysFont("Forte", 30)
    text = font.render("Score: " + str(score), True, white)
    display.blit(text, (20, 20))

# funciona como redrawWindow, pero en principal

blueButtonSS = button2((255, 0, 0), 355, 10, 30, 30, "X")
def ClosePrincipal():
    blueButtonSS.draw(display, (0, 0, 0))

# ButtonStatistics = button2((255, 0, 0), 300, 10, 30, 30, "s")
# def statistics():
#     ButtonStatistics.draw(display, (0, 0, 0))

# The Main Game Loop
def gameLoop():
    global brickW, brickH, score, colorIndex, speed
    loop = True

    brickH = 10
    brickW = 100
    colorIndex = 0
    speed = 3

    score = 0

    stack = Stack()
    stack.addNewBrick()


    # for event in pygame.event.get():
    #     poss = pygame.mouse.get_pos()
    #     if event.type == pygame.MOUSEBUTTONDOWN:
    #         if ButtonStatistics.isOver(poss):
    #             g = GraphicPiero.graph()
    #             plt.show()

    while loop:
        for event in pygame.event.get():
            pos2 = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                stack.pushToStack()
                stack.addNewBrick()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if blueButtonSS.isOver(pos2):
                    pygame.quit()
                    exit()

        display.fill(background)
        stack.move()
        stack.show()

        showScore()
        ClosePrincipal()
        # statistics()
        pygame.display.update()
        clock.tick(60)

gameLoop()