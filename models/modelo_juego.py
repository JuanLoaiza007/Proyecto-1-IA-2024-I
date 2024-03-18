import os
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer, QEventLoop
from PyQt5.QtGui import QPixmap, QIcon
from models.agente_reflejo_simple import agente_reflejo_simple as agente
from models.world_tools import world_tools
from views.sm_dialog_clean import Ui_Dialog as sm_dialog_clean


class modelo_juego:
    def __init__(self):
        self.tabla_juego = None

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
                    else:
                        print(
                            "modelo_juego.py: actualizar_tabla ha omitido cargar el elemento ", elemento)

                icon = QIcon(pixmap)
                item.setIcon(icon)
                self.tabla_juego.setItem(i, j, item)

    def temporizador(self, tiempo_segundos):
        loop = QEventLoop()
        timer = QTimer()
        timer.setSingleShot(True)
        timer.timeout.connect(lambda: loop.quit())
        tiempo_ms = tiempo_segundos * 1000
        timer.start(tiempo_ms)
        loop.exec_()

    def exito(self):
        new_dialog = QtWidgets.QDialog()
        new_ui = sm_dialog_clean()
        new_ui.setupUi(new_dialog)
        new_dialog.setModal(True)
        new_dialog.show()

        saludo = "Encontré a Grogu!"
        new_ui.lbl_main_text.setText(saludo)

        new_dialog.exec()

    def iniciar_juego(self):
        # Mapa
        nombre_mundo = "world.txt"
        juego_activo = True

        ambiente = world_tools.generar_mundo(nombre_mundo)

        mando = agente()
        mando.set_coordenadas(world_tools.determinar_posicion(
            ambiente, self.env_objects_dic['agente']))
        mando.set_ambiente(ambiente, self.env_objects_dic)
        mando.set_meta(world_tools.determinar_posicion(
            ambiente, self.env_objects_dic['meta']))

        ambiente[mando.coordenadas[0]][mando.coordenadas[1]] = 0

        self.actualizar_tabla(ambiente,
                              mando.get_coordenadas(), mando.get_meta())

        self.temporizador(2)

        while juego_activo:

            juego_activo = not (mando.meta_alcanzada())

            self.actualizar_tabla(
                ambiente, mando.get_coordenadas(), mando.get_meta())

            juego_activo = mando.tomar_decision()

            self.temporizador(1.3)

        self.exito()
