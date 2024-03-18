from views.sm_dialog_clean import Ui_Dialog as sm_dialog_clean
from PyQt5 import QtWidgets


class Dialog:
    @staticmethod
    def mostrar(texto):
        new_dialog = QtWidgets.QDialog()
        new_ui = sm_dialog_clean()
        new_ui.setupUi(new_dialog)
        new_ui.lbl_main_text.setText(texto)
        new_dialog.setModal(True)
        new_dialog.show()
        new_dialog.exec()
