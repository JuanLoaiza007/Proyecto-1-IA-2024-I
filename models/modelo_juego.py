import os
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QIcon
from models.agente_reflejo_simple import agente_reflejo_simple as agente
from models.world_tools import world_tools
from models.world_tools import Temporizador
from views.sm_dialog_clean import Ui_Dialog as sm_dialog_clean
from models.file_selector import File_selector


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
                item.setIcon(icon)
                self.tabla_juego.setItem(i, j, item)

    def dialog(self, text):
        new_dialog = QtWidgets.QDialog()
        new_ui = sm_dialog_clean()
        new_ui.setupUi(new_dialog)
        new_ui.lbl_main_text.setText(text)
        new_dialog.setModal(True)
        new_dialog.show()
        new_dialog.exec()

    def iniciar_juego(self):
        # Cargar archivo de mundo
        file_selector = File_selector()
        archivo = file_selector.select()

        # Generar mundo
        ambiente = world_tools.generar_mundo(archivo)

        # Crear agente
        mando = agente()
        mando.set_coordenadas(world_tools.determinar_posicion(
            ambiente, self.env_objects_dic['agente']))
        mando.set_ambiente(ambiente, self.env_objects_dic)
        mando.set_meta(world_tools.determinar_posicion(
            ambiente, self.env_objects_dic['meta']))
        # Limpiar ambiente
        ambiente[mando.coordenadas[0]][mando.coordenadas[1]] = 0

        # Mostrar resultado en pantalla
        self.actualizar_tabla(ambiente,
                              mando.get_coordenadas(), mando.get_meta())

        # Iniciar viaje del agente o el arbol
        # camino: El camino que tomó el agente o el arbol
        # resultado: Un mensaje para decir que pasó
        camino, resultado = mando.iniciar_viaje()

        # Animacion del camino
        for paso in camino:
            Temporizador.iniciar(2)
            self.actualizar_tabla(
                ambiente, paso, mando.get_meta())
        self.dialog(resultado)
