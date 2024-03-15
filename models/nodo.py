class Nodo:
    """
    Clase que representa un nodo en un árbol de búsqueda.

    Cada nodo del árbol guarda la siguiente información:
    - El estado del problema
    - Una referencia al nodo padre
    - El operador que se aplicó para generar el nodo
    - Profundidad del nodo
    - El costo de la ruta desde la raíz hasta el nodo
    """

    def __init__(self):
        """
        Inicializa un nuevo nodo.

        Atributos:
        - estado: El estado del problema.
        - padre: Una referencia al nodo padre.
        - operador: El operador que se aplicó para generar el nodo.
        - profundidad: La profundidad del nodo en el árbol.
        - costo_acumulado: El costo acumulado de la ruta desde la raíz hasta el nodo.
        """
        self.estado = None
        self.padre = None
        self.operador = None
        self.profundidad = None
        self.costo_acumulado = None

    def get_estado(self):
        return self.estado

    def set_estado(self, estado):
        self.estado = estado

    def get_padre(self):
        return self.padre

    def set_padre(self, padre):
        self.padre = padre

    def get_operador(self):
        return self.operador

    def set_operador(self, operador):
        self.operador = operador

    def get_profundidad(self):
        return self.profundidad

    def set_profundidad(self, profundidad):
        self.profundidad = profundidad

    def get_costo_acumulado(self):
        return self.costo_acumulado

    def set_costo_acumulado(self, costo_acumulado):
        self.costo_acumulado = costo_acumulado

    def expandir(self):

        hijos = []

        agente = self.get_estado()[0]
        ambiente = self.get_estado()[1]

        sensores = {
            'izquierda': agente.libre_izquierda(),
            'arriba': agente.libre_arriba(),
            'derecha': agente.libre_derecha(),
            'abajo': agente.libre_abajo(),
        }
        operadores = {
            'izquierda': agente.izquierda(),
            'arriba': agente.arriba(),
            'derecha': agente.derecha(),
            'abajo': agente.abajo(),
        }

        for operador, percepcion in sensores:

            if percepcion:

                nuevo_agente = agente
                nuevo_agente.set_coordenadas(operadores[operador])
                nuevo_ambiente = ambiente
                nuevo_ambiente[nuevo_agente.coordenadas[0]
                               ][nuevo_agente.coordenadas[1]] = 0

                nuevo_estado = (nuevo_agente, nuevo_ambiente, operador)

                hijo = Nodo()
                hijo.set_estado(nuevo_estado)
                hijo.set_padre(self)
                hijo.set_operador(operador)
                hijo.set_profundidad(self.get_profundidad() + 1)
                hijo.set_costo_acumulado(self.get_costo_acumulado() + 1)

                hijos.append(hijo)

        return hijos
