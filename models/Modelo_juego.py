# [Modelo_juego.py]

import os
from models.Estructuras_datos import Estado
from models.Agente import Agente as Agente
from models.tools.World_tools import World_tools as wtools
from models.tools.File_selector import File_selector

debug = False


def print_debug(message):
    new_message = "modelo_juego.py: " + message
    if debug:
        print(new_message)


class Modelo_juego:
    def __init__(self):
        self.camino = None
        self.ambiente = None
        self.estado_inicial = None
        self.estado_objetivo = None
        self.resultado = None

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

        self.estado_inicial = Estado(x_ini, y_ini)
        self.estado_objetivo = Estado(x_meta, y_meta)

        # Inicializar el agente
        mando = Agente([x_ini, y_ini])

        # Eliminar el self.estado_inicial del ambiente
        self.ambiente[x_ini][y_ini] = "0"

        # Iniciar el viaje del Agente/Arbol y obtener los resultados
        self.camino, self.resultado = mando.iniciar_viaje(
            self.estado_inicial, self.estado_objetivo, self.ambiente)
