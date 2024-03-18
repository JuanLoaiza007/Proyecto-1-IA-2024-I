# controlador_principal.py

import os
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QStandardItemModel, QPixmap
from views.vista_juego import Ui_MainWindow
from models.modelo_juego import modelo_juego
from views.sm_dialog_clean import Ui_Dialog as sm_dialog_clean


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

    def mostrar(self, main_window):
        self.cargar(main_window)
        self.MainWindow.show()
        self.modelo.iniciar_juego()

    def block_focus(self, window):
        self.MainWindow.setEnabled(False)
        self.MainWindow.setFixedSize(window.size())

    def unblock_focus(self):
        self.MainWindow.setMinimumSize(self.MainWindow.minimumSizeHint())
        self.MainWindow.setMaximumSize(16777215, 16777215)
        self.MainWindow.setEnabled(True)
