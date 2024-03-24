# [estructura_datos.py]

from agente_reflejo_simple import agente_reflejo_simple as Agente
from tools.file_selector import File_selector
from tools.world_tools import world_tools as wtools


class Accion:
    def __init__(self, nombre, dx, dy):
        """
        Inicializa una accion

        Args:
            nombre (str): El nombre de la accion.
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


class Celda:
    def __init__(self, tipo):
        """
        Inicializa una celda

        Args:
            tipo (str): El tipo de la celda ('pared', 'enemigo', 'nave', 'meta')

        Returns:
            None
        """
        self.tipo = tipo


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
        print("(func) es_objetivo: estado: {} objetivo: {}".format(
            str(estado.get_coordenadas()), str(estado_objetivo.get_coordenadas())))
        return estado.get_coordenadas() == self.estado_objetivo.get_coordenadas()

    def generar_acciones(self, estado):
        """
        Genera las acciones validas para el estado.

        Args:
            estado (Estado): El estado del que se quiere generar acciones

        Returns:
            acciones ([Accion, Accion,... Accion]): Un vector de acciones.
        """
        acciones = []
        # OJO: Aquí hay una corrección para los indices de la matriz,
        # arriba es (0, -1) y así sucesivamente.
        for dy, dx, accion_nombre in [(0, -1, 'arriba'), (0, 1, 'abajo'), (-1, 0, 'izquierda'), (1, 0, 'derecha')]:
            nuevo_estado = Estado(estado.x + dx, estado.y + dy)
            if self.es_valido(nuevo_estado):
                acciones.append(Accion(accion_nombre, dx, dy))
        return acciones

    def resultado(self, estado, accion):
        """
        Genera un nuevo estado aplicando un operador sobre el actual.

        Args:
            estado (Estado): El estado actual.
            accion (Accion): La accion que se quiere aplicar al estado.

        Returns:
            nuevo_estado (Estado): Un nuevo estado que surge de aplicar la accion al estado actual.
            None si el nuevo estado no cumple con las reglas de juego.
        """
        nuevo_estado = Estado(estado.x + accion.dx, estado.y + accion.dy)
        if self.es_valido(nuevo_estado):
            return nuevo_estado
        else:
            return None


if __name__ == '__main__':
    # Reconocer los objetos del entorno
    env_objects_dic = wtools.reconocer_objetos()

    # Cargar archivo de mundo
    file_selector = File_selector()
    archivo = file_selector.select("data/worlds")

    # Generar mundo
    ambiente = wtools.generar_mundo(archivo)

    # Inicializar estado inicial y estado objetivo
    x_ini, y_ini = wtools.determinar_posicion(
        ambiente, env_objects_dic['agente'])
    x_meta, y_meta = wtools.determinar_posicion(
        ambiente, env_objects_dic['meta'])

    mando = Agente([x_ini, y_ini])
    estado_inicial = Estado(mando.get_x(), mando.get_y())
    estado_objetivo = Estado(x_meta, y_meta)

    # Eliminar el estado_inicial del ambiente
    print("x_ini: {}, y_ini: {}".format(str(x_ini), str(y_ini)))
    ambiente[x_ini][y_ini] = "0"

    estado_actual = estado_inicial
    nuevo_estado = None

    while True:
        problema = Problema(estado_actual, estado_objetivo, ambiente)
        print("Coordenadas estado_actual: {}".format(
            str(estado_actual.get_coordenadas())))
        wtools.imprimir_juego(env_objects_dic, ambiente,
                              [mando.get_x(), mando.get_y()], [x_meta, y_meta])
        if (problema.es_objetivo(estado_actual)):
            break

        acciones_validas = problema.generar_acciones(estado_actual)
        print("Acciones válidas desde el estado actual:", [
              accion.nombre for accion in acciones_validas])

        accion = mando.tomar_decision(acciones_validas)
        print("El agente decidió: {}".format(str(accion.get_nombre())))

        nuevo_estado = problema.resultado(estado_actual, accion)
        mando.set_coordenadas(nuevo_estado.get_coordenadas())
        print("Las coordenadas del agente son: {}".format(
            str(mando.get_coordenadas())))

        estado_actual = nuevo_estado
        nuevo_estado = None
