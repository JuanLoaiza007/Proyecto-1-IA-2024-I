# [Agente.py]

from models.Estructuras_datos import Problema
from models.tools.World_tools import World_tools as wtools

debug = False


def print_debug(message):
    new_message = "Agente.py: " + message
    if debug:
        print(new_message)


class Agente():
    def __init__(self, coordenadas):
        self.coordenadas = coordenadas
        self.pasos = []
        self.resultado = "Estoy perdido"

        self.env_objects_dic = wtools.reconocer_objetos()

    # Coordenadas del agente
    def set_coordenadas(self, coordenadas):
        self.coordenadas = coordenadas
        self.pasos.append(self.coordenadas)

    def get_coordenadas(self):
        return self.coordenadas

    def get_x(self):
        return self.coordenadas[0]

    def get_y(self):
        return self.coordenadas[1]

    def tomar_decision(self, operadores_validos):
        """
        A traves de sus criterios escoge un operador entre los posibles.

        Args:
            operadores_validos ([Operador, Operador,.... Operador]): Una lista de operadores aplicables.

        Returns:
            operador (Operador): El operador que escoge el Agente dados los posibles
            None: Si no puede escoger entre los operadores disponibles.
        """
        for operador in operadores_validos:
            if operador.get_nombre() == "arriba":
                return operador
            elif operador.get_nombre() == "derecha":
                return operador
        return None

    def iniciar_viaje(self, estado_inicial, estado_objetivo, ambiente):
        """
        A traves de su proceso interno escoge el camino a seguir.

        Args:
            estado_inicial (Estado): El estado inicial o actual del problema.
            estado_objetivo (Estado): El objetivo deseado del problema.
            ambiente ([[], [],... []]]): Una matriz que representa al ambiente, 
            debe haberse eliminado al Agente

        Returns:
            pasos ([(int, int), (int, int),... (int, int)]): Las coordendas que pasó.
            resultado (str): Un informe sobre el estado final del problema (Que pasó con el agente?)
        """
        estado_actual = estado_inicial
        nuevo_estado = None

        while True:
            problema = Problema(
                estado_actual, estado_objetivo, ambiente)

            print_debug("Coordenadas estado_actual: {}".format(
                str(estado_actual.get_coordenadas())))
            if debug:
                wtools.imprimir_juego(
                    self.env_objects_dic, ambiente, self.get_coordenadas(), estado_objetivo.get_coordenadas())

            if (problema.es_objetivo(estado_actual)):
                self.resultado = "Lo logré"
                break

            operadores_validas = problema.generar_operadores()

            if len(operadores_validas) == 0:
                self.resultado = "Estoy perdido"
                break

            print_debug("operadores válidas desde el estado actual: {}".format(str([
                operador.nombre for operador in operadores_validas])))

            operador = self.tomar_decision(operadores_validas)
            if operador == None:
                self.resultado = "No se que hacer en esta situacion :("
                break

            print_debug("El agente decidió: {}".format(
                str(operador.get_nombre())))

            nuevo_estado = problema.resultado(estado_actual, operador)
            self.set_coordenadas(nuevo_estado.get_coordenadas())

            print_debug("Las coordenadas del agente son: {}".format(
                str(self.get_coordenadas())))

            estado_actual = nuevo_estado
            nuevo_estado = None

        return self.pasos, self.resultado
