# [Controlador_juego.py]

import os
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon
from views.Vista_juego import Ui_MainWindow
from models.Modelo_juego import Modelo_juego
from models.shared.tools.Temporizador import Temporizador
from models.shared.tools.Dialog import Dialog
from PyQt5.QtCore import QThread

debug = True


def print_debug(message):
    new_message = "controlador_juego.py: " + message
    if debug:
        print(new_message)


class WorkerThread(QThread):
    """
    Clase de Hilo Trabajador para ejecutar procesamiento en segundo plano y conservar la ventana recibiendo eventos.
    """

    def __init__(self, modelo: Modelo_juego):

        super().__init__()
        self.modelo = modelo

    def run(self):
        self.modelo.iniciar_juego()


class Controlador_juego:
    # Funcion para inicializar (general)
    def cargar(self, main_window):
        self.modelo = Modelo_juego()
        self.MainWindow = main_window
        self.MainWindow.setMinimumSize(self.MainWindow.minimumSizeHint())
        self.MainWindow.setMaximumSize(16777215, 16777215)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.inicializar_tabla()

        # Hilo de procesamiento
        self.hilo_procesamiento: WorkerThread = None

        # Evento para cierre de programa
        self.MainWindow.destroyed.connect(self.cerrar_ventana)

    def cerrar_ventana(self):
        self.hilo_procesamiento.exit()
        os._exit(0)

    def inicializar_tabla(self):
        self.ui.table_mapa.setRowCount(10)
        self.ui.table_mapa.setColumnCount(10)
        self.ui.table_mapa.verticalHeader().setVisible(False)
        self.ui.table_mapa.horizontalHeader().setVisible(False)
        self.ui.table_mapa.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch)
        self.ui.table_mapa.verticalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch)

    def actualizar_tabla(self, ambiente, coordenadas_agente, coordenadas_meta):
        for i, fila in enumerate(ambiente):
            for j, elemento in enumerate(fila):

                item = QtWidgets.QTableWidgetItem()
                icon = None
                pixmap = None

                if [i, j] == coordenadas_agente:
                    pixmap = QPixmap(self.modelo.mando)
                elif [i, j] == coordenadas_meta:
                    pixmap = QPixmap(self.modelo.grogu)
                else:
                    if elemento == self.modelo.env_objects_dic['vacio']:
                        pixmap = QPixmap(self.modelo.vacio)
                    elif elemento == self.modelo.env_objects_dic['pared']:
                        pixmap = QPixmap(self.modelo.pared)
                    elif elemento == self.modelo.env_objects_dic['enemigo']:
                        pixmap = QPixmap(self.modelo.enemigo)
                    elif elemento == self.modelo.env_objects_dic['nave']:
                        pixmap = QPixmap(self.modelo.nave)
                    else:
                        print_debug(
                            "actualizar_tabla ha omitido cargar el elemento {}".format(str(elemento)))

                icon = QIcon(pixmap)
                item.setData(Qt.DecorationRole, icon)
                icon_size = 45
                self.ui.table_mapa.setIconSize(QSize(icon_size, icon_size))
                self.ui.table_mapa.setItem(i, j, item)

    def mostrar(self, main_window):
        self.cargar(main_window)
        self.MainWindow.show()
        Temporizador.iniciar(1)
        self.iniciar_juego()

    def block_focus(self, window):
        self.MainWindow.setEnabled(False)
        self.MainWindow.setFixedSize(window.size())

    def unblock_focus(self):
        self.MainWindow.setMinimumSize(self.MainWindow.minimumSizeHint())
        self.MainWindow.setMaximumSize(16777215, 16777215)
        self.MainWindow.setEnabled(True)

    def iniciar_juego(self):
        Temporizador.iniciar(100)
        self.modelo.preparar_juego()
        ambiente = self.modelo.ambiente
        e_inicial = self.modelo.estado_inicial.get_coordenadas()
        e_objetivo = self.modelo.estado_objetivo.get_coordenadas()
        self.actualizar_tabla(ambiente, e_inicial, e_objetivo)
        self.ui.lbl_estado_agente.setText(
            "Mando esta pensando... *guiño guiño*")

        Temporizador.iniciar(100)
        # Hilo para mantener la interfaz atenta
        self.hilo_procesamiento = WorkerThread(self.modelo)
        # Eventos que requieren los calculos del hilo
        self.hilo_procesamiento.finished.connect(
            self.animar_juego)
        # Inicia las tareas del hilo de la funcion run()
        self.hilo_procesamiento.start()

    def animar_juego(self):
        self.ui.lbl_estado_agente.setText(
            "Mando ha tomado una decision")

        for paso in self.modelo.camino:
            Temporizador.iniciar(600)
            self.actualizar_tabla(
                self.modelo.ambiente, paso, self.modelo.estado_objetivo.get_coordenadas())

        Temporizador.iniciar(100)
        Dialog.mostrar(self.modelo.resultado)
