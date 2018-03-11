from Barril import*
class BarrilSaltarin(Barril):
    def __init__(self):
        Barril.__init__(self)
        self.estado=True
        self.turno=True
    def mover(self):
        if self.turno:
            if self.estado:
                if self.rect.y<=200:          
                    self.estado=False
                else:
                    self.rect.y-=1
                    #self.rect.x-=2
            else:
                if self.rect.y>=620:
                    self.estado=True
                else:
                    self.rect.y+=1
                    #self.rect.x-=2
            self.turno=False
        else:
            self.turno=True
            self.rect.x-=1
            
    
