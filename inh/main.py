import pygame
import time
import random

class Transport:
    def __init__(self, img, snd):
        self.transport_img = pygame.image.load(img)
        self.transport_snd = snd

    def displayImg(self,x,y):
        gmDisplay.blit(self.transport_img,  (x, y))

pygame.init()

dispWidth = 1200
dispLenght = 800

gmDisplay = pygame.display.set_mode((dispWidth,dispLenght))
pygame.display.set_caption('Transport')

black = (0,0,0)
white = (255, 255, 255)
green = (0, 255, 0)

clock = pygame.time.Clock()
motik = Transport('motik.png', 1)

def button(surf, color, x, y, width, heigh, text, action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    pygame.draw.rect(surf, color, (x, y, width, heigh))

    if x + width > mouse[0] > x and y + heigh > mouse[1] > y:
        if click[0] == True:
            print('oi')

def text_display(text):
    cap = pygame.font.Font('GoodDog.otf', 50)



def text_object(text, font):
    textSur = font.render(text, True, green)
    #должен вернуть мне объекты для отображений

#надо на кнопке нормально отобразить текст


def gameLoop():
    x = 850
    y = 570

    x1 = 0

    isEndDisplay = False

    while not isEndDisplay:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isEndDisplay = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1 = -5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x1 = 0

        x += x1

        gmDisplay.fill(white)

        font = pygame.font.SysFont(None, 25)
        text = font.render("HELLO ", True, black)
        gmDisplay.blit(text, (0, 0))

        motik.displayImg( x, y)

        if(x  < 0):
            isEndDisplay = True

        button(gmDisplay, black, 500, 500, 150, 100, 1, 2)

        pygame.display.update()
        clock.tick(30)

gameLoop()
pygame.quit()
quit()