# main.py

from controllers.controlador_principal import controlador_principal
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    controlador_principal = controlador_principal()
    controlador_principal.mostrar(main_window)
    sys.exit(app.exec_())
