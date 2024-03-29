# [main.py]

from controllers.Controlador_principal import Controlador_principal as Controlador
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget
import sys


def center(main_window: QMainWindow):
    qr = main_window.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    main_window.move(qr.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    center(main_window)
    controlador = Controlador()
    controlador.mostrar(main_window)
    sys.exit(app.exec_())
