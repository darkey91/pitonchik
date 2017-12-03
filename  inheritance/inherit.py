#че я хочу сделать ? класс животных PETS и дочерние классы CAT DOG PARROT
import sys
import pygame
from pygame.locals import *
import time

class Pet:
    x = 10
    y = 10
    def __init__(self, name, age, img, snd):
        self.name = name
        self.age = age
        self.imageObj = pygame.image.load(img)
        self.soundObj = pygame.mixer.Sound(snd)

    def getName(self):
        return self.name



pygame.init()
colWhite = (255,255,255)

ptichka  = Pet("Koka", 2, 'bird.png', 'bird.wav')

displaysurf = pygame.display.set_mode((500, 500), 0, 32)
while True:
    displaysurf.fill(colWhite)
    displaysurf.blit(ptichka.imageObj, (ptichka.x, ptichka.y))
    ptichka.soundObj.play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.eit()

    pygame.display.update()




