# [Estructura_datos.py]
from queue import Queue


class Operador:
    def __init__(self, nombre: str, dx: int, dy: int) -> None:
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

    def get_nombre(self) -> str:
        return self.nombre

    def get_dx(self) -> int:
        return self.dx

    def get_dy(self) -> int:
        return self.dy

    def __str__(self) -> str:
        return self.nombre


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

    def __str__(self) -> str:
        """
        Muestra informacion sobre las coordenadas.

        Args:
            None

        Returns:
            Las coordenadas en string.
        """
        return f"({self.x}, {self.y})"


class Problema:
    def __init__(self, estado_inicial: Estado, estado_objetivo: Estado, matriz):
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

    def __str__(self) -> str:
        mensaje = "Estado inicial: {} -> Estado objetivo: {1}".format(
            self.estado_inicial, self.estado_objetivo)
        return mensaje

    def get_estado_inicial(self) -> Estado:
        return self.estado_inicial

    def get_estado_objetivo(self) -> Estado:
        return self.estado_objetivo

    def get_matriz(self):
        return self.matriz

    def es_estado_valido(self, estado: Estado) -> bool:
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

    def es_estado_objetivo(self) -> bool:
        """
        Determina si un estado es el estado deseado/objetivo.

        Args:
            Ninguno.

        Returns:
            True, si el estado es el objetivo.
            False, si el estado no es el objetivo
        """
        return self.estado_inicial.get_coordenadas() == self.estado_objetivo.get_coordenadas()

    def generar_operadores(self) -> "list[Operador]":
        """
        Genera las operadores validas para el estado.

        Args:
            estado (Estado): El estado del que se quiere generar operadores

        Returns:
            operadores ([Operador, Operador,... Operador]): Un vector de operadores.
        """
        operadores = []
        estado = self.estado_inicial
        # OJO: Aquí hay una corrección para los indices de la matriz,
        # arriba es (0, -1) y así sucesivamente.
        for dy, dx, operador_nombre in [(0, -1, 'arriba'), (0, 1, 'abajo'), (-1, 0, 'izquierda'), (1, 0, 'derecha')]:
            nuevo_estado = Estado(estado.x + dx, estado.y + dy)
            if self.es_estado_valido(nuevo_estado):
                operadores.append(Operador(operador_nombre, dx, dy))
        return operadores

    def resultado(self, estado: Estado, operador: Operador) -> Estado:
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
        if self.es_estado_valido(nuevo_estado):
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

    def __init__(self, problema: Problema):
        """
        Inicializa un nuevo nodo raiz.

        Args:
            problema (Problema): El problema

        Atributos internos (get):
        - estado: El estado del problema.
        - padre: Una referencia al nodo padre.
        - operador: El operador que se aplicó para generar el nodo.
        - profundidad: La profundidad del nodo en el árbol.
        - costo_acumulado: El costo acumulado de la ruta desde la raíz hasta el nodo.
        """
        self.problema: Problema = problema
        self.padre: Nodo = None
        self.operador: Operador = None
        self.profundidad: int = 0
        self.costo_acumulado: int = 0

    def __str__(self) -> str:
        padre = None
        if self.padre != None:
            padre = self.padre.get_estado()
        mensaje = "Estado: {}, padre: {}, operador efectuado: {}, profundidad: {}, costo acumulado: {}".format(
            str(self.problema.get_estado_inicial()), str(padre), str(self.operador), str(self.profundidad), str(self.costo_acumulado))
        return mensaje

    def get_problema(self):
        return self.problema

    def set_problema(self, problema: Problema):
        self.problema = problema

    def get_estado(self):
        return self.problema.estado_inicial

    def get_padre(self):
        return self.padre

    def set_padre(self, padre: "Nodo"):
        self.padre = padre

    def get_operador(self):
        return self.operador

    def set_operador(self, operador: Operador):
        self.operador = operador

    def get_profundidad(self):
        return self.profundidad

    def set_profundidad(self, profundidad: int):
        self.profundidad = profundidad

    def get_costo_acumulado(self):
        return self.costo_acumulado

    def set_costo_acumulado(self, costo_acumulado: int):
        self.costo_acumulado = costo_acumulado

    def es_meta(self) -> bool:
        return self.problema.es_estado_objetivo()

    def expandir(self):
        """
        Expande el nodo actual

        Args:
            Ninguno.

        Returns:
            list[Nodo]: Donde list[Nodo] corresponde a los hijos.
        """
        # Limpiar hijos por si las moscas
        self.hijos = []

        operadores = self.problema.generar_operadores()

        if len(operadores) == 0:
            return self.hijos

        for operador in operadores:
            nuevo_estado = self.problema.resultado(
                self.problema.estado_inicial, operador)

            nuevo_problema = Problema(
                nuevo_estado, self.problema.get_estado_objetivo(), self.problema.get_matriz())

            if nuevo_estado != None:
                hijo = Nodo(nuevo_problema)
                hijo.set_padre(self)
                hijo.set_operador(operador)
                hijo.set_profundidad(self.profundidad + 1)
                hijo.set_costo_acumulado(self.costo_acumulado + 1)

                self.hijos.append(hijo)

        return self.hijos


class Test():
    @staticmethod
    def start():
        from models.shared.tools.World_tools import World_tools as wtools
        from models.shared.tools.File_selector import File_selector

        env_objects_dic = wtools.reconocer_objetos()

        # Cargar archivo de mundo
        file_selector = File_selector()
        archivo = file_selector.select("data/worlds")

        ambiente = wtools.generar_mundo(archivo)

        # Inicializar estado inicial y estado objetivo
        x_ini, y_ini = wtools.determinar_posicion(
            ambiente, env_objects_dic['agente'])
        x_meta, y_meta = wtools.determinar_posicion(
            ambiente, env_objects_dic['meta'])

        # Inicializar estados
        estado_inicial = Estado(x_ini, y_ini)
        estado_objetivo = Estado(x_meta, y_meta)

        # Eliminar el self.estado_inicial del ambiente
        ambiente[x_ini][y_ini] = "0"

        problema = Problema(estado_inicial, estado_objetivo, ambiente)

        # Creando Nodo Padre
        nodo = Nodo(problema)
        print("Nodo padre:\n{}\n".format(nodo))

        # Creando nodos hijos
        print("Hijos:\n")
        hijos = nodo.expandir()
        if len(hijos) == 0:
            print("Este nodo no tiene hijos...")
        else:
            for hijo in hijos:
                print(hijo)

        if len(hijos) != 0:

            hijo_favorito = hijos[0]
            print("El hijo favorito es:\n{}\n".format(str(hijo_favorito)))

            nietos = hijo_favorito.expandir()

            nieto_favorito = nietos[1]

            print("Sus nieto favorito es:\n{}".format(str(nieto_favorito)))

            if str(nieto_favorito.get_estado()) == str(hijo.get_padre().get_estado()):
                print("El nieto:\n{}\nes igual al padre:\n{}\n".format(
                    str(nieto_favorito), str(hijo.get_padre())))
