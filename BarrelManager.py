from Barril import *
from BarrilSaltarin import *
from BarrilEnLlamas import*
import copy
class BarrelManager (object):
    _instancia = None
    def __new__(self):
        if self._instancia==None:
            self._instancia = super(BarrelManager, self).__new__(self)
            self.protoBarril = Barril()
            self.protoSaltarin = BarrilSaltarin()
            self.protoLlamas = BarrilEnLlamas()
            self.protoBarril = Barril()
            self.protoSaltarin = BarrilSaltarin()
            self.protoLlamas = BarrilEnLlamas()
        return self._instancia
    def clonarBarril(self):
        return copy.copy(self.protoBarril)
    def clonarSaltarin(self):
        return copy.copy(self.protoSaltarin)
    def clonarLlamas(self):
        return copy.copy(self.protoLlamas)
