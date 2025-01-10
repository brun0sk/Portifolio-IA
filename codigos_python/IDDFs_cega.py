class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = {}

    def adiciona_no(self, u, v):
        if str(u) in self.grafo:
            self.grafo[str(u)].append(str(v))
            
        else:    
            self.grafo.update({str(u): []})
            self.grafo[str(u)].append(str(v))

    def DLS(self, inicio, objetivo, profundidade_limite):
        if (int(inicio) == objetivo):
            return True

        if (profundidade_limite <= 0):
            return False

        for i in self.grafo[str(inicio)]:
            print(i)
            if self.DLS(i, objetivo, profundidade_limite-1):   
                return True

        return False

    def IDDFS(self, inicio, objetivo, profundidade):
        for i in range(profundidade):
            if (self.DLS(inicio, objetivo, i)):
                return True
        return False
    
if __name__:
    g = Grafo (7)
    g.adiciona_no(0, 1)
    g.adiciona_no(0, 2)
    g.adiciona_no(1, 3)
    g.adiciona_no(1, 4)
    g.adiciona_no(2, 5)
    g.adiciona_no(2, 6)

    objetivo = 4; profundidade_maxima = 3; inicio = 0

    if g.IDDFS(inicio, objetivo, profundidade_maxima) == True:
        print ("Objetivo encontrado")
    else :
        print ("Objetivo não encontrado")