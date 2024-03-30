# [main.py]

from controllers.Controlador_principal import Controlador_principal as Controlador
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    controlador = Controlador()
    controlador.mostrar(main_window)
    sys.exit(app.exec_())
