import pygame
from pygame.sprite import Sprite
from pygame import*
import util
class Barril(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.imagen = util.cargar_imagen('Imagenes/barrilr.png')
        self.rect = self.imagen.get_rect()
        self.posicionX = 1280
        self.posicionY = 620
        self.rect.move_ip(self.posicionX, self.posicionY)
        self.b=True
    def mover (self):
        if self.b:
            self.rect.x-=1
            self.b=False
        else:
            self.b=True
        if self.rect.x<0:
            self.rect.x=1280
