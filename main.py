import pygame
from pygame.locals import *
import random as rd
from Sorting import *

# initialisation des variables
windowDim = [1920, 1080]
backgroundColor = (0, 0, 0)
l = []
for i in range(windowDim[1]):
    l.append(i)
#for i in range(20):
#    l.append(i + 1)
rd.shuffle(l)
min = 0
max = len(l) - 1
type = 0 # 0 - selection; 1 - trie a bulle
sorted = False

pygame.init()

# initialisation de la fenetre
fenetre = pygame.display.set_mode((windowDim[0], windowDim[1]), pygame.FULLSCREEN)
pygame.display.set_caption("fenetre type")  # nom de la fenetre

# fond backgroundColor
fenetre.fill(backgroundColor)


# rafraichissement de la fenetre
pygame.display.flip()
# boucle infinie
continuer = True  # si continuer vaut False, alors la boucle (et le programme) s'arrete(nt)
while continuer:

    # parcourir les evenements
    for event in pygame.event.get():

        # quitte l'app si on appuie sur la croix
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            continuer = False
        if event.type == KEYDOWN and event.key == K_SPACE:
            rd.shuffle(l)
            min = 0
            max = len(l) - 1
            sorted = False

        if event.type == KEYDOWN and event.key == K_s:
            rd.shuffle(l)
            min = 0
            max = len(l) - 1
            sorted = False
        if event.type == KEYDOWN and event.key == K_t:
            type +=1
            if type > 2:
                type = 0

            rd.shuffle(l)
            min = 0
            max = len(l) - 1
            if type == 2:
                min = 1
            sorted = False

    # update
    if type == 0:
        if min < len(l):
            a = selection_step(l, min)
            l = a[0]
            min = a[1]
        else:
            sorted = True
        #    rd.shuffle(l)
        #    min = 0
    elif type == 1:
        if max > 0:
            a = trieABulle_step(l, max)
            l = a[0]
            max = a[1]
        else:
            sorted = True
        #    rd.shuffle(l)
        #    max = len(l) - 1
    elif type == 2:
        if min < len(l):
            a = insertion_step(l, min)
            l = a[0]
            min = a[1]
        else:
            sorted = True
        #    rd.shuffle(l)
        #    min = 0


    # draw
    fenetre.fill(backgroundColor)
    for i in range(len(l)):
        if sorted:
            pygame.draw.rect(fenetre, (0, 255, 0), (windowDim[0]/len(l)*i, windowDim[1] - (windowDim[1]//len(l)*l[i]), windowDim[0]//len(l), windowDim[1]//len(l)*l[i]))

        else:
            pygame.draw.rect(fenetre, (255, 255, 255), (windowDim[0]/len(l)*i, windowDim[1] - (windowDim[1]//len(l)*l[i]), windowDim[0]//len(l), windowDim[1]//len(l)*l[i]))

    # rafraichissement de la fenetre
    pygame.display.flip()
