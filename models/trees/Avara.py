# [Avara.py]

from models.shared.Estructuras_datos import *
import time
from queue import PriorityQueue
from models.trees.CommonTreeUtils import CommonTreeUtils as common

evitar_devolverse = True
evitar_ciclo = True

debug = False


def print_debug(message):
    new_message = "Avara.py: " + message
    if debug:
        print(new_message)


class Avara:
    def busqueda_por_avara(problema: Problema):
        nodos_expandidos = 0
        profundidad = 0
        reporte = "Generando..."

        tiempo_inicio = time.time()
        cola_prioridad = PriorityQueue()
        nodo_inicial = Nodo(problema)
        heuristica = nodo_inicial.calcular_heuristica()
        cola_prioridad.put((heuristica, nodo_inicial))

        # while not len(cola_prioridad) == 0:
        while not cola_prioridad.empty():
            print_debug("La cola de prioridad actual es {}".format(
                str(cola_prioridad)))
            heuristica, nodo = cola_prioridad.get()  # Saca un nodo de la cola
            print_debug("{}".format(str(heuristica)))
            print_debug("{}".format(str(nodo)))
            print_debug("{}".format(str(heuristica), str(nodo)))

            if nodo.es_meta():
                camino = common.reconstruir_camino(nodo)
                reporte = common.generar_reporte(
                    nodos_expandidos, profundidad, tiempo_inicio, nodo)

                return camino, 'Encontré a grogu', reporte

            # Expande el nodo y obtiene sus hijos
            hijos: "list[Nodo]" = nodo.expandir()

            # Actualiza cantidad de nodos expandidos
            nodos_expandidos += 1

            for hijo in hijos:
                print_debug(f"El hijo actual es {hijo}")
                # Actualiza profundidad
                if profundidad < hijo.get_profundidad():
                    profundidad = hijo.get_profundidad()

                if evitar_devolverse and common.se_ha_devuelto(hijo):
                    print_debug("paso, queria ir a {} pero hace dos pasos estuve en {}".format(
                        str(hijo.get_estado()), str(nodo.get_padre().get_estado())))
                    continue

                if evitar_ciclo and common.cayo_en_ciclo(hijo):
                    print_debug("paso, hace un tiempo estuve en {}, evitare entrar en ciclo".format(
                        str(hijo.get_estado())))
                    continue

                # Agrega los hijos a la cola
                heuristica = hijo.calcular_heuristica()
                cola_prioridad.put((heuristica, hijo))
                print_debug("{}".format(str(heuristica)))
                print_debug("{}".format(str(hijo)))
                print_debug("{} {}".format(
                    str(hijo.get_costo_acumulado()), str(hijo)))
                print_debug("{}".format(str(cola_prioridad)))

        camino = common.reconstruir_camino(nodo)
        reporte = common.generar_reporte(
            nodos_expandidos, profundidad, tiempo_inicio, nodo)

        return camino, 'Me perdí', reporte


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

        print(Avara.busqueda_por_avara(problema))
