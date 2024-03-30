# [Modelo_juego.py]

import os
from models.trees.Amplitud import *
from models.trees.Profundidad import *
from models.shared.Estructuras_datos import Estado
from models.shared.tools.World_tools import World_tools as wtools

debug = True


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
        self.reporte = None
        self.problema_inicial = None
        self.algoritmo_actual = None
        self.algoritmos_disponibles = [
            "amplitud", "costo", "profundidad", "avara", "a*"]

        self.assets_dic = wtools.reconocer_assets()
        self.env_objects_dic = wtools.reconocer_objetos()

        # Personajes
        self.vacio = os.path.abspath(self.assets_dic['vacio'])
        self.pared = os.path.abspath(self.assets_dic['pared'])
        self.mando = os.path.abspath(self.assets_dic['agente'])
        self.nave = os.path.abspath(self.assets_dic['nave'])
        self.enemigo = os.path.abspath(self.assets_dic['enemigo'])
        self.grogu = os.path.abspath(self.assets_dic['meta'])

    def cargar_ambiente(self, ambiente):
        self.ambiente = ambiente

    def cargar_algorimo(self, algoritmo):
        if algoritmo in self.algoritmos_disponibles:
            self.algoritmo_actual = algoritmo
            return True
        return False

    def preparar_juego(self):
        # Inicializar estado inicial y estado objetivo
        x_ini, y_ini = wtools.determinar_posicion(
            self.ambiente, self.env_objects_dic['agente'])
        x_meta, y_meta = wtools.determinar_posicion(
            self.ambiente, self.env_objects_dic['meta'])

        self.estado_inicial = Estado(x_ini, y_ini)
        self.estado_objetivo = Estado(x_meta, y_meta)

        # Eliminar el self.estado_inicial del ambiente
        self.ambiente[x_ini][y_ini] = "0"

        self.problema_inicial = Problema(self.estado_inicial,
                                         self.estado_objetivo, self.ambiente)

    def iniciar_juego(self):

        if self.algoritmo_actual == "profundidad":
            self.camino, self.resultado, self.reporte = Profundidad.busqueda_preferente_por_profundidad(
                self.problema_inicial)
            print_debug("He decidido usar el algoritmo profundidad")
        else:
            self.camino, self.resultado, self.reporte = Amplitud.busqueda_preferente_por_amplitud(
                self.problema_inicial)
            print_debug(
                "ATENCION: Por DEFAULT he decidido usar el algoritmo amplitud")

        print_debug("Camino es {}\nResultado es {}\n".format(
            str(self.camino), str(self.resultado)))
