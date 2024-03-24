# [modelo_juego.py]

import os
from models.estructura_datos import Operador, Celda, Estado, Problema
from models.agente_reflejo_simple import agente_reflejo_simple as Agente
from models.tools.world_tools import world_tools as wtools
from models.tools.file_selector import File_selector

debug = False


def print_debug(message):
    new_message = "modelo_juego.py: " + message
    if debug:
        print(new_message)


class modelo_juego:
    def __init__(self):
        self.camino = None
        self.ambiente = None
        self.estado_inicial = None
        self.estado_objetivo = None
        self.resultado = "Estoy perdido"

        self.assets_dic = wtools.reconocer_assets()
        self.env_objects_dic = wtools.reconocer_objetos()

        # Personajes
        self.vacio = os.path.abspath(self.assets_dic['vacio'])
        self.pared = os.path.abspath(self.assets_dic['pared'])
        self.mando = os.path.abspath(self.assets_dic['agente'])
        self.nave = os.path.abspath(self.assets_dic['nave'])
        self.enemigo = os.path.abspath(self.assets_dic['enemigo'])
        self.grogu = os.path.abspath(self.assets_dic['meta'])

    def iniciar_juego(self):
        # Cargar archivo de mundo
        file_selector = File_selector()
        archivo = file_selector.select("data/worlds")

        # Generar mundo
        self.ambiente = wtools.generar_mundo(archivo)

        # Inicializar estado inicial y estado objetivo
        x_ini, y_ini = wtools.determinar_posicion(
            self.ambiente, self.env_objects_dic['agente'])
        x_meta, y_meta = wtools.determinar_posicion(
            self.ambiente, self.env_objects_dic['meta'])

        mando = Agente([x_ini, y_ini])
        self.estado_inicial = Estado(mando.get_x(), mando.get_y())
        self.estado_objetivo = Estado(x_meta, y_meta)

        # Eliminar el self.estado_inicial del ambiente
        print_debug("x_ini: {}, y_ini: {}".format(str(x_ini), str(y_ini)))
        self.ambiente[x_ini][y_ini] = "0"

        estado_actual = self.estado_inicial
        nuevo_estado = None

        while True:
            problema = Problema(
                estado_actual, self.estado_objetivo, self.ambiente)

            print_debug("Coordenadas estado_actual: {}".format(
                str(estado_actual.get_coordenadas())))
            if debug:
                wtools.imprimir_juego(
                    self.env_objects_dic, self.ambiente, mando.get_coordenadas(), self.estado_objetivo.get_coordenadas())

            if (problema.es_objetivo(estado_actual)):
                self.resultado = "Lo logré"
                break

            operadores_validas = problema.generar_operadores(estado_actual)

            if len(operadores_validas) == 0:
                self.resultado = "Estoy perdido"
                break

            print_debug("operadores válidas desde el estado actual: {}".format(str([
                operador.nombre for operador in operadores_validas])))

            operador = mando.tomar_decision(operadores_validas)
            if operador == None:
                self.resultado = "No se que hacer en esta situacion :("
                break

            print_debug("El agente decidió: {}".format(
                str(operador.get_nombre())))

            nuevo_estado = problema.resultado(estado_actual, operador)
            mando.set_coordenadas(nuevo_estado.get_coordenadas())

            print_debug("Las coordenadas del agente son: {}".format(
                str(mando.get_coordenadas())))

            estado_actual = nuevo_estado
            nuevo_estado = None

        self.camino = mando.get_pasos()
