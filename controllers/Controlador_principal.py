# [Controlador_principal.py]

import os
from PyQt5 import QtWidgets, QtGui
from views.Vista_principal import Ui_MainWindow
from models.Modelo_principal import Modelo_principal
from views.Sm_dialog_clean import Ui_Dialog as sm_dialog_clean
from models.shared.tools.Temporizador import Temporizador

debug = True


def print_debug(message):
    new_message = "Controlador_principal.py: " + message
    if debug:
        print(new_message)


class Controlador_principal:
    # Funcion para inicializar (general)
    def cargar(self, main_window):
        self.modelo = Modelo_principal()
        self.MainWindow = main_window
        self.minSizeHint = self.MainWindow.minimumSizeHint()
        self.maxSizeHint = self.MainWindow.minimumSizeHint()
        self.restart_window_size()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.cargar_imagenes()

        # Configuracion del modelo
        self.modelo.select_busqueda_no_informada()
        self.ui.box_tipo_busqueda.setCurrentIndex(0)
        self.cargar_algoritmos()

        # Listeners específicos
        self.ui.box_tipo_busqueda.currentIndexChanged.connect(
            self.cambiar_tipo_busqueda)
        self.ui.box_algoritmo.currentIndexChanged.connect(
            self.cambiar_algoritmo)
        self.ui.btn_cargar_mundo.clicked.connect(self.cargar_mundo)
        self.ui.btn_iniciar.clicked.connect(self.iniciar)
        self.ui.btn_sobre.clicked.connect(self.mostrar_sobre_nosotros)

    def block_window_size(self):
        self.MainWindow.setFixedSize(self.MainWindow.size())

    def restart_window_size(self):
        self.MainWindow.setMinimumSize(self.minSizeHint)
        self.MainWindow.setMaximumSize(self.maxSizeHint)

    def cargar_imagenes(self):
        image_path = os.path.abspath(
            "./views/assets/gui/sidebar_image.png")
        self.ui.lbl_side_image.setPixmap(QtGui.QPixmap(image_path))

    def mostrar(self, main_window):
        self.cargar(main_window)
        self.MainWindow.show()

    def block_focus(self):
        """
        Funcion intuitiva para mostrar que la ventana principal NO es la que esta recibiendo eventos, ayuda a mostrar que el flujo de trabajo esta ocurriendo en otra ventana.
        """
        self.MainWindow.setEnabled(False)
        self.ui.centralwidget.setEnabled(False)
        self.ui.centralwidget.setVisible(False)
        self.block_window_size()

    def little_block_focus(self):
        """
        Funcion intuitiva para mostrar que la ventana principal esta procesando sin embargo el flujo de trabajo esta actualmente en ella.
        """
        self.MainWindow.setEnabled(False)
        self.ui.centralwidget.setEnabled(False)
        self.block_window_size()

    def unblock_focus(self):
        """
        Funcion intuitiva para revertir block_focus() y little_block_focus(), muestra que el flujo de trabajo esta ocurriendo en la ventana principal y habilita los eventos.
        """
        self.restart_window_size()
        self.MainWindow.setEnabled(True)
        self.ui.centralwidget.setEnabled(True)
        self.ui.centralwidget.setVisible(True)

    def mostrar_dialogo(self, titulo, mensaje):
        self.block_focus()
        Temporizador.iniciar(1)

        new_dialog = QtWidgets.QDialog()
        new_ui = sm_dialog_clean()
        new_ui.setupUi(new_dialog)
        new_dialog.setModal(True)
        new_dialog.show()
        new_ui.lbl_title.setText(titulo)
        new_ui.lbl_body.setText(mensaje)

        new_dialog.exec()

        self.unblock_focus()

    def cambiar_tipo_busqueda(self):
        indice_actual = self.ui.box_tipo_busqueda.currentIndex()
        if indice_actual == 0:
            self.modelo.select_busqueda_no_informada()
        elif indice_actual == 1:
            self.modelo.select_busqueda_informada()
        else:
            print_debug("Hay algo raro aqui, el indice es {}".format(
                str(indice_actual)))

        self.cargar_algoritmos()

    def cargar_algoritmos(self):
        algoritmos = self.modelo.get_algoritmos_disponibles()
        self.ui.box_algoritmo.clear()

        for algoritmo in algoritmos:
            nombre = algoritmo.capitalize()

            if self.modelo.get_tipo_busqueda() == "no-informada":
                nombre = "Busqueda preferente por " + nombre
            self.ui.box_algoritmo.addItem(nombre)

        self.ui.box_algoritmo.setCurrentIndex(0)

    def cambiar_algoritmo(self):
        tipo_busqueda = self.modelo.get_tipo_busqueda()
        indice_actual = self.ui.box_algoritmo.currentIndex()

        if tipo_busqueda == "informada":
            if indice_actual == 0:
                self.modelo.select_algoritmo_avara()
            elif indice_actual == 1:
                self.modelo.select_algoritmo_a_ast()
        elif tipo_busqueda == "no-informada":
            if indice_actual == 0:
                self.modelo.select_algoritmo_amplitud()
            elif indice_actual == 1:
                self.modelo.select_algoritmo_costo()
            elif indice_actual == 2:
                self.modelo.select_algoritmo_profundidad()

    def iniciar(self):
        if self.modelo.get_mundo() != None:
            print_debug("Se procede a iniciar")
            return None

        print_debug("El mundo esta vacio, cargue un mundo")

    def cargar_mundo(self):
        errores = self.modelo.cargar_mundo()
        titulo = ""
        mensaje = ""

        if errores == None:
            titulo = "Operacion exitosa"
            mensaje = "El archivo seleccionado es un mundo válido para probar el algoritmo."
        else:
            titulo = "Operacion fallida"
            mensaje = "El archivo seleccionado NO es un mundo válido por las siguientes razones:\n\n"
            for error in errores:
                mensaje += "* " + error + "\n"

        self.mostrar_dialogo(titulo, mensaje)

    def mostrar_sobre_nosotros(self):
        from controllers.Controlador_sobre_nosotros import controlador_sobre_nosotros
        self.controlador_sobre_nosotros = controlador_sobre_nosotros()
        self.controlador_sobre_nosotros.mostrar(self.MainWindow)
