# [Modelo_principal.py]

from models.shared.tools.File_selector import File_selector
from models.shared.tools.World_tools import World_tools as wtools

debug = False


def print_debug(message):
    new_message = "Modelo_principal.py: " + message
    if debug:
        print(new_message)


class Modelo_principal:
    def __init__(self) -> None:
        self.tipo_busqueda = None
        self.algoritmo_actual = None
        self.algoritmos_disponibles = None
        self.mundo = None
        self.algoritmos_informada = ["avara", "a*"]
        self.algoritmos_no_informada = ["amplitud", "costo", "profundidad"]

    def get_tipo_busqueda(self):
        return self.tipo_busqueda

    def get_algoritmo_actual(self):
        return self.algoritmo_actual

    def get_algoritmos_disponibles(self):
        return self.algoritmos_disponibles

    def get_mundo(self):
        return self.mundo

    def select_tipo_busqueda(self, tipo_busqueda):
        self.tipo_busqueda = tipo_busqueda

        if self.tipo_busqueda == "informada":
            self.algoritmos_disponibles = self.algoritmos_informada
        elif self.tipo_busqueda == "no-informada":
            self.algoritmos_disponibles = self.algoritmos_no_informada
        else:
            print_debug("Hay un problema, el tipo de busqueda obtenido fue: {}".format(
                str(self.tipo_busqueda)))

        print_debug("Se ha seleccionado busqueda {} y se han seleccionado los algoritmos {}".format(
            str(self.tipo_busqueda), str(self.algoritmos_disponibles)))

    def select_busqueda_informada(self):
        self.select_tipo_busqueda("informada")

    def select_busqueda_no_informada(self):
        self.select_tipo_busqueda("no-informada")

    def select_algoritmo(self, algoritmo):
        if self.tipo_busqueda == "informada" and algoritmo in self.algoritmos_informada:
            self.algoritmo_actual = algoritmo
        elif self.tipo_busqueda == "no-informada" and algoritmo in self.algoritmos_no_informada:
            self.algoritmo_actual = algoritmo
        else:
            print_debug("Hay un problema, el tipo de busqueda actual es {} y el algoritmo solicitado fue {}".format(
                str(self.tipo_busqueda), str(algoritmo)))
            return None

        print_debug("Se ha seleccionado busqueda {} y algoritmo {}".format(
            str(self.tipo_busqueda), str(self.algoritmo_actual)))
        return self.algoritmos_disponibles

    def select_algoritmo_amplitud(self):
        self.select_algoritmo("amplitud")

    def select_algoritmo_costo(self):
        self.select_algoritmo("costo")

    def select_algoritmo_profundidad(self):
        self.select_algoritmo("profundidad")

    def select_algoritmo_avara(self):
        self.select_algoritmo("avara")

    def select_algoritmo_a_ast(self):
        self.select_algoritmo("a*")

    def cargar_mundo(self):
        try:
            # Cargar archivo de mundo
            file_selector = File_selector()
            archivo = file_selector.select("data/worlds")

            errores = wtools.comprobar_mundo(archivo)

            if len(errores) != 0:
                self.mundo = None
                return errores

            self.mundo = wtools.generar_mundo(archivo)
        except TypeError:
            self.mundo = None
            print_debug(
                "cargar_mundo() -> He absorbido un error ocasionado por una ruta de archivo inválida")
            return None
