class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ColaConListasEnlazadas:
    def __init__(self):
        self.frente = None
        self.final = None

    def esta_vacia(self):
        return self.frente is None

    def encolar(self, elemento):
        nuevo_nodo = Nodo(elemento)
        if self.esta_vacia():
            self.frente = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
        self.final = nuevo_nodo

    def desencolar(self, elemento):
        if self.esta_vacia():
            print("La cola está vacía")
            return None
        
        actual = self.frente
        anterior = None
        
        while actual and actual.dato != elemento:
            anterior = actual
            actual = actual.siguiente
        
        if actual is None:
            print(f"Elemento {elemento} no encontrado en la cola")
            return None
        
        if anterior is None:
            self.frente = actual.siguiente
        else:
            anterior.siguiente = actual.siguiente
        
        if actual == self.final:
            self.final = anterior
        
        return actual.dato

    def imprimir_cola(self):
        actual = self.frente
        elementos = []
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        print("Cola:", elementos)

cola = ColaConListasEnlazadas()
while True:
    print("\nOpciones:")
    print("1. Encolar elemento")
    print("2. Desencolar elemento")
    print("3. Mostrar cola")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        elem = input("Ingrese el elemento a encolar: ")
        cola.encolar(elem)
    elif opcion == "2":
        elem = input("Ingrese el elemento a desencolar: ")
        desencolado = cola.desencolar(elem)
        if desencolado is not None:
            print(f"Elemento {desencolado} desencolado")
    elif opcion == "3":
        cola.imprimir_cola()
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida, intente de nuevo.")

