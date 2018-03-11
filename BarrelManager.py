from Barril import *
from BarrilSaltarin import *
from BarrilEnLlamas import*
import copy
class BarrelManager:
    def __init__(self):
        self.protoBarril = Barril()
        self.protoSaltarin = BarrilSaltarin()
        self.protoLlamas = BarrilEnLlamas()
    def clonarBarril(self):
        return copy.copy(self.protoBarril)
    def clonarSaltarin(self):
        return copy.copy(self.protoSaltarin)
    def clonarLlamas(self):
        return copy.copy(self.protoLlamas)
