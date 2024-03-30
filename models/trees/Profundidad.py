# [Profundidad.py]

import time
from models.shared.Estructuras_datos import *

evitar_devolverse = True
evitar_ciclo = True

debug = True


def print_debug(message):
    new_message = "Profundidad.py: " + message
    if debug:
        print(new_message)


class Profundidad:
    @staticmethod
    def busqueda_preferente_por_profundidad(problema: Problema):
        nodos_expandidos = 0
        profundidad = 0
        reporte = ""

        tiempo_inicio = time.time()
        pila = list()
        pila.append(Nodo(problema))  # Agrega el nodo raíz a la cola

        while len(pila) != 0:
            nodo: Nodo = pila.pop()  # Saca un nodo de la cola

            if nodo.es_meta():
                camino = Profundidad.reconstruir_camino(nodo)
                reporte = Profundidad.generar_reporte(
                    nodos_expandidos, profundidad, tiempo_inicio)

                return camino, 'Encontré a grogu', reporte

            # Expande el nodo y obtiene sus hijos
            hijos: "list[Nodo]" = nodo.expandir()

            # Actualiza cantidad de nodos expandidos
            nodos_expandidos += 1

            for hijo in hijos:

                # Actualiza profundidad
                if profundidad < hijo.get_profundidad():
                    profundidad = hijo.get_profundidad()

                if evitar_devolverse and Profundidad.se_ha_devuelto(hijo):
                    print_debug("paso, queria ir a {} pero hace dos pasos estuve en {}".format(
                        str(hijo.get_estado()), str(nodo.get_padre().get_estado())))
                    continue

                if evitar_ciclo and Profundidad.cayo_en_ciclo(hijo):
                    print_debug("paso, hace un tiempo estuve en {}, evitare entrar en ciclo".format(
                        str(hijo.get_estado())))
                    continue
                pila.append(hijo)  # Agrega los hijos a la cola

        camino = Profundidad.reconstruir_camino(nodo)
        reporte = Profundidad.generar_reporte(
            nodos_expandidos, profundidad, tiempo_inicio)

        return camino, 'Me perdí', reporte

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

    @staticmethod
    def generar_reporte(nodos_expandidos, profundidad, tiempo_inicio):
        tiempo_computo = round(time.time() - tiempo_inicio, 6)
        return "Cantidad de nodos expandidos: {}\nProfundidad del arbol: {}\nTiempo de computo: {} s".format(
            str(nodos_expandidos), str(profundidad), str(tiempo_computo))


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

        print(Profundidad.busqueda_preferente_por_profundidad(problema))
