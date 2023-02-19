##recursion por que todo se basa en un solo nodo
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class ListaEnlazada: 
    def __init__(self):
        self.cabeza = None
## Agregar nodos
def agragar_nodo(self,dato):
    nodo = Node(dato)
    if self.es_vacio():
        self.cabeza = nodo
    else:
        nodo_actual = self.cabeza
        while nodo_actual.next is not None :
            nodo_actual = nodo_actual.next
        nodo_actual.next = nodo
##Imprimir nodos
def imprimir(self):
    nodo_actual = self.cabeza
    while nodo_actual is not None:
        print(nodo_actual.data)
        nodo_actual = nodo_actual.next
##Eliminar nodos
def eliminar(self, dato):
    nodo_actual = self.cabeza
    if nodo_actual.data == dato :
        self.cabeza = nodo_actual.next
        return
    while nodo_actual.next is not None:
        if nodo_actual.next.data == dato:
            nodo_actual.next = nodo_actual.next.next
            return
        nodo_actual =  nodo_actual.next




