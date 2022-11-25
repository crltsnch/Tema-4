import heapq #estructura de montículos
class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq=freq #frecuencia de cada simbolo
        self.symbol=symbol #simbolos
        self.left=left #nodo que sale hacia la izquierda del nodo anterior
        self.right=right #nodo que sale hacia la derecha del nodo anterior


