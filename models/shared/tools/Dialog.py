# [Dialog.py]

from views.Sm_dialog_clean import Ui_Dialog as sm_dialog_clean
from models.shared.tools.Temporizador import Temporizador
from PyQt5 import QtWidgets


class Dialog:
    @staticmethod
    def mostrar_dialogo(titulo, mensaje):
        Temporizador.iniciar(1)

        new_dialog = QtWidgets.QDialog()
        new_ui = sm_dialog_clean()
        new_ui.setupUi(new_dialog)
        new_dialog.setModal(True)
        new_dialog.show()
        new_ui.lbl_title.setText(titulo)
        new_ui.lbl_body.setText(mensaje)

        new_dialog.exec()
