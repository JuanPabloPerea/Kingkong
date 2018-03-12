from Barril import *
import util
class BarrilEnLlamas (Barril):
    def __init__(self):
        Barril.__init__(self)
        self.imagen=util.cargar_imagen('Fuego1.png')
        self.rect.y=470
        self.controlador =5
    def mover(self):
        if self.controlador==5:
            Barril.mover(self)
            self.controlador=0
        else:
            self.controlador +=1
