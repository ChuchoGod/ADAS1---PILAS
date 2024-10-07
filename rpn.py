class Pila:
    def __init__(self):
        self.items = []
    
    def esta_vacia(self):
        return self.items == []
    
    def apilar(self, item):
        self.items.append(item)
    
    def desapilar(self):
        return self.items.pop()
    
    def ver_cima(self):
        return self.items[-1] if not self.esta_vacia() else None

def evaluar_posfija(expresion):
    pila = Pila()
    operadores = '+-*/'

    for token in expresion.split():
        if token not in operadores:
            pila.apilar(int(token))
        else:
            operando2 = pila.desapilar()
            operando1 = pila.desapilar()
            
            if token == '+':
                resultado = operando1 + operando2
            elif token == '-':
                resultado = operando1 - operando2
            elif token == '*':
                resultado = operando1 * operando2
            elif token == '/':
                resultado = operando1 / operando2
            
            pila.apilar(resultado)
    
    return pila.desapilar()

expresion = "3 4 + 2 * 7 /"
print(f"Resultado de la expresión posfija: {evaluar_posfija(expresion)}")
