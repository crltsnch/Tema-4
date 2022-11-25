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

#funcion que imprima árbol de Huffman
def printNodes(node, val=''):
    nuevoVal= val + str(node.huff)   #huffman para el nodo actual

    #si el nodo no es un nodo extremo entonces recorrelo
    if (node.left):
        printNodes(node.left, nuevoVal)
    if (node.right):
        printNodes(node.right, nuevoVal)

    #si el nodo es extremo imprimelo
    if (not node.left and not node.right):
        print(f"{node.symbol} -> {nuevoVal}")

#datos de los caracteres y sus frecuencias
symbols=['A', 'F', 1, 2, 0, 'M', 'T']
freq=[0.2, 0.17, 0.13, 0.21, 0.05, 0.09, 0.15]

#lista que contiene los nodos no utilizados
nodes = []

#convertir los caracteres y las frecuencias en un árbol de Huffman
for x in range(len(symbols)):
    heapq.heappush(nodes, node(freq[x], symbols[x]))

while len(nodes)