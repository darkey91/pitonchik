import pygame

pygame.init()

dispHeight = 600
dispWidth = 800

gameDisplay = pygame.display.set_mode((dispWidth, dispHeight))
pygame.display.set_caption('EVILS')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()

toClose = False

class evil(object):
    cnt = 1
    untilWalk = 10
    untilIdle = 6
    imgPath = ''

    isAppearAllowed = False
    isAttackAllowed = False

    def __init__(self, species):
        self.kind = species
        self.didWalk = False
        self.didIdle = False

    def idle(self):
        if self.didIdle == False or self.cnt == self.untilIdle:
            self.cnt = 1

        self.imgPath = self.kind + '/idle/idle_' + str(self.cnt) + '.png'

        self.cnt += 1

        self.didIdle = True
        self.didWalk = False

    def walk(self):
        if self.didWalk == False or self.cnt == self.untilWalk:
            self.cnt = 1

        self.imgPath = self.kind + '/walk/go_' + str(self.cnt) + '.png'
        self.cnt += 1

        self.didIdle = False
        self.didWalk = True

    def display(self, x, y):
        imgEvil = pygame.image.load(self.imgPath)
        gameDisplay.blit(imgEvil, (x, y))

class Zombie(evil):

    untilAppear = 11
    evil.isAppearAllowed = True

    def __init__(self, species):
        evil.__init__(self, species = species)
        evil.isAttackAllowed = False

        evil.untilWalk = 10
        evil.untilIdle = 6


    def appear(self , x, y):
        finish = False
        i = 1

        while not finish:
            if i == self.untilAppear:
                finish = True
            self.imgPath = self.kind + '/appear/appear_' + str(i) + '.png'

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finish = True

            gameDisplay.fill(white)
            evil.display(self, x, y)

            pygame.display.update()
            clock.tick(8)
            i += 1

class Skeleton(Zombie):
    untilAttack = 8

    def __init__(self, species):
        evil.__init__(self, species = species)
        evil.untilWalk = 8
        evil.untilIdle = 6
        Zombie.untilAppear = 10
        evil.isAttackAllowed = True

    def display(self, x, y):
        y = y - 40
        evil.display(self, x, y)

    def attack(self, x, y):
        x-= 110
        y -=2
        finish = False
        i = 1

        while not finish:
            if i == self.untilAttack:
                finish = True

            self.imgPath = self.kind + '/attack/hit_' + str(i) + '.png'

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finish = True

            gameDisplay.fill(white)
            Skeleton.display(self, x, y)

            pygame.display.update()
            clock.tick(8)
            i += 1

class button:
    color = (255, 255, 255)
    width = 100
    height = 50

    def __init__(self, text, action, x, y):
        self.caption = text
        self.action = action
        self.x = x
        self.y = y


x_change = 0

x = dispWidth * 0.7
y = dispHeight * 0.45

choose = input("Choose evil: \n 1 - Zombie \n 2 - Skeleton\n")

if choose == '1':
    creature = Zombie('zombie')
elif choose == '2':
    creature = Skeleton('skeleton')
else:
    creature = Zombie('zombie')

if creature.isAppearAllowed:
    creature.appear(x, y)

isIdle = True
while not toClose:

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            toClose = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                isIdle = False
                creature.walk()
                x_change = -5
            if event.key == pygame.K_RIGHT and creature.isAttackAllowed == True:
                isIdle = True
                creature.attack(x, y)


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                isIdle = True
                x_change = 0


    x += x_change
    if isIdle:
        creature.idle()
    else:
        creature.walk()

    gameDisplay.fill(white)

    creature.display(x, y)

    pygame.display.update()
    clock.tick(8)

pygame.quit()
quit(0)