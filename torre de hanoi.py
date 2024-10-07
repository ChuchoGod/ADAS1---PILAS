class Pila:
    def __init__(self):
        self.items = []
    
    def esta_vacia(self):
        return self.items == []
    
    def apilar(self, item):
        self.items.append(item)
    
    def desapilar(self):
        return self.items.pop()

def mover_disco(origen, destino):
    print(f"Mover disco de {origen} a {destino}")

def hanoi(n, origen, destino, auxiliar):
    if n == 1:
        mover_disco(origen, destino)
    else:
        hanoi(n-1, origen, auxiliar, destino)
        mover_disco(origen, destino)
        hanoi(n-1, auxiliar, destino, origen)

n = 3
hanoi(n, 'A', 'C', 'B')
