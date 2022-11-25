import heapq #estructura de montículos
class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq=freq    #frecuencia de cada simbolo
        self.symbol=symbol    #simbolos
        self.left=left    #nodo que sale hacia la izquierda del nodo anterior
        self.right=right    #nodo que sale hacia la derecha del nodo anterior
        self.huff=''    #forma de arbol de huffman (0/1)

    def __lt__(self, nxt):
        return self.freq < nxt.freq

#funcion que imprima árbol de huffman
def printNodes(node, val=''):
    nuevoValor= val + str(node.huff)   #huffman para el nodo actual

    #si el nodo no es un nodo extremo entonces recorrelo
    if (node.left)

