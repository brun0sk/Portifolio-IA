from heapq import heappush, heappop

class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = {}

    def adiciona_no(self, u, v, w):
        if str(u) in self.grafo:
            self.grafo[str(u)].append((str(v), w))
            
        else:    
            self.grafo.update({str(u): []})
            self.grafo[str(u)].append((str(v), w))

    def beam_search(graph, start, goal, k, heuristic):

        # Fila de prioridade
        frontier = [(heuristic(start), start, [start])]
        
        while frontier:
            # Seleciona os k melhores nós da fronteira
            next_frontier = []
            for _ in range(min(k, len(frontier))):
                _, current, path = heappop(frontier)
    
                if current == goal:
                    return path
                
                if current in graph:  
                    # Expande os vizinhos
                    for neighbor, cost in graph[current]:
                        new_path = path + [neighbor]
                        priority = heuristic(neighbor)
                        heappush(next_frontier, (priority, neighbor, new_path))
            
            frontier = next_frontier
        
        return None


# Exemplo de uso
if __name__ == "__main__":
    g = Grafo(12)
    
    g.adiciona_no("A", "B", 1)
    g.adiciona_no("A", "C", 2)
    g.adiciona_no("A", "D", 4)
    g.adiciona_no("B", "E", 5)
    g.adiciona_no("B", "F", 1)
    g.adiciona_no("C", "G", 3)
    g.adiciona_no("C", "H", 1)
    g.adiciona_no("D", "I", 2)
    g.adiciona_no("D", "J", 3)
    g.adiciona_no("F", "K", 2)
    g.adiciona_no("J", "L", 1)

    # Heurística (distância estimada até o objetivo)
    heuristic = lambda node: {
        "A": 10, "B": 8, "C": 5, "D": 7, "E": 9, "F": 4, 
        "G": 7, "H": 3, "I": 6, "J": 2, "K": 1, "L": 0
    }.get(node, float("inf"))
    
    start = "A"
    goal = "L"
    k = 2  # Largura do feixe
    
    result = Grafo.beam_search(g.grafo, start, goal, k, heuristic)
    print("Caminho encontrado:", result)
