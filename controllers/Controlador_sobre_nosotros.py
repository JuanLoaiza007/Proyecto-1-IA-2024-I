# [Controlador_sobre_nosotros.py]

from views.Vista_sobre_nosotros import Ui_MainWindow
from models.Modelo_sobre_nosotros import Modelo_sobre_nosotros


class Controlador_sobre_nosotros:
    # Funcion para inicializar (general)
    def cargar(self, main_window):
        self.modelo = Modelo_sobre_nosotros()
        self.MainWindow = main_window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

        # Listeners específicos
        self.ui.btn_volver.clicked.connect(self.volver)

    def mostrar(self, main_window):
        self.cargar(main_window)
        self.MainWindow.show()

    def volver(self):
        from controllers.Controlador_principal import Controlador_principal
        self.controlador_principal = Controlador_principal()
        self.controlador_principal.mostrar(self.MainWindow)
