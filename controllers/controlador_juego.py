# controlador_principal.py

import os
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QStandardItemModel, QPixmap, QIcon
from views.vista_juego import Ui_MainWindow
from models.modelo_juego import modelo_juego
from views.sm_dialog_clean import Ui_Dialog as sm_dialog_clean
from models.tools.temporizador import Temporizador
from models.tools.dialog import Dialog


class controlador_juego:
    # Funcion para inicializar (general)
    def cargar(self, main_window):
        self.modelo = modelo_juego()
        self.MainWindow = main_window
        self.MainWindow.setMinimumSize(self.MainWindow.minimumSizeHint())
        self.MainWindow.setMaximumSize(16777215, 16777215)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.inicializar_tabla()

    def inicializar_tabla(self):
        self.ui.table_mapa.setRowCount(10)
        self.ui.table_mapa.setColumnCount(10)
        self.ui.table_mapa.verticalHeader().setVisible(False)
        self.ui.table_mapa.horizontalHeader().setVisible(False)

        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        self.ui.table_mapa.setSizePolicy(size_policy)
        self.ui.table_mapa.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch)
        self.ui.table_mapa.verticalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch)

        self.ui.table_mapa.horizontalHeader().setSectionResizeMode(
            0, QtWidgets.QHeaderView.Stretch)
        self.ui.table_mapa.verticalHeader().setSectionResizeMode(
            0, QtWidgets.QHeaderView.Stretch)

        self.modelo.setTabla(self.ui.table_mapa)

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
                        if self.debug:
                            print(
                                "modelo_juego.py: actualizar_tabla ha omitido cargar el elemento ", elemento)

                icon = QIcon(pixmap)
                item.setData(Qt.DecorationRole, icon)
                icon_size = 45
                self.ui.table_mapa.setIconSize(QSize(icon_size, icon_size))
                self.ui.table_mapa.setItem(i, j, item)

    def mostrar(self, main_window):
        self.cargar(main_window)
        self.MainWindow.show()
        Temporizador.iniciar(0.1)
        self.iniciar_juego()

    def block_focus(self, window):
        self.MainWindow.setEnabled(False)
        self.MainWindow.setFixedSize(window.size())

    def unblock_focus(self):
        self.MainWindow.setMinimumSize(self.MainWindow.minimumSizeHint())
        self.MainWindow.setMaximumSize(16777215, 16777215)
        self.MainWindow.setEnabled(True)

    def iniciar_juego(self):
        self.modelo.iniciar_juego()
        self.animar_juego()

    def animar_juego(self):
        for paso in self.modelo.camino:
            Temporizador.iniciar(1.5)
            self.actualizar_tabla(
                self.modelo.ambiente, paso, self.modelo.estado_objetivo.get_coordenadas())

        Dialog.mostrar(self.modelo.resultado)
