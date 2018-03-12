import pygame
from pygame.sprite import Sprite
from pygame import*
import util
class Jugador (Sprite):
    _instancia = None
    def __new__(self):
        if self._instancia == None:
            self._instancia = super (Jugador, self).__new__(self)
            self.imagen = util.cargar_imagen('JumpMan3.png')
            self.rect = self.imagen.get_rect()
            self.posicionX = 0
            self.posicionY = 547
            self.rect.move_ip(self.posicionX, self.posicionY)
            self.saltando=False
            self.salto=0
            return self._instancia
        else:
            return self._instancia
    def mover(self):
        accion = pygame.key.get_pressed()
        if self.saltando:
            if self.salto==0 :
                self.saltando=False
            else:
                self.salto -=1
                self.rect.y-=1
        else:
            if self.rect.y<547:
                self.rect.y +=1
        if accion[K_LEFT] and self.rect.x>0:
            self.rect.x -=1
        elif accion[K_RIGHT] and self.rect.x<=1280:
            self.rect.x +=1
        elif accion[K_UP] and self.saltando==False:
            self.saltando=True
            self.salto=300
    def chocar (self,barriles):
        temp=True
        for barril in barriles:
            if barril.rect.colliderect(self.rect):
                temp=False
        return temp
        
