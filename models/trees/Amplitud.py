# [Amplitud.py]

from models.shared.Estructuras_datos import *

evitar_devolverse = True
evitar_ciclo = True

debug = True


def print_debug(message):
    new_message = "Amplitud.py: " + message
    if debug:
        print(new_message)


class Amplitud:
    @staticmethod
    def busqueda_preferente_por_amplitud(problema: Problema):
        cola = Queue()
        cola.put(Nodo(problema))  # Agrega el nodo raíz a la cola

        while not cola.empty():
            nodo: Nodo = cola.get()  # Saca un nodo de la cola

            if nodo.es_meta():
                camino = Amplitud.reconstruir_camino(nodo)
                return camino, 'Encontré a grogu'

            # Expande el nodo y obtiene sus hijos
            hijos: "list[Nodo]" = nodo.expandir()
            for hijo in hijos:

                if evitar_devolverse and Amplitud.se_ha_devuelto(hijo):
                    print_debug("paso, {} es igual a {}".format(
                        str(hijo.get_estado()), str(nodo.get_padre().get_estado())))
                    continue

                if evitar_ciclo and Amplitud.cayo_en_ciclo(hijo):
                    print_debug("paso, se ha repetido el antecesor{}".format(
                        str(hijo.get_estado())))
                    continue
                cola.put(hijo)  # Agrega los hijos a la cola

        camino = Amplitud.reconstruir_camino(nodo)
        return camino, 'Me perdí'

    @staticmethod
    def reconstruir_camino(nodo: Nodo):
        # Reconstruir el camino desde el nodo solución hasta el nodo raíz
        camino = []
        while nodo is not None:
            estado = nodo.get_estado()
            camino.append(estado.get_coordenadas())
            nodo = nodo.get_padre()
        # Revertir el camino para que esté en orden desde el nodo raíz hasta la solución
        return camino[::-1]

    @staticmethod
    def se_ha_devuelto(nodo: Nodo):
        # El nodo no tiene padre o abuelo
        if nodo.get_profundidad() <= 1:
            return False

        abuelo = nodo.get_padre().get_padre()
        nodo = nodo

        # El nodo es igual a su abuelo, se esta devolviendo
        if ((str(nodo.get_estado()) == str(abuelo.get_estado()))):
            return True

        return False

    @staticmethod
    def cayo_en_ciclo(nodo: Nodo):
        # El nodo no tiene padre o abuelo
        if nodo.get_profundidad() <= 1:
            return False

        antecesor = nodo.get_padre().get_padre()
        nodo = nodo

        while (antecesor != None):
            # El nodo es igual a un antecesor, cayo a un ciclo
            if ((str(nodo.get_estado()) == str(antecesor.get_estado()))):
                return True
            antecesor = antecesor.get_padre()

        return False


class Test():
    @staticmethod
    def start():
        from models.shared.tools.World_tools import World_tools as wtools
        from models.shared.tools.File_selector import File_selector

        env_objects_dic = wtools.reconocer_objetos()

        # Cargar archivo de mundo
        file_selector = File_selector()
        archivo = file_selector.select("data/worlds")

        ambiente = wtools.generar_mundo(archivo)

        # Inicializar estado inicial y estado objetivo
        x_ini, y_ini = wtools.determinar_posicion(
            ambiente, env_objects_dic['agente'])
        x_meta, y_meta = wtools.determinar_posicion(
            ambiente, env_objects_dic['meta'])

        # Inicializar estados
        estado_inicial = Estado(x_ini, y_ini)
        estado_objetivo = Estado(x_meta, y_meta)

        # Eliminar el self.estado_inicial del ambiente
        ambiente[x_ini][y_ini] = "0"

        problema = Problema(estado_inicial, estado_objetivo, ambiente)

        print(Amplitud.busqueda_preferente_por_amplitud(problema))

# <pseudocódigo>
# function BUSQUEDA-PREFERENTE-POR-AMPLITUD(problema) returns solución o falla
#     Cola cola
#     cola = nodo_raiz(problema)
#     while not estaVacia(cola) do
#         n = sacar(cola)
#         if n es un nodo meta then
#             return encontró solución
#         expandir(n) y meter todos sus hijos al final de la cola
#     return falló
