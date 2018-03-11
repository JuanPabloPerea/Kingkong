import pygame, sys
from pygame.locals import*
from Jugador import*
from Barril import*
from BarrilSaltarin import*
from random import randint
from BarrilEnLlamas import *
from BarrelManager import*
booleano = True
ventana = pygame.display.set_mode( (1280,720) )
pygame.display.set_caption("DK PreAlpha")
jugador = Jugador()
manager = BarrelManager()
barriles = []
#barril=BarrilSaltarin()
#barriles.append(barril)
contador = 900
def spawn(contador):
    spawnNum=randint(0,2)
    if contador == 0:
        if spawnNum == 1:
            barriles.append(manager.clonarSaltarin())
            contador=2000
        elif spawnNum == 2:
            barriles.append(manager.clonarLlamas())
            contador = 2000
        elif spawnNum == 0:
            barriles.append(manager.clonarBarril())
            contador = 2000
    else:
        contador-=1
    return contador
while booleano:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            booleano= False
            break
    ventana.blit(jugador.imagen,jugador.rect)
    for barril in barriles:
        ventana.blit(barril.imagen,barril.rect)
    jugador.mover()
    for barril in barriles:
        barril.mover()
    booleano = jugador.chocar(barriles)
    contador=spawn(contador)
    pygame.display.update()
    ventana.fill((0,0,0))
        
