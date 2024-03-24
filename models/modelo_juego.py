# [modelo_juego.py]

import os
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QSize
from models.estructura_datos import Accion, Celda, Estado, Problema
from models.agente_reflejo_simple import agente_reflejo_simple as Agente
from models.tools.world_tools import world_tools as wtools
from models.tools.temporizador import Temporizador
from models.tools.file_selector import File_selector
from models.tools.dialog import Dialog

debug = False


def print_debug(message):
    new_message = "modelo_juego.py: " + message
    if debug:
        print(new_message)


class modelo_juego:
    def __init__(self):
        self.tabla_juego = None
        self.debug = False

        self.assets_dic = wtools.reconocer_assets()
        self.env_objects_dic = wtools.reconocer_objetos()

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
                icon_size = 45
                self.tabla_juego.setIconSize(QSize(icon_size, icon_size))
                self.tabla_juego.setItem(i, j, item)

    def iniciar_juego(self):

        # Cargar archivo de mundo
        file_selector = File_selector()
        archivo = file_selector.select("data/worlds")

        # Generar mundo
        ambiente = wtools.generar_mundo(archivo)

        # Inicializar estado inicial y estado objetivo
        x_ini, y_ini = wtools.determinar_posicion(
            ambiente, self.env_objects_dic['agente'])
        x_meta, y_meta = wtools.determinar_posicion(
            ambiente, self.env_objects_dic['meta'])

        mando = Agente([x_ini, y_ini])
        estado_inicial = Estado(mando.get_x(), mando.get_y())
        estado_objetivo = Estado(x_meta, y_meta)

        # Eliminar el estado_inicial del ambiente
        print_debug("x_ini: {}, y_ini: {}".format(str(x_ini), str(y_ini)))
        ambiente[x_ini][y_ini] = "0"

        estado_actual = estado_inicial
        nuevo_estado = None
        resultado = "Estoy perdido"

        self.actualizar_tabla(
            ambiente, mando.get_coordenadas(), estado_objetivo.get_coordenadas())

        while True:
            problema = Problema(estado_actual, estado_objetivo, ambiente)
            print_debug("Coordenadas estado_actual: {}".format(
                str(estado_actual.get_coordenadas())))
            if (problema.es_objetivo(estado_actual)):
                resultado = "Lo logré"
                break

            acciones_validas = problema.generar_acciones(estado_actual)
            if len(acciones_validas) == 0:
                resultado = "Estoy perdido"
                break
            print_debug("Acciones válidas desde el estado actual: {}".format(str([
                accion.nombre for accion in acciones_validas])))

            accion = mando.tomar_decision(acciones_validas)
            if accion == None:
                resultado = "No se que hacer en esta situacion :("
                break
            print_debug("El agente decidió: {}".format(
                str(accion.get_nombre())))

            nuevo_estado = problema.resultado(estado_actual, accion)
            mando.set_coordenadas(nuevo_estado.get_coordenadas())
            print_debug("Las coordenadas del agente son: {}".format(
                str(mando.get_coordenadas())))

            estado_actual = nuevo_estado
            nuevo_estado = None

        camino = mando.get_pasos()

        for paso in camino:
            Temporizador.iniciar(1.5)
            self.actualizar_tabla(
                ambiente, paso, estado_objetivo.get_coordenadas())

        Dialog.mostrar(resultado)
