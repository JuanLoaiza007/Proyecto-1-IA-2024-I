# main.py

from controllers.Controlador_juego import Controlador_juego as controlador
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    controlador = controlador()
    controlador.mostrar(main_window)
    sys.exit(app.exec_())
