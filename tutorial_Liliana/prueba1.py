
def AMLO(libertad=100, avance=100, democracia=100):
    '''esta función necesita de más mexicanos
    '''
    a=libertad*avance+democracia
    return a

def adivinogenero(nombre):
    
    genero=None
    
    if nombre.endswith('a'):
        genero='mujer'
    elif nombre.endswith('o'):
        genero='hombre'
    else:
        genero='hermafrodita'
    
    return genero

class partido():
    
    def __init__(self,nombre):
        self.nombre=nombre
        self.honestidad=self.calcularhonestidad()    
        
    def calcularhonestidad(self):
        return len(self.nombre)
    
class persona():
    '''Candidatos non gratos
    '''
    
    def __init__(self,nombre,nombrepartido):
        
        self.nombre=nombre
        self.partido=partido(nombrepartido)
        self.genero=adivinogenero(nombre)
        
    def numerodeletrasdelnombre(self):
        return len(self.nombre)