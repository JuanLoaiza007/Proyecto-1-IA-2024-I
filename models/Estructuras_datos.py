# [Estructura_datos.py]

class Operador:
    def __init__(self, nombre, dx, dy):
        """
        Inicializa un operador

        Args:
            nombre (str): El nombre del operador.
            dx (int): El cambio de coordenada en x.
            dy (int): El cambio de coordenada en y.

        Returns:
            None
        """
        self.nombre = nombre
        self.dx = dx  # Cambio en x
        self.dy = dy  # Cambio en y

    def get_nombre(self):
        return self.nombre

    def get_dx(self):
        return self.dx

    def get_dy(self):
        return self.dy


class Estado:
    def __init__(self, x: int, y: int):
        """
        Inicializa un estado.

        Args:
            x (int): La coordenada en x.
            y (int): La coordenada en y.

        Returns:
            None
        """
        self.x = x
        self.y = y

    def get_coordenadas(self):
        return [self.x, self.y]

    def __str__(self):
        """
        Muestra informacion sobre las coordenadas.

        Args:
            None

        Returns:
            Las coordenadas en string.
        """
        return f"({self.x}, {self.y})"


class Problema:
    def __init__(self, estado_inicial, estado_objetivo, matriz):
        """
        Inicializa un nuevo problema

        Args:
            estado_inicial (Estado): El estado actual del problema.
            estado_objetivo (Estado): El estado deseado.
            matriz (): La matriz que representa el ambiente.


        Returns:
            Las coordenadas en string.
        """
        self.estado_inicial = estado_inicial
        self.estado_objetivo = estado_objetivo
        self.matriz = matriz

    def es_valido(self, estado):
        """
        Determina si un estado es valido o no.
        Eg: Un estado NO válido seria que el agente se encontra en las mismas coordenadas que un muro.

        Args:
            estado (Estado): El estado que se desea evaluar.

        Returns:
            True, si el estado es válido
            False, si el estado NO es válido.
        """

        enMatriz = 0 <= estado.x < 10 and 0 <= estado.y < 10
        if not (enMatriz):
            return False

        enPared = self.matriz[estado.x][estado.y] != "1"
        return enMatriz and enPared

    def es_objetivo(self, estado):
        """
        Determina si un estado es el estado deseado/objetivo.

        Args:
            estado (Estado): El estado a evaluar

        Returns:
            True, si el estado es el objetivo.
            False, si el estado no es el objetivo
        """
        return estado.get_coordenadas() == self.estado_objetivo.get_coordenadas()

    def generar_operadores(self, estado):
        """
        Genera las operadores validas para el estado.

        Args:
            estado (Estado): El estado del que se quiere generar operadores

        Returns:
            operadores ([Operador, Operador,... Operador]): Un vector de operadores.
        """
        operadores = []
        # OJO: Aquí hay una corrección para los indices de la matriz,
        # arriba es (0, -1) y así sucesivamente.
        for dy, dx, operador_nombre in [(0, -1, 'arriba'), (0, 1, 'abajo'), (-1, 0, 'izquierda'), (1, 0, 'derecha')]:
            nuevo_estado = Estado(estado.x + dx, estado.y + dy)
            if self.es_valido(nuevo_estado):
                operadores.append(Operador(operador_nombre, dx, dy))
        return operadores

    def resultado(self, estado, operador):
        """
        Genera un nuevo estado aplicando un operador sobre el actual.

        Args:
            estado (Estado): El estado actual.
            operador (Operador): El operador que se quiere aplicar al estado.

        Returns:
            nuevo_estado (Estado): Un nuevo estado que surge de aplicar el operador al estado actual.
            None si el nuevo estado no cumple con las reglas de juego.
        """
        nuevo_estado = Estado(estado.x + operador.dx, estado.y + operador.dy)
        if self.es_valido(nuevo_estado):
            return nuevo_estado
        else:
            return None


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

        # algun for para las opciones válidas
        # hijo = Nodo()
        # hijo.set_estado(nuevo_estado)
        # hijo.set_padre(self)
        # hijo.set_operador(operador)
        # hijo.set_profundidad(self.get_profundidad() + 1)
        # hijo.set_costo_acumulado(self.get_costo_acumulado() + 1)

        # hijos.append(hijo)

        return hijos
