
import pygame, sys
from pygame.locals import*
from Jugador import*
booleano = True
ventana = pygame.display.set_mode( (1280,720) )
pygame.display.set_caption("DK PreAlpha")
jugador = Jugador()
while booleano:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            booleano= False
            break
    jugador.blit(jugador.imagen,jugador.rect)
