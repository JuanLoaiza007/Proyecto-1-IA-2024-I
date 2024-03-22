# [modelo_juego.py]

import os
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QSize
from models.agente_reflejo_simple import agente_reflejo_simple as agente
from models.tools.world_tools import world_tools
from models.tools.temporizador import Temporizador
from models.tools.file_selector import File_selector
from models.tools.dialog import Dialog


class modelo_juego:
    def __init__(self):
        self.tabla_juego = None
        self.debug = False

        self.assets_dic = world_tools.reconocer_assets()
        self.env_objects_dic = world_tools.reconocer_objetos()

        # Personajes
        self.vacio = os.path.abspath(self.assets_dic['vacio'])
        self.pared = os.path.abspath(self.assets_dic['pared'])
        self.mando = os.path.abspath(self.assets_dic['agente'])
        self.nave = os.path.abspath(self.assets_dic['nave'])
        self.enemigo = os.path.abspath(self.assets_dic['enemigo'])
        self.grogu = os.path.abspath(self.assets_dic['meta'])

    def setTabla(self, tabla,):
        self.tabla_juego = tabla

    def actualizar_tabla(self, ambiente, coordenadas_agente, coordenadas_meta):
        for i, fila in enumerate(ambiente):
            for j, elemento in enumerate(fila):

                item = QtWidgets.QTableWidgetItem()
                icon = None
                pixmap = None

                if [i, j] == coordenadas_agente:
                    pixmap = QPixmap(self.mando)
                elif [i, j] == coordenadas_meta:
                    pixmap = QPixmap(self.grogu)
                else:
                    if elemento == self.env_objects_dic['vacio']:
                        pixmap = QPixmap(self.vacio)
                    elif elemento == self.env_objects_dic['pared']:
                        pixmap = QPixmap(self.pared)
                    elif elemento == self.env_objects_dic['enemigo']:
                        pixmap = QPixmap(self.enemigo)
                    elif elemento == self.env_objects_dic['nave']:
                        pixmap = QPixmap(self.nave)
                    else:
                        if self.debug:
                            print(
                                "modelo_juego.py: actualizar_tabla ha omitido cargar el elemento ", elemento)

                icon = QIcon(pixmap)
                item.setData(Qt.DecorationRole, icon)
                self.tabla_juego.setIconSize(QSize(38, 38))
                self.tabla_juego.setItem(i, j, item)

    def iniciar_juego(self):

        # Cargar archivo de mundo
        file_selector = File_selector()
        archivo = file_selector.select("data/worlds")

        # Generar mundo
        ambiente = world_tools.generar_mundo(archivo)

        # Creacion de agente / arbol de busqueda
        # El agente/arbol debe recibir:
        # * Las coordenadas iniciales
        # * El ambiente o mapa (matriz)
        # * Las coordenadas de la meta
        mando = agente()
        mando.set_coordenadas(world_tools.determinar_posicion(
            ambiente, self.env_objects_dic['agente']))
        mando.set_ambiente(ambiente, self.env_objects_dic)
        mando.set_meta(world_tools.determinar_posicion(
            ambiente, self.env_objects_dic['meta']))

        # Limpiar ambiente para mostrar en pantalla
        ambiente[mando.coordenadas[0]][mando.coordenadas[1]] = 0
        self.actualizar_tabla(ambiente,
                              mando.get_coordenadas(), mando.get_meta())

        # Iniciar viaje del agente / arbol de busqueda
        # La funcion iniciar_viaje se usa para la animacion, debe retornar:
        # * camino: Una lista de coordenadas que representa los pasos que tomó
        # * resultado: Un mensaje que indique en que concluyó el camino
        camino, resultado = mando.iniciar_viaje()

        # Animacion del camino
        for paso in camino:

            Temporizador.iniciar(2)
            self.actualizar_tabla(
                ambiente, paso, mando.get_meta())

        Dialog.mostrar(resultado)
