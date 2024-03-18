# controlador_sobre_nosotros.py

from views.vista_sobre_nosotros import Ui_MainWindow
from models.modelo_sobre_nosotros import modelo_sobre_nosotros


class controlador_sobre_nosotros:
    # Funcion para inicializar (general)
    def cargar(self, main_window):
        self.modelo = modelo_sobre_nosotros()
        self.MainWindow = main_window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

        # Listeners específicos
        self.ui.btn_volver.clicked.connect(self.volver)

    def mostrar(self, main_window):
        self.cargar(main_window)
        self.MainWindow.show()

    def volver(self):
        from controllers.controlador_principal import controlador_principal
        self.controlador_principal = controlador_principal()
        self.controlador_principal.mostrar(self.MainWindow)
