class Animals():
    def breathe(self):
        print('Breathing.')
        
class Mammals(Animals):
    def fywm(self):
        print('Feeding young.')

class Giraffes(Mammals):
    def elft(self):
        print('Eating leaves.')
    def lff(self):
        print('Left foot forward,')
    def rff(self):
        print('Right foot forward,')
    def bas(self):
        print('Then both step back and spin!')
    def dance(self):
        self.lff()
        self.rff()
        self.bas()
    pass

Ajay = Giraffes()
