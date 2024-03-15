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
