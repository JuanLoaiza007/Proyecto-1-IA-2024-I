# controlador_principal.py

from views.vista_principal import Ui_MainWindow
from models.modelo_principal import modelo_principal


class controlador_principal:
    # Funcion para inicializar (general)
    def cargar(self, main_window):
        self.modelo = modelo_principal()
        self.MainWindow = main_window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

        # Listeners específicos
        self.ui.btn_saludar.clicked.connect(self.saludar)
        self.ui.btn_sobre.clicked.connect(self.mostrar_sobre_nosotros)

    def mostrar(self, main_window):
        self.cargar(main_window)
        self.MainWindow.show()

    # Funciones especificas
    def saludar(self):
        nombre = self.ui.txta_nombre.toPlainText()
        print("Hola", nombre)

    def mostrar_sobre_nosotros(self):
        from controllers.controlador_sobre_nosotros import controlador_sobre_nosotros
        self.controlador_sobre_nosotros = controlador_sobre_nosotros()
        self.controlador_sobre_nosotros.mostrar(self.MainWindow)
