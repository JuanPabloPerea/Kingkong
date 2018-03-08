import pygame
from pygame.sprite import Sprite
from pygame import*
import util
class Jugador (Sprite):
    _instancia = None
    def __new__(self):
        if self._instancia == None:
            self._instancia = super (Jugador, self).__new__(self)
            self.imagen = util.cargar_imagen('imagenes/jumpMan.png')
            self.rect = self.imagen.get_rect()
            self.posicionX = 0
            self.posicionY = 240
            self.rect.move_ip(self.posicionX, self.posicionY)
            return self._instancia
        else:
            return self._instancia
            
                                                            
